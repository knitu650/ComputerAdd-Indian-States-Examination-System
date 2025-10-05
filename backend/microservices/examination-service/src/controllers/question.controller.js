const Question = require('../models/Question');
const Exam = require('../models/Exam');

// @desc    Create a new question
// @route   POST /questions
// @access  Private (Admin)
const createQuestion = async (req, res) => {
    try {
        // Assuming req.user.id is populated by auth middleware
        const createdBy = req.user.id;
        const question = await Question.create({ ...req.body, createdBy });
        res.status(201).json(question);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Add a question to an exam
// @route   POST /exams/:examId/questions
// @access  Private (Admin)
const addQuestionToExam = async (req, res) => {
    try {
        const { questionId } = req.body;
        const exam = await Exam.findById(req.params.examId);

        if (!exam) {
            return res.status(404).json({ message: 'Exam not found' });
        }

        exam.questions.push(questionId);
        await exam.save();
        res.json(exam);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Get all questions for a specific state
// @route   GET /questions/state/:stateName
// @access  Public
const getQuestionsByState = async (req, res) => {
    try {
        const questions = await Question.find({ state: req.params.stateName });
        res.json(questions);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Update a question
// @route   PUT /questions/:id
// @access  Private (Admin)
const updateQuestion = async (req, res) => {
    try {
        const question = await Question.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!question) {
            return res.status(404).json({ message: 'Question not found' });
        }
        res.json(question);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// @desc    Delete a question
// @route   DELETE /questions/:id
// @access  Private (Admin)
const deleteQuestion = async (req, res) => {
    try {
        const question = await Question.findByIdAndDelete(req.params.id);
        if (!question) {
            return res.status(404).json({ message: 'Question not found' });
        }
        res.json({ message: 'Question removed' });
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

module.exports = {
    createQuestion,
    addQuestionToExam,
    getQuestionsByState,
    updateQuestion,
    deleteQuestion,
};