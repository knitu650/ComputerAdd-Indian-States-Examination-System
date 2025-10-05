const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

/**
 * User Model Schema
 * Comprehensive user data structure for examination system
 */

const userSchema = new mongoose.Schema({
  // Basic Information
  email: {
    type: String,
    required: [true, 'Email is required'],
    unique: true,
    lowercase: true,
    trim: true,
    match: [/^\S+@\S+\.\S+$/, 'Please provide a valid email address']
  },

  password: {
    type: String,
    required: [true, 'Password is required'],
    minlength: [8, 'Password must be at least 8 characters'],
    select: false
  },

  // Personal Information
  profile: {
    firstName: {
      type: String,
      required: [true, 'First name is required'],
      trim: true,
      maxlength: [50, 'First name cannot exceed 50 characters']
    },
    
    lastName: {
      type: String,
      required: [true, 'Last name is required'],
      trim: true,
      maxlength: [50, 'Last name cannot exceed 50 characters']
    },
    
    dateOfBirth: {
      type: Date,
      required: [true, 'Date of birth is required']
    },
    
    gender: {
      type: String,
      enum: ['male', 'female', 'other', 'prefer-not-to-say'],
      required: true
    },
    
    phoneNumber: {
      type: String,
      required: [true, 'Phone number is required'],
      match: [/^[0-9]{10}$/, 'Please provide a valid 10-digit phone number']
    },
    
    alternatePhone: {
      type: String,
      match: [/^[0-9]{10}$/, 'Please provide a valid 10-digit phone number']
    },
    
    avatar: {
      type: String,
      default: null
    },
    
    // Address
    address: {
      street: String,
      city: String,
      state: {
        type: String,
        enum: [
          'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
          'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
          'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
          'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
          'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal',
          'Andaman and Nicobar Islands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu',
          'Delhi', 'Jammu and Kashmir', 'Ladakh', 'Lakshadweep', 'Puducherry'
        ]
      },
      pincode: {
        type: String,
        match: [/^[0-9]{6}$/, 'Please provide a valid 6-digit pincode']
      },
      country: {
        type: String,
        default: 'India'
      }
    }
  },

  // Role and Permissions
  role: {
    type: String,
    enum: ['student', 'examiner', 'admin', 'super-admin'],
    default: 'student'
  },

  permissions: [{
    type: String,
    enum: [
      'take_exam', 'create_exam', 'edit_exam', 'delete_exam',
      'view_results', 'manage_users', 'manage_questions',
      'access_analytics', 'manage_system', 'approve_content'
    ]
  }],

  // Account Status
  isVerified: {
    type: Boolean,
    default: false
  },

  isActive: {
    type: Boolean,
    default: true
  },

  isBlocked: {
    type: Boolean,
    default: false
  },

  blockReason: {
    type: String,
    default: null
  },

  // Verification
  emailVerificationToken: {
    type: String,
    select: false
  },

  emailVerifiedAt: {
    type: Date,
    default: null
  },

  phoneVerificationOTP: {
    type: String,
    select: false
  },

  phoneVerifiedAt: {
    type: Date,
    default: null
  },

  // Security
  twoFactorAuth: {
    enabled: {
      type: Boolean,
      default: false
    },
    secret: {
      type: String,
      select: false
    },
    backupCodes: [{
      type: String,
      select: false
    }]
  },

  biometric: {
    faceData: {
      type: mongoose.Schema.Types.Mixed,
      select: false
    },
    fingerprintData: {
      type: mongoose.Schema.Types.Mixed,
      select: false
    },
    enrolledAt: Date
  },

  // Password Reset
  passwordResetToken: {
    type: String,
    select: false
  },

  passwordResetExpires: {
    type: Date,
    select: false
  },

  passwordChangedAt: {
    type: Date
  },

  // Login History
  lastLogin: {
    type: Date,
    default: null
  },

  lastLoginIP: {
    type: String,
    default: null
  },

  loginHistory: [{
    timestamp: Date,
    ip: String,
    userAgent: String,
    location: String,
    success: Boolean
  }],

  failedLoginAttempts: {
    type: Number,
    default: 0
  },

  accountLockedUntil: {
    type: Date,
    default: null
  },

  // Preferences
  preferences: {
    language: {
      type: String,
      enum: [
        'en', 'hi', 'ta', 'te', 'kn', 'ml', 'gu', 'mr', 'bn', 'pa',
        'as', 'or', 'ur', 'sa', 'ks', 'sd', 'ne', 'kok', 'mai', 'mni', 'doi', 'sat'
      ],
      default: 'en'
    },
    theme: {
      type: String,
      enum: ['light', 'dark', 'auto'],
      default: 'light'
    },
    notifications: {
      email: {
        type: Boolean,
        default: true
      },
      sms: {
        type: Boolean,
        default: true
      },
      push: {
        type: Boolean,
        default: true
      },
      inApp: {
        type: Boolean,
        default: true
      }
    },
    examSettings: {
      fontSize: {
        type: String,
        enum: ['small', 'medium', 'large'],
        default: 'medium'
      },
      calculatorEnabled: {
        type: Boolean,
        default: true
      },
      soundEnabled: {
        type: Boolean,
        default: true
      }
    }
  },

  // Statistics
  stats: {
    totalExamsTaken: {
      type: Number,
      default: 0
    },
    totalExamsPassed: {
      type: Number,
      default: 0
    },
    averageScore: {
      type: Number,
      default: 0
    },
    totalStudyTime: {
      type: Number,
      default: 0
    },
    rank: {
      type: Number,
      default: null
    },
    badges: [{
      name: String,
      icon: String,
      earnedAt: Date
    }]
  },

  // Subscription
  subscription: {
    plan: {
      type: String,
      enum: ['free', 'basic', 'premium', 'enterprise'],
      default: 'free'
    },
    startDate: Date,
    endDate: Date,
    autoRenew: {
      type: Boolean,
      default: false
    },
    paymentMethod: String
  },

  // Device Information
  devices: [{
    deviceId: String,
    deviceName: String,
    deviceType: {
      type: String,
      enum: ['web', 'android', 'ios']
    },
    lastUsed: Date,
    fcmToken: String
  }],

  // Timestamps
  createdAt: {
    type: Date,
    default: Date.now
  },

  updatedAt: {
    type: Date,
    default: Date.now
  },

  deletedAt: {
    type: Date,
    default: null
  }
}, {
  timestamps: true,
  toJSON: {
    virtuals: true,
    transform: function(doc, ret) {
      delete ret.password;
      delete ret.passwordResetToken;
      delete ret.emailVerificationToken;
      delete ret.phoneVerificationOTP;
      delete ret.twoFactorAuth;
      delete ret.__v;
      return ret;
    }
  }
});

// Indexes
userSchema.index({ email: 1 });
userSchema.index({ 'profile.phoneNumber': 1 });
userSchema.index({ role: 1 });
userSchema.index({ isActive: 1, isBlocked: 1 });
userSchema.index({ createdAt: -1 });

// Virtual for full name
userSchema.virtual('fullName').get(function() {
  return `${this.profile.firstName} ${this.profile.lastName}`;
});

// Pre-save middleware to hash password
userSchema.pre('save', async function(next) {
  // Only hash if password is modified
  if (!this.isModified('password')) return next();

  try {
    // Hash password with bcrypt
    const salt = await bcrypt.genSalt(12);
    this.password = await bcrypt.hash(this.password, salt);
    
    // Set password changed timestamp
    if (!this.isNew) {
      this.passwordChangedAt = Date.now() - 1000;
    }
    
    next();
  } catch (error) {
    next(error);
  }
});

// Method to compare passwords
userSchema.methods.comparePassword = async function(candidatePassword) {
  return await bcrypt.compare(candidatePassword, this.password);
};

// Method to check if password was changed after JWT was issued
userSchema.methods.changedPasswordAfter = function(JWTTimestamp) {
  if (this.passwordChangedAt) {
    const changedTimestamp = parseInt(this.passwordChangedAt.getTime() / 1000, 10);
    return JWTTimestamp < changedTimestamp;
  }
  return false;
};

// Method to increment failed login attempts
userSchema.methods.incrementFailedAttempts = async function() {
  this.failedLoginAttempts += 1;

  // Lock account after 5 failed attempts
  if (this.failedLoginAttempts >= 5) {
    this.accountLockedUntil = new Date(Date.now() + 30 * 60 * 1000); // 30 minutes
  }

  await this.save();
};

// Method to reset failed login attempts
userSchema.methods.resetFailedAttempts = async function() {
  this.failedLoginAttempts = 0;
  this.accountLockedUntil = null;
  await this.save();
};

// Method to check if account is locked
userSchema.methods.isAccountLocked = function() {
  return this.accountLockedUntil && this.accountLockedUntil > Date.now();
};

// Static method to find by credentials
userSchema.statics.findByCredentials = async function(email, password) {
  const user = await this.findOne({ email }).select('+password');
  
  if (!user) {
    throw new Error('Invalid credentials');
  }

  const isPasswordValid = await user.comparePassword(password);
  
  if (!isPasswordValid) {
    await user.incrementFailedAttempts();
    throw new Error('Invalid credentials');
  }

  if (user.isAccountLocked()) {
    throw new Error('Account is temporarily locked');
  }

  await user.resetFailedAttempts();
  return user;
};

const User = mongoose.model('User', userSchema);

module.exports = User;
