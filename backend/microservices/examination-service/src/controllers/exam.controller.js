const Exam = require('../models/Exam');

// @desc    Create a new exam
// @route   POST /exams
// @access  Private (Admin)
const createExam = async (req, res) => {
    try {
        // Assuming req.user.id is populated by auth middleware
        const createdBy = req.user.id;
        const exam = await Exam.create({ ...req.body, createdBy });
        res.status(201).json(exam);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Get all exams
// @route   GET /exams
// @access  Public
const getExams = async (req, res) => {
    try {
        const exams = await Exam.find({ isActive: true }).populate('questions');
        res.json(exams);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Get a single exam by ID
// @route   GET /exams/:id
// @access  Public
const getExamById = async (req, res) => {
    try {
        const exam = await Exam.findById(req.params.id).populate('questions');
        if (!exam) {
            return res.status(404).json({ message: 'Exam not found' });
        }
        res.json(exam);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Update an exam
// @route   PUT /exams/:id
// @access  Private (Admin)
const updateExam = async (req, res) => {
    try {
        const exam = await Exam.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!exam) {
            return res.status(404).json({ message: 'Exam not found' });
        }
        res.json(exam);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Delete an exam
// @route   DELETE /exams/:id
// @access  Private (Admin)
const deleteExam = async (req, res) => {
    try {
        const exam = await Exam.findByIdAndDelete(req.params.id);
        if (!exam) {
            return res.status(404).json({ message: 'Exam not found' });
        }
        res.json({ message: 'Exam removed' });
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

module.exports = {
    createExam,
    getExams,
    getExamById,
    updateExam,
    deleteExam,
};