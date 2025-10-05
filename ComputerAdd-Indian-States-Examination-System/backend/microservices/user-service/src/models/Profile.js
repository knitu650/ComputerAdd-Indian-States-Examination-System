const mongoose = require('mongoose');

const profileSchema = new mongoose.Schema({
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true,
    unique: true
  },
  
  personalInfo: {
    firstName: { type: String, required: true },
    lastName: { type: String, required: true },
    dateOfBirth: Date,
    gender: { type: String, enum: ['male', 'female', 'other'] },
    phoneNumber: String,
    alternateEmail: String
  },
  
  address: {
    street: String,
    city: String,
    state: String,
    pincode: String,
    country: { type: String, default: 'India' }
  },
  
  education: [{
    degree: String,
    institution: String,
    yearOfCompletion: Number,
    percentage: Number
  }],
  
  preferences: {
    language: { type: String, default: 'en' },
    theme: { type: String, enum: ['light', 'dark'], default: 'light' },
    notifications: {
      email: { type: Boolean, default: true },
      sms: { type: Boolean, default: false },
      push: { type: Boolean, default: true }
    }
  },
  
  examPreferences: {
    preferredStates: [String],
    preferredDifficulty: { type: String, enum: ['easy', 'medium', 'hard'] },
    preferredTopics: [String]
  },
  
  achievements: [{
    title: String,
    description: String,
    icon: String,
    earnedAt: { type: Date, default: Date.now }
  }],
  
  socialProfiles: {
    linkedin: String,
    twitter: String,
    facebook: String
  }
  
}, { timestamps: true });

module.exports = mongoose.model('Profile', profileSchema);
