const mongoose = require('mongoose');

const ResultSchema = new mongoose.Schema({
    exam: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Exam',
        required: true,
    },
    user: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User',
        required: true,
    },
    score: {
        type: Number,
        required: true,
    },
    totalQuestions: {
        type: Number,
        required: true,
    },
    correctAnswers: {
        type: Number,
        required: true,
    },
    incorrectAnswers: {
        type: Number,
        required: true,
    },
    completionTime: {
        type: Number, // in seconds
    },
    submittedAt: {
        type: Date,
        default: Date.now,
    },
    certificateId: {
        type: String, // From Blockchain service
    }
});

module.exports = mongoose.model('Result', ResultSchema);