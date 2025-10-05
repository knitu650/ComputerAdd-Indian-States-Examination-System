const express = require('express');
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
