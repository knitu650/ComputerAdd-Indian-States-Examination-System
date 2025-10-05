const Profile = require('../models/Profile');
const User = require('../models/User');

// @desc    Get user profile
// @route   GET /profile/me
// @access  Private
const getProfile = async (req, res) => {
    try {
        // The user ID should be available from an authentication middleware
        const profile = await Profile.findOne({ user: req.user.id }).populate('user', ['username', 'email']);

        if (!profile) {
            return res.status(404).json({ message: 'Profile not found' });
        }

        res.json(profile);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Create or update user profile
// @route   POST /profile
// @access  Private
const updateProfile = async (req, res) => {
    const { firstName, lastName, dateOfBirth, address, phone, profilePicture } = req.body;

    const profileFields = {
        user: req.user.id,
        firstName,
        lastName,
        dateOfBirth,
        address,
        phone,
        profilePicture,
    };

    try {
        let profile = await Profile.findOneAndUpdate(
            { user: req.user.id },
            { $set: profileFields },
            { new: true, upsert: true }
        );

        res.json(profile);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

module.exports = {
    getProfile,
    updateProfile,
};