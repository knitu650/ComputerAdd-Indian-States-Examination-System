const mongoose = require('mongoose');

/**
 * Exam Model Schema
 * Comprehensive examination structure
 */

const examSchema = new mongoose.Schema({
  // Basic Information
  title: {
    type: String,
    required: [true, 'Exam title is required'],
    trim: true,
    maxlength: [200, 'Title cannot exceed 200 characters']
  },

  description: {
    type: String,
    required: [true, 'Exam description is required'],
    maxlength: [2000, 'Description cannot exceed 2000 characters']
  },

  code: {
    type: String,
    required: true,
    unique: true,
    uppercase: true
  },

  // Exam Configuration
  type: {
    type: String,
    enum: ['practice', 'mock', 'actual', 'competition', 'assessment'],
    required: true
  },

  category: {
    type: String,
    enum: ['indian-states', 'geography', 'history', 'culture', 'mixed', 'custom'],
    default: 'indian-states'
  },

  difficulty: {
    type: String,
    enum: ['beginner', 'intermediate', 'advanced', 'expert'],
    default: 'intermediate'
  },

  // States Coverage
  states: [{
    name: String,
    weightage: Number // Percentage of questions from this state
  }],

  // Question Configuration
  questionsConfig: {
    totalQuestions: {
      type: Number,
      required: true,
      min: 1,
      max: 500
    },
    
    questionTypes: [{
      type: {
        type: String,
        enum: ['mcq', 'true-false', 'image-based', 'audio', 'drag-drop', 'interactive-map']
      },
      count: Number,
      marks: Number
    }],

    difficultyDistribution: {
      easy: {
        type: Number,
        default: 30 // percentage
      },
      medium: {
        type: Number,
        default: 50
      },
      hard: {
        type: Number,
        default: 20
      }
    },

    adaptiveTesting: {
      enabled: {
        type: Boolean,
        default: false
      },
      algorithm: {
        type: String,
        enum: ['irt', 'cat', 'linear'],
        default: 'cat'
      }
    }
  },

  // Scoring Configuration
  scoring: {
    totalMarks: {
      type: Number,
      required: true
    },
    
    passingMarks: {
      type: Number,
      required: true
    },
    
    passingPercentage: {
      type: Number,
      min: 0,
      max: 100
    },

    negativeMarking: {
      enabled: {
        type: Boolean,
        default: false
      },
      deduction: {
        type: Number,
        default: 0.25 // Marks to deduct
      }
    },

    partialMarking: {
      enabled: {
        type: Boolean,
        default: false
      }
    }
  },

  // Time Configuration
  duration: {
    type: Number,
    required: true, // in minutes
    min: 5,
    max: 360
  },

  schedule: {
    startDate: {
      type: Date,
      required: true
    },
    
    endDate: {
      type: Date,
      required: true
    },
    
    timezone: {
      type: String,
      default: 'Asia/Kolkata'
    },

    allowLateEntry: {
      type: Boolean,
      default: false
    },

    lateEntryBuffer: {
      type: Number,
      default: 0 // minutes
    }
  },

  // Access Control
  access: {
    visibility: {
      type: String,
      enum: ['public', 'private', 'restricted'],
      default: 'public'
    },

    requiresRegistration: {
      type: Boolean,
      default: true
    },

    maxAttempts: {
      type: Number,
      default: 1,
      min: 1,
      max: 10
    },

    allowedUsers: [{
      type: mongoose.Schema.Types.ObjectId,
      ref: 'User'
    }],

    restrictedStates: [String], // Only users from these states

    prerequisites: [{
      examId: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Exam'
      },
      minimumScore: Number
    }]
  },

  // Proctoring Settings
  proctoring: {
    enabled: {
      type: Boolean,
      default: true
    },

    features: {
      faceDetection: {
        type: Boolean,
        default: true
      },
      
      multiPersonDetection: {
        type: Boolean,
        default: true
      },
      
      phoneDetection: {
        type: Boolean,
        default: true
      },
      
      tabSwitchDetection: {
        type: Boolean,
        default: true
      },
      
      screenRecording: {
        type: Boolean,
        default: true
      },
      
      audioMonitoring: {
        type: Boolean,
        default: false
      },

      browserLock: {
        type: Boolean,
        default: true
      }
    },

    strictness: {
      type: String,
      enum: ['low', 'medium', 'high', 'strict'],
      default: 'medium'
    },

    violationThreshold: {
      type: Number,
      default: 3 // Auto-terminate after this many violations
    }
  },

  // Instructions
  instructions: {
    general: String,
    language: String,
    technical: String,
    examSpecific: String
  },

  // Resources Allowed
  resources: {
    calculator: {
      type: Boolean,
      default: true
    },
    
    roughSheet: {
      type: Boolean,
      default: true
    },
    
    referenceBooks: {
      type: Boolean,
      default: false
    }
  },

  // Multi-language Support
  languages: [{
    code: String,
    name: String,
    enabled: Boolean
  }],

  // Results Configuration
  results: {
    showImmediately: {
      type: Boolean,
      default: false
    },
    
    showAnswers: {
      type: Boolean,
      default: false
    },
    
    showSolutions: {
      type: Boolean,
      default: false
    },
    
    publishDate: Date,
    
    certificateEnabled: {
      type: Boolean,
      default: false
    },

    certificateTemplate: String
  },

  // Analytics
  analytics: {
    totalAttempts: {
      type: Number,
      default: 0
    },
    
    totalCompleted: {
      type: Number,
      default: 0
    },
    
    averageScore: {
      type: Number,
      default: 0
    },
    
    averageTime: {
      type: Number,
      default: 0
    },
    
    passRate: {
      type: Number,
      default: 0
    },

    stateWiseStats: [{
      state: String,
      attempts: Number,
      averageScore: Number,
      passRate: Number
    }]
  },

  // Status
  status: {
    type: String,
    enum: ['draft', 'scheduled', 'active', 'completed', 'cancelled', 'archived'],
    default: 'draft'
  },

  isPublished: {
    type: Boolean,
    default: false
  },

  publishedAt: Date,

  // Creator Information
  createdBy: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },

  lastModifiedBy: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  },

  // Tags and Metadata
  tags: [String],
  
  metadata: {
    version: {
      type: Number,
      default: 1
    },
    
    featured: {
      type: Boolean,
      default: false
    },
    
    trending: {
      type: Boolean,
      default: false
    },
    
    recommendedFor: [String]
  },

  // Questions (populated)
  questions: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Question'
  }],

  // Timestamps
  createdAt: {
    type: Date,
    default: Date.now
  },

  updatedAt: {
    type: Date,
    default: Date.now
  }
}, {
  timestamps: true,
  toJSON: { virtuals: true },
  toObject: { virtuals: true }
});

// Indexes
examSchema.index({ code: 1 });
examSchema.index({ type: 1, status: 1 });
examSchema.index({ 'schedule.startDate': 1, 'schedule.endDate': 1 });
examSchema.index({ category: 1 });
examSchema.index({ createdBy: 1 });
examSchema.index({ isPublished: 1, status: 1 });

// Virtual for exam URL
examSchema.virtual('url').get(function() {
  return `/exams/${this.code}`;
});

// Virtual for is active
examSchema.virtual('isActive').get(function() {
  const now = new Date();
  return (
    this.status === 'active' &&
    this.schedule.startDate <= now &&
    this.schedule.endDate >= now
  );
});

// Virtual for time remaining
examSchema.virtual('timeRemaining').get(function() {
  const now = new Date();
  if (this.schedule.endDate > now) {
    return Math.floor((this.schedule.endDate - now) / 1000 / 60); // minutes
  }
  return 0;
});

// Pre-save middleware
examSchema.pre('save', async function(next) {
  if (this.isModified('scoring.totalMarks') && this.scoring.passingPercentage) {
    this.scoring.passingMarks = (this.scoring.totalMarks * this.scoring.passingPercentage) / 100;
  }

  // Update status based on schedule
  const now = new Date();
  if (this.status === 'scheduled' && this.schedule.startDate <= now && this.schedule.endDate >= now) {
    this.status = 'active';
  } else if (this.status === 'active' && this.schedule.endDate < now) {
    this.status = 'completed';
  }

  next();
});

// Static method to find active exams
examSchema.statics.findActive = function() {
  const now = new Date();
  return this.find({
    status: 'active',
    isPublished: true,
    'schedule.startDate': { $lte: now },
    'schedule.endDate': { $gte: now }
  });
};

// Static method to find upcoming exams
examSchema.statics.findUpcoming = function() {
  const now = new Date();
  return this.find({
    status: 'scheduled',
    isPublished: true,
    'schedule.startDate': { $gt: now }
  }).sort({ 'schedule.startDate': 1 });
};

// Method to check if user can attempt
examSchema.methods.canUserAttempt = async function(userId) {
  // Check if exam is active
  if (!this.isActive) {
    return { allowed: false, reason: 'Exam is not active' };
  }

  // Check access restrictions
  if (this.access.visibility === 'private') {
    const isAllowed = this.access.allowedUsers.some(
      id => id.toString() === userId.toString()
    );
    if (!isAllowed) {
      return { allowed: false, reason: 'You do not have access to this exam' };
    }
  }

  // Check attempts remaining
  const Result = mongoose.model('Result');
  const attempts = await Result.countDocuments({
    examId: this._id,
    userId: userId
  });

  if (attempts >= this.access.maxAttempts) {
    return { allowed: false, reason: 'Maximum attempts reached' };
  }

  return { allowed: true };
};

const Exam = mongoose.model('Exam', examSchema);

module.exports = Exam;
