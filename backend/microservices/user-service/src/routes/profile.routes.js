const express = require('express');
const router = express.Router();
const { getProfile, updateProfile } = require('../controllers/profile.controller');
const authMiddleware = require('../middleware/auth.middleware'); // Assuming auth middleware is created

// A placeholder for auth middleware
const protect = (req, res, next) => {
    // In a real app, this would validate the JWT and set req.user
    // For now, we'll simulate it for development
    req.user = { id: 'some-user-id' }; // Replace with actual user logic
    next();
};


router.route('/')
    .post(protect, updateProfile);

router.route('/me')
    .get(protect, getProfile);

module.exports = router;