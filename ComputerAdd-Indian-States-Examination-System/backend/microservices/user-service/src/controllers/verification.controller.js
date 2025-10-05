const User = require('../models/User');
const crypto = require('crypto');
const emailService = require('../services/notification.service');

/**
 * Email Verification Controller
 */
exports.sendVerificationEmail = async (req, res) => {
  try {
    const { email } = req.body;
    
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(404).json({
        success: false,
        message: 'User not found'
      });
    }
    
    if (user.emailVerified) {
      return res.status(400).json({
        success: false,
        message: 'Email already verified'
      });
    }
    
    // Generate verification token
    const verificationToken = crypto.randomBytes(32).toString('hex');
    user.emailVerificationToken = verificationToken;
    user.emailVerificationExpires = Date.now() + 24 * 60 * 60 * 1000; // 24 hours
    
    await user.save();
    
    // Send email
    await emailService.sendVerificationEmail(email, verificationToken);
    
    res.json({
      success: true,
      message: 'Verification email sent'
    });
    
  } catch (error) {
    console.error('Send verification error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to send verification email'
    });
  }
};

exports.verifyEmail = async (req, res) => {
  try {
    const { token } = req.params;
    
    const user = await User.findOne({
      emailVerificationToken: token,
      emailVerificationExpires: { $gt: Date.now() }
    });
    
    if (!user) {
      return res.status(400).json({
        success: false,
        message: 'Invalid or expired verification token'
      });
    }
    
    user.emailVerified = true;
    user.emailVerificationToken = undefined;
    user.emailVerificationExpires = undefined;
    
    await user.save();
    
    res.json({
      success: true,
      message: 'Email verified successfully'
    });
    
  } catch (error) {
    console.error('Email verification error:', error);
    res.status(500).json({
      success: false,
      message: 'Email verification failed'
    });
  }
};

exports.sendPhoneOTP = async (req, res) => {
  try {
    const { userId } = req.user;
    const { phoneNumber } = req.body;
    
    const user = await User.findById(userId);
    if (!user) {
      return res.status(404).json({
        success: false,
        message: 'User not found'
      });
    }
    
    // Generate 6-digit OTP
    const otp = Math.floor(100000 + Math.random() * 900000).toString();
    
    user.phoneOTP = otp;
    user.phoneOTPExpires = Date.now() + 10 * 60 * 1000; // 10 minutes
    user.profile.phoneNumber = phoneNumber;
    
    await user.save();
    
    // Send SMS (placeholder)
    console.log(`OTP for ${phoneNumber}: ${otp}`);
    
    res.json({
      success: true,
      message: 'OTP sent to phone'
    });
    
  } catch (error) {
    console.error('Send OTP error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to send OTP'
    });
  }
};

exports.verifyPhone = async (req, res) => {
  try {
    const { userId } = req.user;
    const { otp } = req.body;
    
    const user = await User.findOne({
      _id: userId,
      phoneOTP: otp,
      phoneOTPExpires: { $gt: Date.now() }
    });
    
    if (!user) {
      return res.status(400).json({
        success: false,
        message: 'Invalid or expired OTP'
      });
    }
    
    user.phoneVerified = true;
    user.phoneOTP = undefined;
    user.phoneOTPExpires = undefined;
    
    await user.save();
    
    res.json({
      success: true,
      message: 'Phone verified successfully'
    });
    
  } catch (error) {
    console.error('Phone verification error:', error);
    res.status(500).json({
      success: false,
      message: 'Phone verification failed'
    });
  }
};
