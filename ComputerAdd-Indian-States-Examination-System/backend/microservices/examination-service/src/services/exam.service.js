const Exam = require('../models/Exam');
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
