const mongoose = require('mongoose');

const resultSchema = new mongoose.Schema({
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
  
  status: {
    type: String,
    enum: ['in_progress', 'completed', 'reviewed', 'published'],
    default: 'in_progress'
  },
  
  startTime: {
    type: Date,
    default: Date.now
  },
  
  endTime: Date,
  
  totalMarks: {
    type: Number,
    required: true
  },
  
  obtainedMarks: {
    type: Number,
    required: true
  },
  
  percentage: {
    type: Number,
    required: true
  },
  
  grade: {
    type: String,
    enum: ['A+', 'A', 'B+', 'B', 'C', 'D', 'F']
  },
  
  rank: Number,
  
  questionResults: [{
    questionId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'Question'
    },
    isCorrect: Boolean,
    marksObtained: Number,
    timeTaken: Number
  }],
  
  topicWiseAnalysis: [{
    topic: String,
    totalQuestions: Number,
    correctAnswers: Number,
    percentage: Number
  }],
  
  stateWiseAnalysis: [{
    state: String,
    totalQuestions: Number,
    correctAnswers: Number,
    percentage: Number
  }],
  
  difficultyAnalysis: {
    easy: { attempted: Number, correct: Number },
    medium: { attempted: Number, correct: Number },
    hard: { attempted: Number, correct: Number }
  },
  
  timeAnalysis: {
    totalTimeTaken: Number,
    averageTimePerQuestion: Number,
    fastestQuestion: Number,
    slowestQuestion: Number
  },
  
  proctoringReport: {
    violations: [{
      type: String,
      severity: String,
      timestamp: Date,
      description: String
    }],
    totalViolations: Number,
    suspicionScore: Number
  },
  
  certificateId: String,
  
  reviewedBy: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  },
  
  reviewedAt: Date,
  
  comments: String
  
}, { timestamps: true });

// Indexes
resultSchema.index({ userId: 1, examId: 1 });
resultSchema.index({ examId: 1, percentage: -1 });
resultSchema.index({ createdAt: -1 });

// Calculate grade based on percentage
resultSchema.methods.calculateGrade = function() {
  if (this.percentage >= 90) return 'A+';
  if (this.percentage >= 80) return 'A';
  if (this.percentage >= 70) return 'B+';
  if (this.percentage >= 60) return 'B';
  if (this.percentage >= 50) return 'C';
  if (this.percentage >= 40) return 'D';
  return 'F';
};

module.exports = mongoose.model('Result', resultSchema);
