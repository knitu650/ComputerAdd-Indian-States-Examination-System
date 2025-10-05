const express = require('express');
const router = express.Router();
const {
    createExam,
    getExams,
    getExamById,
    updateExam,
    deleteExam,
} = require('../controllers/exam.controller');
const { addQuestionToExam } = require('../controllers/question.controller');

// A placeholder for auth middleware
const protect = (req, res, next) => {
    req.user = { id: 'some-admin-id', role: 'admin' }; // Simulate admin user
    next();
};

const isAdmin = (req, res, next) => {
    if (req.user && req.user.role === 'admin') {
        next();
    } else {
        res.status(403).json({ message: 'Not authorized as an admin' });
    }
};

router.route('/')
    .post(protect, isAdmin, createExam)
    .get(getExams);

router.route('/:id')
    .get(getExamById)
    .put(protect, isAdmin, updateExam)
    .delete(protect, isAdmin, deleteExam);

router.route('/:examId/questions')
    .post(protect, isAdmin, addQuestionToExam);

module.exports = router;