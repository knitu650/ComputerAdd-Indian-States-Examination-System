#!/usr/bin/env python3
"""
Complete Backend Generator - Part 1
Generates all remaining backend microservices files
"""

import os

BASE_DIR = "/workspace/ComputerAdd-Indian-States-Examination-System"

def create_file(filepath, content):
    full_path = os.path.join(BASE_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {filepath}")

BACKEND_PART1 = {
    # USER SERVICE - MISSING FILES
    
    "backend/microservices/user-service/src/controllers/verification.controller.js": '''const User = require('../models/User');
const crypto = require('crypto');
const emailService = require('../services/notification.service');

/**
 * Email Verification Controller
 */
exports.sendVerificationEmail = async (req, res) => {
  try {
    const { email } = req.body;
    
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(404).json({
        success: false,
        message: 'User not found'
      });
    }
    
    if (user.emailVerified) {
      return res.status(400).json({
        success: false,
        message: 'Email already verified'
      });
    }
    
    // Generate verification token
    const verificationToken = crypto.randomBytes(32).toString('hex');
    user.emailVerificationToken = verificationToken;
    user.emailVerificationExpires = Date.now() + 24 * 60 * 60 * 1000; // 24 hours
    
    await user.save();
    
    // Send email
    await emailService.sendVerificationEmail(email, verificationToken);
    
    res.json({
      success: true,
      message: 'Verification email sent'
    });
    
  } catch (error) {
    console.error('Send verification error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to send verification email'
    });
  }
};

exports.verifyEmail = async (req, res) => {
  try {
    const { token } = req.params;
    
    const user = await User.findOne({
      emailVerificationToken: token,
      emailVerificationExpires: { $gt: Date.now() }
    });
    
    if (!user) {
      return res.status(400).json({
        success: false,
        message: 'Invalid or expired verification token'
      });
    }
    
    user.emailVerified = true;
    user.emailVerificationToken = undefined;
    user.emailVerificationExpires = undefined;
    
    await user.save();
    
    res.json({
      success: true,
      message: 'Email verified successfully'
    });
    
  } catch (error) {
    console.error('Email verification error:', error);
    res.status(500).json({
      success: false,
      message: 'Email verification failed'
    });
  }
};

exports.sendPhoneOTP = async (req, res) => {
  try {
    const { userId } = req.user;
    const { phoneNumber } = req.body;
    
    const user = await User.findById(userId);
    if (!user) {
      return res.status(404).json({
        success: false,
        message: 'User not found'
      });
    }
    
    // Generate 6-digit OTP
    const otp = Math.floor(100000 + Math.random() * 900000).toString();
    
    user.phoneOTP = otp;
    user.phoneOTPExpires = Date.now() + 10 * 60 * 1000; // 10 minutes
    user.profile.phoneNumber = phoneNumber;
    
    await user.save();
    
    // Send SMS (placeholder)
    console.log(`OTP for ${phoneNumber}: ${otp}`);
    
    res.json({
      success: true,
      message: 'OTP sent to phone'
    });
    
  } catch (error) {
    console.error('Send OTP error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to send OTP'
    });
  }
};

exports.verifyPhone = async (req, res) => {
  try {
    const { userId } = req.user;
    const { otp } = req.body;
    
    const user = await User.findOne({
      _id: userId,
      phoneOTP: otp,
      phoneOTPExpires: { $gt: Date.now() }
    });
    
    if (!user) {
      return res.status(400).json({
        success: false,
        message: 'Invalid or expired OTP'
      });
    }
    
    user.phoneVerified = true;
    user.phoneOTP = undefined;
    user.phoneOTPExpires = undefined;
    
    await user.save();
    
    res.json({
      success: true,
      message: 'Phone verified successfully'
    });
    
  } catch (error) {
    console.error('Phone verification error:', error);
    res.status(500).json({
      success: false,
      message: 'Phone verification failed'
    });
  }
};
''',

    "backend/microservices/user-service/src/models/Profile.js": '''const mongoose = require('mongoose');

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
''',

    "backend/microservices/user-service/src/models/Verification.js": '''const mongoose = require('mongoose');

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
''',

    "backend/microservices/user-service/src/routes/verification.routes.js": '''const express = require('express');
const router = express.Router();
const verificationController = require('../controllers/verification.controller');
const authMiddleware = require('../middleware/auth.middleware');

// Send verification email
router.post('/email/send', verificationController.sendVerificationEmail);

// Verify email with token
router.get('/email/verify/:token', verificationController.verifyEmail);

// Send phone OTP (protected)
router.post('/phone/send', authMiddleware, verificationController.sendPhoneOTP);

// Verify phone OTP (protected)
router.post('/phone/verify', authMiddleware, verificationController.verifyPhone);

module.exports = router;
''',

    # EXAMINATION SERVICE - MISSING FILES
    
    "backend/microservices/examination-service/src/controllers/answer.controller.js": '''const Answer = require('../models/Answer');
const Question = require('../models/Question');

exports.submitAnswer = async (req, res) => {
  try {
    const { examId, questionId } = req.params;
    const { answer, timeTaken } = req.body;
    const { userId } = req.user;
    
    // Check if answer already exists
    let answerDoc = await Answer.findOne({
      userId,
      examId,
      questionId
    });
    
    if (answerDoc) {
      // Update existing answer
      answerDoc.answer = answer;
      answerDoc.timeTaken = timeTaken;
      answerDoc.attemptNumber += 1;
    } else {
      // Create new answer
      answerDoc = new Answer({
        userId,
        examId,
        questionId,
        answer,
        timeTaken,
        attemptNumber: 1
      });
    }
    
    await answerDoc.save();
    
    res.json({
      success: true,
      message: 'Answer submitted successfully',
      data: answerDoc
    });
    
  } catch (error) {
    console.error('Submit answer error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to submit answer'
    });
  }
};

exports.getAnswer = async (req, res) => {
  try {
    const { examId, questionId } = req.params;
    const { userId } = req.user;
    
    const answer = await Answer.findOne({
      userId,
      examId,
      questionId
    });
    
    res.json({
      success: true,
      data: answer
    });
    
  } catch (error) {
    console.error('Get answer error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to get answer'
    });
  }
};

exports.getAllAnswers = async (req, res) => {
  try {
    const { examId } = req.params;
    const { userId } = req.user;
    
    const answers = await Answer.find({
      userId,
      examId
    }).populate('questionId');
    
    res.json({
      success: true,
      data: answers
    });
    
  } catch (error) {
    console.error('Get answers error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to get answers'
    });
  }
};
''',

    "backend/microservices/examination-service/src/controllers/result.controller.js": '''const Result = require('../models/Result');
const Answer = require('../models/Answer');
const Exam = require('../models/Exam');
const Question = require('../models/Question');

exports.calculateResult = async (req, res) => {
  try {
    const { examId } = req.params;
    const { userId } = req.user;
    
    // Get all answers
    const answers = await Answer.find({ userId, examId }).populate('questionId');
    
    // Get exam details
    const exam = await Exam.findById(examId);
    
    if (!exam) {
      return res.status(404).json({
        success: false,
        message: 'Exam not found'
      });
    }
    
    // Calculate score
    let totalMarks = 0;
    let obtainedMarks = 0;
    const questionResults = [];
    
    for (const answer of answers) {
      const question = answer.questionId;
      totalMarks += question.marks;
      
      const isCorrect = this.checkAnswer(answer.answer, question.correctAnswer);
      const marksObtained = isCorrect ? question.marks : 0;
      
      obtainedMarks += marksObtained;
      
      questionResults.push({
        questionId: question._id,
        isCorrect,
        marksObtained,
        timeTaken: answer.timeTaken
      });
    }
    
    const percentage = (obtainedMarks / totalMarks) * 100;
    
    // Create or update result
    let result = await Result.findOne({ userId, examId });
    
    if (result) {
      result.totalMarks = totalMarks;
      result.obtainedMarks = obtainedMarks;
      result.percentage = percentage;
      result.questionResults = questionResults;
      result.status = 'completed';
    } else {
      result = new Result({
        userId,
        examId,
        totalMarks,
        obtainedMarks,
        percentage,
        questionResults,
        status: 'completed'
      });
    }
    
    await result.save();
    
    res.json({
      success: true,
      message: 'Result calculated successfully',
      data: result
    });
    
  } catch (error) {
    console.error('Calculate result error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to calculate result'
    });
  }
};

exports.getResult = async (req, res) => {
  try {
    const { examId } = req.params;
    const { userId } = req.user;
    
    const result = await Result.findOne({ userId, examId })
      .populate('examId')
      .populate('userId', 'email profile.firstName profile.lastName');
    
    if (!result) {
      return res.status(404).json({
        success: false,
        message: 'Result not found'
      });
    }
    
    res.json({
      success: true,
      data: result
    });
    
  } catch (error) {
    console.error('Get result error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to get result'
    });
  }
};

exports.getAllResults = async (req, res) => {
  try {
    const { userId } = req.user;
    
    const results = await Result.find({ userId })
      .populate('examId')
      .sort({ createdAt: -1 });
    
    res.json({
      success: true,
      data: results
    });
    
  } catch (error) {
    console.error('Get results error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to get results'
    });
  }
};

exports.checkAnswer = function(studentAnswer, correctAnswer) {
  if (!studentAnswer || !correctAnswer) return false;
  
  // Normalize and compare
  const normalize = (str) => str.toLowerCase().trim();
  
  return normalize(studentAnswer) === normalize(correctAnswer);
};
''',

    "backend/microservices/examination-service/src/models/Answer.js": '''const mongoose = require('mongoose');

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
''',

    "backend/microservices/examination-service/src/models/Result.js": '''const mongoose = require('mongoose');

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
''',

    "backend/microservices/examination-service/src/models/IndianStates.js": '''const mongoose = require('mongoose');

const indianStateSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    unique: true
  },
  
  code: {
    type: String,
    required: true,
    unique: true
  },
  
  type: {
    type: String,
    enum: ['state', 'union_territory'],
    required: true
  },
  
  capital: {
    type: String,
    required: true
  },
  
  largestCity: String,
  
  formation: {
    date: Date,
    description: String
  },
  
  geography: {
    area: Number, // in km²
    borders: [String],
    coastline: Number,
    highestPoint: String,
    majorRivers: [String],
    climate: String,
    coordinates: {
      latitude: Number,
      longitude: Number
    }
  },
  
  demographics: {
    population: Number,
    density: Number,
    sexRatio: Number,
    literacyRate: Number,
    urbanPopulation: Number,
    ruralPopulation: Number
  },
  
  language: {
    official: [String],
    spoken: [String]
  },
  
  government: {
    governor: String,
    chiefMinister: String,
    legislature: String,
    parliamentarySeats: Number,
    assemblySeats: Number
  },
  
  economy: {
    gdp: Number,
    gdpPerCapita: Number,
    majorIndustries: [String],
    agriculture: [String],
    exports: [String]
  },
  
  culture: {
    festivals: [String],
    dances: [String],
    cuisine: [String],
    crafts: [String],
    monuments: [String]
  },
  
  history: {
    ancientHistory: String,
    medievalHistory: String,
    modernHistory: String,
    importantEvents: [{
      event: String,
      year: Number,
      description: String
    }]
  },
  
  tourism: {
    popularDestinations: [String],
    unesco WorldHeritageSites: [String],
    touristArrivals: Number
  },
  
  education: {
    universities: Number,
    literacyRate: Number,
    majorInstitutions: [String]
  },
  
  images: {
    flag: String,
    map: String,
    emblem: String,
    photos: [String]
  },
  
  metadata: {
    lastUpdated: {
      type: Date,
      default: Date.now
    },
    dataSource: String
  }
  
}, { timestamps: true });

// Indexes
indianStateSchema.index({ name: 1 });
indianStateSchema.index({ code: 1 });
indianStateSchema.index({ type: 1 });

module.exports = mongoose.model('IndianState', indianStateSchema);
''',

    "backend/microservices/examination-service/src/services/exam.service.js": '''const Exam = require('../models/Exam');
const Question = require('../models/Question');
const Answer = require('../models/Answer');

class ExamService {
  
  async createExam(examData) {
    try {
      const exam = new Exam(examData);
      await exam.save();
      return exam;
    } catch (error) {
      throw error;
    }
  }
  
  async getExamById(examId) {
    try {
      const exam = await Exam.findById(examId)
        .populate('questions')
        .populate('createdBy', 'email profile.firstName profile.lastName');
      return exam;
    } catch (error) {
      throw error;
    }
  }
  
  async getActiveExams(filters = {}) {
    try {
      const query = { isActive: true };
      
      if (filters.difficulty) {
        query['settings.difficulty'] = filters.difficulty;
      }
      
      if (filters.category) {
        query.category = filters.category;
      }
      
      const exams = await Exam.find(query)
        .select('-questions')
        .sort({ createdAt: -1 });
      
      return exams;
    } catch (error) {
      throw error;
    }
  }
  
  async startExam(examId, userId) {
    try {
      const exam = await Exam.findById(examId);
      
      if (!exam) {
        throw new Error('Exam not found');
      }
      
      if (!exam.isActive) {
        throw new Error('Exam is not active');
      }
      
      // Check if already started
      const existingSession = await this.getExamSession(examId, userId);
      
      if (existingSession) {
        return existingSession;
      }
      
      // Create exam session
      const session = {
        userId,
        examId,
        startTime: new Date(),
        endTime: new Date(Date.now() + exam.duration * 60 * 1000),
        status: 'in_progress'
      };
      
      // Store session (you'd typically use Redis)
      // await redisClient.setex(`exam:session:${userId}:${examId}`, 
      //   exam.duration * 60, JSON.stringify(session));
      
      return session;
    } catch (error) {
      throw error;
    }
  }
  
  async getExamQuestions(examId, userId) {
    try {
      const exam = await Exam.findById(examId);
      
      if (!exam) {
        throw new Error('Exam not found');
      }
      
      // Get questions
      const questions = await Question.find({
        _id: { $in: exam.questions }
      }).select('-correctAnswer'); // Don't send correct answer
      
      // Shuffle questions if random order enabled
      if (exam.settings.randomizeQuestions) {
        questions.sort(() => Math.random() - 0.5);
      }
      
      return questions;
    } catch (error) {
      throw error;
    }
  }
  
  async submitExam(examId, userId) {
    try {
      // Get all answers
      const answers = await Answer.find({ userId, examId });
      
      // Calculate result
      const result = await this.calculateResult(examId, userId);
      
      // Mark session as completed
      // await redisClient.del(`exam:session:${userId}:${examId}`);
      
      return result;
    } catch (error) {
      throw error;
    }
  }
  
  async calculateResult(examId, userId) {
    // Implementation moved to result.controller.js
    return {};
  }
  
  async getExamSession(examId, userId) {
    // Get session from Redis
    // const session = await redisClient.get(`exam:session:${userId}:${examId}`);
    // return session ? JSON.parse(session) : null;
    return null;
  }
}

module.exports = new ExamService();
''',

    "backend/microservices/examination-service/src/services/question-bank.service.js": '''const Question = require('../models/Question');

class QuestionBankService {
  
  async createQuestion(questionData) {
    try {
      const question = new Question(questionData);
      await question.save();
      return question;
    } catch (error) {
      throw error;
    }
  }
  
  async bulkImportQuestions(questions) {
    try {
      const result = await Question.insertMany(questions);
      return {
        total: questions.length,
        inserted: result.length
      };
    } catch (error) {
      throw error;
    }
  }
  
  async getQuestionsByState(state) {
    try {
      const questions = await Question.find({
        'indianStatesContent.states': state
      });
      return questions;
    } catch (error) {
      throw error;
    }
  }
  
  async getQuestionsByDifficulty(difficulty) {
    try {
      const questions = await Question.find({ difficulty });
      return questions;
    } catch (error) {
      throw error;
    }
  }
  
  async searchQuestions(filters) {
    try {
      const query = {};
      
      if (filters.type) query.type = filters.type;
      if (filters.difficulty) query.difficulty = filters.difficulty;
      if (filters.category) query.category = filters.category;
      if (filters.tags) query.tags = { $in: filters.tags };
      
      if (filters.search) {
        query.$text = { $search: filters.search };
      }
      
      const questions = await Question.find(query)
        .limit(filters.limit || 50)
        .skip(filters.skip || 0);
      
      const total = await Question.countDocuments(query);
      
      return {
        questions,
        total,
        page: Math.floor((filters.skip || 0) / (filters.limit || 50)) + 1,
        totalPages: Math.ceil(total / (filters.limit || 50))
      };
    } catch (error) {
      throw error;
    }
  }
  
  async updateQuestion(questionId, updates) {
    try {
      const question = await Question.findByIdAndUpdate(
        questionId,
        updates,
        { new: true, runValidators: true }
      );
      return question;
    } catch (error) {
      throw error;
    }
  }
  
  async deleteQuestion(questionId) {
    try {
      await Question.findByIdAndDelete(questionId);
      return true;
    } catch (error) {
      throw error;
    }
  }
  
  async getRandomQuestions(filters, count) {
    try {
      const query = {};
      
      if (filters.difficulty) query.difficulty = filters.difficulty;
      if (filters.category) query.category = filters.category;
      if (filters.states) {
        query['indianStatesContent.states'] = { $in: filters.states };
      }
      
      const questions = await Question.aggregate([
        { $match: query },
        { $sample: { size: count } }
      ]);
      
      return questions;
    } catch (error) {
      throw error;
    }
  }
}

module.exports = new QuestionBankService();
''',

    "backend/microservices/examination-service/src/middleware/exam-session.middleware.js": '''const examService = require('../services/exam.service');

module.exports = async (req, res, next) => {
  try {
    const { examId } = req.params;
    const { userId } = req.user;
    
    // Check if exam session exists and is valid
    const session = await examService.getExamSession(examId, userId);
    
    if (!session) {
      return res.status(403).json({
        success: false,
        message: 'No active exam session found. Please start the exam first.'
      });
    }
    
    // Check if session expired
    if (new Date() > new Date(session.endTime)) {
      return res.status(403).json({
        success: false,
        message: 'Exam time has expired'
      });
    }
    
    // Attach session to request
    req.examSession = session;
    
    next();
    
  } catch (error) {
    console.error('Exam session middleware error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to validate exam session'
    });
  }
};
''',

    "backend/microservices/examination-service/src/routes/exam.routes.js": '''const express = require('express');
const router = express.Router();
const examController = require('../controllers/exam.controller');
const answerController = require('../controllers/answer.controller');
const resultController = require('../controllers/result.controller');
const authMiddleware = require('../middleware/auth.middleware');
const examSessionMiddleware = require('../middleware/exam-session.middleware');

// Public routes
router.get('/active', examController.getActiveExams);
router.get('/:examId', examController.getExamById);

// Protected routes
router.use(authMiddleware);

// Exam management (admin only)
router.post('/', examController.createExam);
router.put('/:examId', examController.updateExam);
router.delete('/:examId', examController.deleteExam);

// Student exam routes
router.post('/:examId/start', examController.startExam);
router.get('/:examId/questions', examSessionMiddleware, examController.getExamQuestions);

// Answer submission
router.post('/:examId/questions/:questionId/answer', 
  examSessionMiddleware, 
  answerController.submitAnswer
);
router.get('/:examId/questions/:questionId/answer', 
  answerController.getAnswer
);
router.get('/:examId/answers', answerController.getAllAnswers);

// Exam submission
router.post('/:examId/submit', examSessionMiddleware, examController.submitExam);

// Results
router.get('/:examId/result', resultController.getResult);
router.get('/results/all', resultController.getAllResults);

module.exports = router;
''',
}

print(f"🚀 Generating {len(BACKEND_PART1)} backend files (Part 1)...")
for filepath, content in BACKEND_PART1.items():
    create_file(filepath, content)

print(f"\n✅ Successfully created {len(BACKEND_PART1)} files!")
print("\n📊 Created:")
print("  ✅ User Service - Verification controller, models, routes")
print("  ✅ Examination Service - Answer/Result controllers & models")
print("  ✅ Examination Service - Services & middleware")
print("  ✅ Examination Service - Routes")
print("\n📦 Next: Generating remaining services...")
