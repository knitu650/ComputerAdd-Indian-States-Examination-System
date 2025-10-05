const mongoose = require('mongoose');

const answerSchema = new mongoose.Schema({
  userId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  
  examId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Exam',
    required: true
  },
  
  questionId: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Question',
    required: true
  },
  
  answer: {
    type: mongoose.Schema.Types.Mixed,
    required: true
  },
  
  timeTaken: {
    type: Number, // seconds
    default: 0
  },
  
  attemptNumber: {
    type: Number,
    default: 1
  },
  
  isCorrect: Boolean,
  
  marksObtained: {
    type: Number,
    default: 0
  },
  
  confidence: Number,
  
  metadata: {
    ipAddress: String,
    userAgent: String,
    browserInfo: String,
    deviceInfo: String,
    location: Object
  }
  
}, { timestamps: true });

// Indexes
answerSchema.index({ userId: 1, examId: 1, questionId: 1 }, { unique: true });
answerSchema.index({ examId: 1, userId: 1 });

module.exports = mongoose.model('Answer', answerSchema);
