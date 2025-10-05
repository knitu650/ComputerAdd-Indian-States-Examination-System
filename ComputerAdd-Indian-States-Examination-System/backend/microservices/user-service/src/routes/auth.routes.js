const express = require('express');
const router = express.Router();
const authController = require('../controllers/auth.controller');
const { authMiddleware } = require('../middleware/auth.middleware');

/**
 * Authentication Routes
 */

// Register new user
router.post('/register', authController.register.bind(authController));

// Login
router.post('/login', authController.login.bind(authController));

// Verify email
router.get('/verify-email/:token', authController.verifyEmail.bind(authController));

// Forgot password
router.post('/forgot-password', authController.forgotPassword.bind(authController));

// Reset password
router.post('/reset-password/:token', authController.resetPassword.bind(authController));

// Change password (authenticated)
router.post('/change-password', authMiddleware, authController.changePassword.bind(authController));

// Refresh token
router.post('/refresh-token', authController.refreshToken.bind(authController));

// Logout
router.post('/logout', authMiddleware, authController.logout.bind(authController));

module.exports = router;
