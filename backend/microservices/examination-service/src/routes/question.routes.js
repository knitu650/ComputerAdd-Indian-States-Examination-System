const express = require('express');
const router = express.Router();
const {
    createQuestion,
    getQuestionsByState,
    updateQuestion,
    deleteQuestion,
} = require('../controllers/question.controller');

// Placeholder for auth middleware
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
    .post(protect, isAdmin, createQuestion);

router.route('/state/:stateName')
    .get(getQuestionsByState);

router.route('/:id')
    .put(protect, isAdmin, updateQuestion)
    .delete(protect, isAdmin, deleteQuestion);

module.exports = router;