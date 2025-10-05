const Result = require('../models/Result');
const Answer = require('../models/Answer');
const Exam = require('../models/Exam');
const Question = require('../models/Question');

exports.calculateResult = async (req, res) => {
  try {
    const { examId } = req.params;
    const { userId } = req.user;
    
    // Get all answers
    const answers = await Answer.find({ userId, examId }).populate('questionId');
    
    // Get exam details
    const exam = await Exam.findById(examId);
    
    if (!exam) {
      return res.status(404).json({
        success: false,
        message: 'Exam not found'
      });
    }
    
    // Calculate score
    let totalMarks = 0;
    let obtainedMarks = 0;
    const questionResults = [];
    
    for (const answer of answers) {
      const question = answer.questionId;
      totalMarks += question.marks;
      
      const isCorrect = this.checkAnswer(answer.answer, question.correctAnswer);
      const marksObtained = isCorrect ? question.marks : 0;
      
      obtainedMarks += marksObtained;
      
      questionResults.push({
        questionId: question._id,
        isCorrect,
        marksObtained,
        timeTaken: answer.timeTaken
      });
    }
    
    const percentage = (obtainedMarks / totalMarks) * 100;
    
    // Create or update result
    let result = await Result.findOne({ userId, examId });
    
    if (result) {
      result.totalMarks = totalMarks;
      result.obtainedMarks = obtainedMarks;
      result.percentage = percentage;
      result.questionResults = questionResults;
      result.status = 'completed';
    } else {
      result = new Result({
        userId,
        examId,
        totalMarks,
        obtainedMarks,
        percentage,
        questionResults,
        status: 'completed'
      });
    }
    
    await result.save();
    
    res.json({
      success: true,
      message: 'Result calculated successfully',
      data: result
    });
    
  } catch (error) {
    console.error('Calculate result error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to calculate result'
    });
  }
};

exports.getResult = async (req, res) => {
  try {
    const { examId } = req.params;
    const { userId } = req.user;
    
    const result = await Result.findOne({ userId, examId })
      .populate('examId')
      .populate('userId', 'email profile.firstName profile.lastName');
    
    if (!result) {
      return res.status(404).json({
        success: false,
        message: 'Result not found'
      });
    }
    
    res.json({
      success: true,
      data: result
    });
    
  } catch (error) {
    console.error('Get result error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to get result'
    });
  }
};

exports.getAllResults = async (req, res) => {
  try {
    const { userId } = req.user;
    
    const results = await Result.find({ userId })
      .populate('examId')
      .sort({ createdAt: -1 });
    
    res.json({
      success: true,
      data: results
    });
    
  } catch (error) {
    console.error('Get results error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to get results'
    });
  }
};

exports.checkAnswer = function(studentAnswer, correctAnswer) {
  if (!studentAnswer || !correctAnswer) return false;
  
  // Normalize and compare
  const normalize = (str) => str.toLowerCase().trim();
  
  return normalize(studentAnswer) === normalize(correctAnswer);
};
