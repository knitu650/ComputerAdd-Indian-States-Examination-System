const express = require('express');
const router = express.Router();
const verificationController = require('../controllers/verification.controller');
const authMiddleware = require('../middleware/auth.middleware');

// Send verification email
router.post('/email/send', verificationController.sendVerificationEmail);

// Verify email with token
router.get('/email/verify/:token', verificationController.verifyEmail);

// Send phone OTP (protected)
router.post('/phone/send', authMiddleware, verificationController.sendPhoneOTP);

// Verify phone OTP (protected)
router.post('/phone/verify', authMiddleware, verificationController.verifyPhone);

module.exports = router;
