const Exam = require('../models/Exam');
const Question = require('../models/Question');

class ExamController {
  async createExam(req, res) {
    try {
      const exam = new Exam(req.body);
      await exam.save();
      res.status(201).json({ success: true, data: exam });
    } catch (error) {
      res.status(500).json({ success: false, message: error.message });
    }
  }

  async getExams(req, res) {
    try {
      const exams = await Exam.find({ isPublished: true });
      res.json({ success: true, data: exams });
    } catch (error) {
      res.status(500).json({ success: false, message: error.message });
    }
  }

  async getExamById(req, res) {
    try {
      const exam = await Exam.findById(req.params.id).populate('questions');
      if (!exam) {
        return res.status(404).json({ success: false, message: 'Exam not found' });
      }
      res.json({ success: true, data: exam });
    } catch (error) {
      res.status(500).json({ success: false, message: error.message });
    }
  }

  async startExam(req, res) {
    try {
      const exam = await Exam.findById(req.params.id);
      // Create exam session logic
      res.json({ success: true, message: 'Exam started', data: exam });
    } catch (error) {
      res.status(500).json({ success: false, message: error.message });
    }
  }

  async submitExam(req, res) {
    try {
      // Calculate score and save result
      res.json({ success: true, message: 'Exam submitted' });
    } catch (error) {
      res.status(500).json({ success: false, message: error.message });
    }
  }
}

module.exports = new ExamController();
