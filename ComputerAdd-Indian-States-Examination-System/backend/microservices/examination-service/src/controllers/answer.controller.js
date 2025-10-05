const Answer = require('../models/Answer');
const Question = require('../models/Question');

exports.submitAnswer = async (req, res) => {
  try {
    const { examId, questionId } = req.params;
    const { answer, timeTaken } = req.body;
    const { userId } = req.user;
    
    // Check if answer already exists
    let answerDoc = await Answer.findOne({
      userId,
      examId,
      questionId
    });
    
    if (answerDoc) {
      // Update existing answer
      answerDoc.answer = answer;
      answerDoc.timeTaken = timeTaken;
      answerDoc.attemptNumber += 1;
    } else {
      // Create new answer
      answerDoc = new Answer({
        userId,
        examId,
        questionId,
        answer,
        timeTaken,
        attemptNumber: 1
      });
    }
    
    await answerDoc.save();
    
    res.json({
      success: true,
      message: 'Answer submitted successfully',
      data: answerDoc
    });
    
  } catch (error) {
    console.error('Submit answer error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to submit answer'
    });
  }
};

exports.getAnswer = async (req, res) => {
  try {
    const { examId, questionId } = req.params;
    const { userId } = req.user;
    
    const answer = await Answer.findOne({
      userId,
      examId,
      questionId
    });
    
    res.json({
      success: true,
      data: answer
    });
    
  } catch (error) {
    console.error('Get answer error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to get answer'
    });
  }
};

exports.getAllAnswers = async (req, res) => {
  try {
    const { examId } = req.params;
    const { userId } = req.user;
    
    const answers = await Answer.find({
      userId,
      examId
    }).populate('questionId');
    
    res.json({
      success: true,
      data: answers
    });
    
  } catch (error) {
    console.error('Get answers error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to get answers'
    });
  }
};
