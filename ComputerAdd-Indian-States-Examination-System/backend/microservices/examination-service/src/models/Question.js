const mongoose = require('mongoose');

/**
 * Question Model Schema
 * Supports multiple question types for Indian States examination
 */

const questionSchema = new mongoose.Schema({
  // Question Content
  questionText: {
    type: String,
    required: [true, 'Question text is required'],
    trim: true
  },

  questionType: {
    type: String,
    enum: ['mcq', 'true-false', 'image-based', 'audio', 'drag-drop', 'interactive-map', 'fill-blank', 'match-following'],
    required: true
  },

  // Multi-language Support
  translations: [{
    language: {
      type: String,
      required: true
    },
    questionText: String,
    options: [String],
    hint: String,
    explanation: String
  }],

  // Options (for MCQ, True/False)
  options: [{
    text: {
      type: String,
      required: true
    },
    imageUrl: String,
    audioUrl: String,
    isCorrect: {
      type: Boolean,
      default: false
    },
    order: Number
  }],

  // Correct Answer(s)
  correctAnswers: [{
    type: mongoose.Schema.Types.Mixed // Can be string, number, array, object
  }],

  // Media Assets
  media: {
    imageUrl: String,
    audioUrl: String,
    videoUrl: String,
    mapData: mongoose.Schema.Types.Mixed,
    interactiveElements: mongoose.Schema.Types.Mixed
  },

  // Indian States Specific
  stateInfo: {
    relatedState: {
      type: String,
      enum: [
        'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
        'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
        'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
        'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
        'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal',
        'Andaman and Nicobar Islands', 'Chandigarh', 'Dadra and Nagar Haveli and Daman and Diu',
        'Delhi', 'Jammu and Kashmir', 'Ladakh', 'Lakshadweep', 'Puducherry', 'All'
      ]
    },
    
    category: {
      type: String,
      enum: ['geography', 'history', 'culture', 'government', 'economy', 'demography', 'festivals', 'monuments', 'general']
    },
    
    subcategory: String,
    
    topics: [String]
  },

  // Difficulty and Scoring
  difficulty: {
    type: String,
    enum: ['easy', 'medium', 'hard', 'expert'],
    required: true
  },

  marks: {
    type: Number,
    required: true,
    min: 0
  },

  negativeMarks: {
    type: Number,
    default: 0
  },

  partialMarking: {
    enabled: {
      type: Boolean,
      default: false
    },
    rules: mongoose.Schema.Types.Mixed
  },

  // Time Configuration
  timeLimit: {
    type: Number, // in seconds
    default: 60
  },

  // Hints and Explanation
  hint: {
    type: String,
    default: null
  },

  hintDeduction: {
    type: Number,
    default: 0 // Marks deducted if hint is used
  },

  explanation: {
    type: String,
    required: true
  },

  explanationMedia: {
    imageUrl: String,
    videoUrl: String
  },

  // References
  references: [{
    title: String,
    url: String,
    type: {
      type: String,
      enum: ['book', 'article', 'video', 'website', 'document']
    }
  }],

  // Tags and Metadata
  tags: [String],

  keywords: [String],

  metadata: {
    bloomsTaxonomy: {
      type: String,
      enum: ['remember', 'understand', 'apply', 'analyze', 'evaluate', 'create']
    },
    
    cognitiveLevel: {
      type: String,
      enum: ['knowledge', 'comprehension', 'application', 'analysis', 'synthesis', 'evaluation']
    },
    
    learningObjective: String
  },

  // IRT Parameters (for adaptive testing)
  irt: {
    discrimination: {
      type: Number,
      default: 1
    },
    difficulty: {
      type: Number,
      default: 0
    },
    guessing: {
      type: Number,
      default: 0
    }
  },

  // Analytics
  analytics: {
    totalAttempts: {
      type: Number,
      default: 0
    },
    
    correctAttempts: {
      type: Number,
      default: 0
    },
    
    averageTime: {
      type: Number,
      default: 0
    },
    
    accuracyRate: {
      type: Number,
      default: 0
    },
    
    difficultyIndex: {
      type: Number,
      default: 0
    },
    
    discriminationIndex: {
      type: Number,
      default: 0
    },

    optionDistribution: [{
      option: String,
      count: Number,
      percentage: Number
    }]
  },

  // Status
  status: {
    type: String,
    enum: ['draft', 'review', 'approved', 'published', 'archived'],
    default: 'draft'
  },

  isActive: {
    type: Boolean,
    default: true
  },

  isVerified: {
    type: Boolean,
    default: false
  },

  verifiedBy: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  },

  verifiedAt: Date,

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

  // Version Control
  version: {
    type: Number,
    default: 1
  },

  previousVersions: [{
    version: Number,
    questionData: mongoose.Schema.Types.Mixed,
    modifiedAt: Date,
    modifiedBy: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'User'
    }
  }],

  // Usage Tracking
  usedInExams: [{
    examId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'Exam'
    },
    usedAt: Date
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
questionSchema.index({ questionType: 1, 'stateInfo.relatedState': 1 });
questionSchema.index({ difficulty: 1, 'stateInfo.category': 1 });
questionSchema.index({ status: 1, isActive: 1 });
questionSchema.index({ tags: 1 });
questionSchema.index({ createdBy: 1 });

// Virtual for accuracy percentage
questionSchema.virtual('accuracyPercentage').get(function() {
  if (this.analytics.totalAttempts === 0) return 0;
  return (this.analytics.correctAttempts / this.analytics.totalAttempts) * 100;
});

// Pre-save middleware
questionSchema.pre('save', function(next) {
  // Calculate accuracy rate
  if (this.analytics.totalAttempts > 0) {
    this.analytics.accuracyRate = this.analytics.correctAttempts / this.analytics.totalAttempts;
  }

  // Update difficulty index
  if (this.analytics.totalAttempts >= 30) {
    this.analytics.difficultyIndex = 1 - this.analytics.accuracyRate;
  }

  next();
});

// Static method to find by state and category
questionSchema.statics.findByStateAndCategory = function(state, category) {
  return this.find({
    'stateInfo.relatedState': state,
    'stateInfo.category': category,
    status: 'published',
    isActive: true
  });
};

// Static method to get random questions
questionSchema.statics.getRandomQuestions = async function(criteria = {}, count = 10) {
  const { difficulty, state, category, excludeIds = [] } = criteria;

  const query = {
    status: 'published',
    isActive: true,
    _id: { $nin: excludeIds }
  };

  if (difficulty) query.difficulty = difficulty;
  if (state) query['stateInfo.relatedState'] = state;
  if (category) query['stateInfo.category'] = category;

  return this.aggregate([
    { $match: query },
    { $sample: { size: count } }
  ]);
};

// Method to validate answer
questionSchema.methods.validateAnswer = function(userAnswer) {
  if (this.questionType === 'mcq' || this.questionType === 'true-false') {
    const correctOption = this.options.find(opt => opt.isCorrect);
    return correctOption && correctOption.text === userAnswer;
  }

  if (Array.isArray(this.correctAnswers)) {
    return this.correctAnswers.some(ans => 
      JSON.stringify(ans) === JSON.stringify(userAnswer)
    );
  }

  return false;
};

// Method to increment analytics
questionSchema.methods.updateAnalytics = async function(isCorrect, timeTaken) {
  this.analytics.totalAttempts += 1;
  
  if (isCorrect) {
    this.analytics.correctAttempts += 1;
  }

  // Update average time
  const totalTime = this.analytics.averageTime * (this.analytics.totalAttempts - 1);
  this.analytics.averageTime = (totalTime + timeTaken) / this.analytics.totalAttempts;

  await this.save();
};

const Question = mongoose.model('Question', questionSchema);

module.exports = Question;
