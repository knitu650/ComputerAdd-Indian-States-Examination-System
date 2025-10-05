const mongoose = require('mongoose');

const verificationSchema = new mongoose.Schema({
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  
  type: {
    type: String,
    enum: ['email', 'phone', 'identity', 'document'],
    required: true
  },
  
  status: {
    type: String,
    enum: ['pending', 'verified', 'rejected', 'expired'],
    default: 'pending'
  },
  
  token: String,
  otp: String,
  expiresAt: Date,
  
  verificationData: {
    email: String,
    phoneNumber: String,
    documentType: String,
    documentNumber: String,
    documentImage: String
  },
  
  attempts: {
    type: Number,
    default: 0
  },
  
  maxAttempts: {
    type: Number,
    default: 3
  },
  
  verifiedAt: Date,
  verifiedBy: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  },
  
  rejectionReason: String,
  
  metadata: {
    ipAddress: String,
    userAgent: String,
    location: String
  }
  
}, { timestamps: true });

// Indexes
verificationSchema.index({ userId: 1, type: 1 });
verificationSchema.index({ expiresAt: 1 }, { expireAfterSeconds: 0 });

module.exports = mongoose.model('Verification', verificationSchema);
