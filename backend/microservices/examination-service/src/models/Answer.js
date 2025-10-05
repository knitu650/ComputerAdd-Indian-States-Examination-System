const mongoose = require('mongoose');

const AnswerSchema = new mongoose.Schema({
    exam: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Exam',
        required: true,
    },
    question: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Question',
        required: true,
    },
    user: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User',
        required: true,
    },
    selectedOption: {
        type: mongoose.Schema.Types.ObjectId, // Refers to the _id of the option in the Question model
    },
    isCorrect: {
        type: Boolean,
    },
    answeredAt: {
        type: Date,
        default: Date.now,
    },
});

module.exports = mongoose.model('Answer', AnswerSchema);