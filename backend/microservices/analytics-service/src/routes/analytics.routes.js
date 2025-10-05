const express = require('express');
const router = express.Router();

// @desc    Get overall performance analytics
// @route   GET /api/performance
// @access  Private (Admin)
router.get('/performance', (req, res) => {
    // Placeholder data
    const analytics = {
        totalExams: 150,
        totalStudents: 2500,
        averageScore: 72.5,
        passRate: 0.85,
    };
    res.json(analytics);
});

// @desc    Get state-wise performance breakdown
// @route   GET /api/states/:stateName
// @access  Private (Admin)
router.get('/states/:stateName', (req, res) => {
    const { stateName } = req.params;
    // Placeholder data
    const stateAnalytics = {
        state: stateName,
        averageScore: Math.random() * 30 + 50, // Random score between 50-80
        totalParticipants: Math.floor(Math.random() * 500) + 100,
    };
    res.json(stateAnalytics);
});

module.exports = router;