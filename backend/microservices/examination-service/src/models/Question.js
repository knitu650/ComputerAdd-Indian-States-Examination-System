const mongoose = require('mongoose');

const OptionSchema = new mongoose.Schema({
    text: {
        type: String,
        required: true,
    },
    isCorrect: {
        type: Boolean,
        required: true,
        default: false,
    },
});

const QuestionSchema = new mongoose.Schema({
    questionText: {
        type: String,
        required: true,
    },
    questionType: {
        type: String,
        enum: ['MCQ', 'TrueFalse', 'ImageBased', 'DragDrop'],
        required: true,
    },
    options: [OptionSchema],
    state: {
        type: String, // e.g., 'Andhra Pradesh', 'Assam'
        required: true,
    },
    difficulty: {
        type: String,
        enum: ['Easy', 'Medium', 'Hard'],
        default: 'Medium',
    },
    topic: {
        type: String, // e.g., 'History', 'Geography', 'Culture'
    },
    imageUrl: {
        type: String, // For ImageBased questions
    },
    createdBy: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User',
        required: true,
    },
    createdAt: {
        type: Date,
        default: Date.now,
    },
});

module.exports = mongoose.model('Question', QuestionSchema);