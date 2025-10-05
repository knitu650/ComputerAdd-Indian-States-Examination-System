const mongoose = require('mongoose');

const ProfileSchema = new mongoose.Schema({
    user: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User',
        required: true,
    },
    firstName: {
        type: String,
        trim: true,
    },
    lastName: {
        type: String,
        trim: true,
    },
    dateOfBirth: {
        type: Date,
    },
    address: {
        street: String,
        city: String,
        state: String,
        zipCode: String,
    },
    phone: {
        type: String,
    },
    profilePicture: {
        type: String, // URL to the image
    },
    updatedAt: {
        type: Date,
        default: Date.now,
    },
});

ProfileSchema.pre('save', function(next) {
    this.updatedAt = Date.now();
    next();
});

module.exports = mongoose.model('Profile', ProfileSchema);