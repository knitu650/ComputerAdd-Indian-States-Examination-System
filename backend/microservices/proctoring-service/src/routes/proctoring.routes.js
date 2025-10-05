const express = require('express');
const router = express.Router();

// @desc    Get proctoring status for an exam
// @route   GET /api/status/:examId
// @access  Private (Admin/Proctor)
router.get('/status/:examId', (req, res) => {
    // In a real app, you'd fetch this from a database or cache
    const status = {
        examId: req.params.examId,
        activeStudents: Math.floor(Math.random() * 50),
        alerts: Math.floor(Math.random() * 5),
    };
    res.json(status);
});

// @desc    Log a manual violation
// @route   POST /api/violation
// @access  Private (Admin/Proctor)
router.post('/violation', (req, res) => {
    const { examId, userId, violationType, description } = req.body;
    console.log(`Violation logged: ${violationType} for user ${userId} in exam ${examId}`);
    // Here you would save the violation to the database
    res.status(201).json({ message: 'Violation logged successfully' });
});

module.exports = router;