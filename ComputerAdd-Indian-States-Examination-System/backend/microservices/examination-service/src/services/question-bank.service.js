const Question = require('../models/Question');

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
