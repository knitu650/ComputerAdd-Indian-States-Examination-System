const User = require('../models/User');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const { sendVerificationEmail, sendPasswordResetEmail } = require('../services/notification.service');
const { encrypt, decrypt } = require('../services/encryption.service');

/**
 * Authentication Controller
 * Handles user authentication operations
 */

class AuthController {
  /**
   * Register new user
   */
  async register(req, res) {
    try {
      const {
        email,
        password,
        profile,
        role = 'student'
      } = req.body;

      // Check if user already exists
      const existingUser = await User.findOne({ email });
      if (existingUser) {
        return res.status(400).json({
          success: false,
          message: 'User already exists with this email',
          error: 'USER_EXISTS'
        });
      }

      // Create new user
      const user = new User({
        email,
        password,
        profile,
        role,
        emailVerificationToken: encrypt(email + Date.now())
      });

      await user.save();

      // Send verification email
      await sendVerificationEmail(user.email, user.emailVerificationToken);

      // Generate JWT token
      const token = this.generateToken(user);
      const refreshToken = this.generateRefreshToken(user);

      res.status(201).json({
        success: true,
        message: 'User registered successfully',
        data: {
          user: {
            id: user._id,
            email: user.email,
            fullName: user.fullName,
            role: user.role,
            isVerified: user.isVerified
          },
          token,
          refreshToken
        }
      });
    } catch (error) {
      console.error('Registration error:', error);
      res.status(500).json({
        success: false,
        message: 'Registration failed',
        error: error.message
      });
    }
  }

  /**
   * Login user
   */
  async login(req, res) {
    try {
      const { email, password, deviceInfo } = req.body;

      // Find user with password field
      const user = await User.findOne({ email }).select('+password');
      
      if (!user) {
        return res.status(401).json({
          success: false,
          message: 'Invalid credentials',
          error: 'INVALID_CREDENTIALS'
        });
      }

      // Check if account is blocked
      if (user.isBlocked) {
        return res.status(403).json({
          success: false,
          message: 'Account is blocked',
          error: 'ACCOUNT_BLOCKED',
          reason: user.blockReason
        });
      }

      // Check if account is locked
      if (user.isAccountLocked()) {
        const lockDuration = Math.ceil((user.accountLockedUntil - Date.now()) / 60000);
        return res.status(403).json({
          success: false,
          message: `Account is locked. Try again in ${lockDuration} minutes`,
          error: 'ACCOUNT_LOCKED'
        });
      }

      // Verify password
      const isPasswordValid = await user.comparePassword(password);
      
      if (!isPasswordValid) {
        await user.incrementFailedAttempts();
        return res.status(401).json({
          success: false,
          message: 'Invalid credentials',
          error: 'INVALID_CREDENTIALS'
        });
      }

      // Reset failed attempts
      await user.resetFailedAttempts();

      // Update login history
      user.lastLogin = new Date();
      user.lastLoginIP = req.ip;
      user.loginHistory.push({
        timestamp: new Date(),
        ip: req.ip,
        userAgent: req.get('user-agent'),
        success: true
      });

      // Update device info if provided
      if (deviceInfo) {
        const existingDevice = user.devices.find(d => d.deviceId === deviceInfo.deviceId);
        if (existingDevice) {
          existingDevice.lastUsed = new Date();
        } else {
          user.devices.push({
            ...deviceInfo,
            lastUsed: new Date()
          });
        }
      }

      await user.save();

      // Generate tokens
      const token = this.generateToken(user);
      const refreshToken = this.generateRefreshToken(user);

      res.json({
        success: true,
        message: 'Login successful',
        data: {
          user: {
            id: user._id,
            email: user.email,
            fullName: user.fullName,
            role: user.role,
            avatar: user.profile.avatar,
            isVerified: user.isVerified,
            preferences: user.preferences
          },
          token,
          refreshToken
        }
      });
    } catch (error) {
      console.error('Login error:', error);
      res.status(500).json({
        success: false,
        message: 'Login failed',
        error: error.message
      });
    }
  }

  /**
   * Verify email
   */
  async verifyEmail(req, res) {
    try {
      const { token } = req.params;

      const user = await User.findOne({ emailVerificationToken: token });
      
      if (!user) {
        return res.status(400).json({
          success: false,
          message: 'Invalid or expired verification token',
          error: 'INVALID_TOKEN'
        });
      }

      user.isVerified = true;
      user.emailVerifiedAt = new Date();
      user.emailVerificationToken = null;

      await user.save();

      res.json({
        success: true,
        message: 'Email verified successfully'
      });
    } catch (error) {
      console.error('Email verification error:', error);
      res.status(500).json({
        success: false,
        message: 'Email verification failed',
        error: error.message
      });
    }
  }

  /**
   * Forgot password
   */
  async forgotPassword(req, res) {
    try {
      const { email } = req.body;

      const user = await User.findOne({ email });
      
      if (!user) {
        // Don't reveal if user exists
        return res.json({
          success: true,
          message: 'If email exists, password reset link has been sent'
        });
      }

      // Generate reset token
      const resetToken = encrypt(user.email + Date.now());
      user.passwordResetToken = resetToken;
      user.passwordResetExpires = new Date(Date.now() + 3600000); // 1 hour

      await user.save();

      // Send password reset email
      await sendPasswordResetEmail(user.email, resetToken);

      res.json({
        success: true,
        message: 'Password reset link has been sent to your email'
      });
    } catch (error) {
      console.error('Forgot password error:', error);
      res.status(500).json({
        success: false,
        message: 'Failed to process password reset',
        error: error.message
      });
    }
  }

  /**
   * Reset password
   */
  async resetPassword(req, res) {
    try {
      const { token } = req.params;
      const { password } = req.body;

      const user = await User.findOne({
        passwordResetToken: token,
        passwordResetExpires: { $gt: Date.now() }
      });

      if (!user) {
        return res.status(400).json({
          success: false,
          message: 'Invalid or expired reset token',
          error: 'INVALID_TOKEN'
        });
      }

      // Update password
      user.password = password;
      user.passwordResetToken = null;
      user.passwordResetExpires = null;
      user.passwordChangedAt = new Date();

      await user.save();

      res.json({
        success: true,
        message: 'Password reset successfully'
      });
    } catch (error) {
      console.error('Reset password error:', error);
      res.status(500).json({
        success: false,
        message: 'Password reset failed',
        error: error.message
      });
    }
  }

  /**
   * Change password
   */
  async changePassword(req, res) {
    try {
      const { currentPassword, newPassword } = req.body;
      const userId = req.user.id;

      const user = await User.findById(userId).select('+password');
      
      if (!user) {
        return res.status(404).json({
          success: false,
          message: 'User not found',
          error: 'USER_NOT_FOUND'
        });
      }

      // Verify current password
      const isPasswordValid = await user.comparePassword(currentPassword);
      
      if (!isPasswordValid) {
        return res.status(401).json({
          success: false,
          message: 'Current password is incorrect',
          error: 'INVALID_PASSWORD'
        });
      }

      // Update password
      user.password = newPassword;
      user.passwordChangedAt = new Date();

      await user.save();

      res.json({
        success: true,
        message: 'Password changed successfully'
      });
    } catch (error) {
      console.error('Change password error:', error);
      res.status(500).json({
        success: false,
        message: 'Password change failed',
        error: error.message
      });
    }
  }

  /**
   * Refresh token
   */
  async refreshToken(req, res) {
    try {
      const { refreshToken } = req.body;

      if (!refreshToken) {
        return res.status(401).json({
          success: false,
          message: 'Refresh token required',
          error: 'TOKEN_REQUIRED'
        });
      }

      // Verify refresh token
      const decoded = jwt.verify(refreshToken, process.env.JWT_SECRET);

      const user = await User.findById(decoded.userId);
      
      if (!user) {
        return res.status(401).json({
          success: false,
          message: 'Invalid refresh token',
          error: 'INVALID_TOKEN'
        });
      }

      // Generate new tokens
      const token = this.generateToken(user);
      const newRefreshToken = this.generateRefreshToken(user);

      res.json({
        success: true,
        data: {
          token,
          refreshToken: newRefreshToken
        }
      });
    } catch (error) {
      console.error('Refresh token error:', error);
      res.status(401).json({
        success: false,
        message: 'Invalid refresh token',
        error: 'INVALID_TOKEN'
      });
    }
  }

  /**
   * Logout
   */
  async logout(req, res) {
    try {
      // In a real implementation, blacklist the token in Redis
      // await redis.set(`blacklist:${token}`, '1', 'EX', 604800); // 7 days

      res.json({
        success: true,
        message: 'Logged out successfully'
      });
    } catch (error) {
      console.error('Logout error:', error);
      res.status(500).json({
        success: false,
        message: 'Logout failed',
        error: error.message
      });
    }
  }

  /**
   * Generate JWT token
   */
  generateToken(user) {
    return jwt.sign(
      {
        userId: user._id,
        email: user.email,
        role: user.role
      },
      process.env.JWT_SECRET,
      {
        expiresIn: process.env.JWT_EXPIRY || '7d'
      }
    );
  }

  /**
   * Generate refresh token
   */
  generateRefreshToken(user) {
    return jwt.sign(
      {
        userId: user._id,
        email: user.email,
        type: 'refresh'
      },
      process.env.JWT_SECRET,
      {
        expiresIn: process.env.JWT_REFRESH_EXPIRY || '30d'
      }
    );
  }
}

module.exports = new AuthController();
