const examService = require('../services/exam.service');

module.exports = async (req, res, next) => {
  try {
    const { examId } = req.params;
    const { userId } = req.user;
    
    // Check if exam session exists and is valid
    const session = await examService.getExamSession(examId, userId);
    
    if (!session) {
      return res.status(403).json({
        success: false,
        message: 'No active exam session found. Please start the exam first.'
      });
    }
    
    // Check if session expired
    if (new Date() > new Date(session.endTime)) {
      return res.status(403).json({
        success: false,
        message: 'Exam time has expired'
      });
    }
    
    // Attach session to request
    req.examSession = session;
    
    next();
    
  } catch (error) {
    console.error('Exam session middleware error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to validate exam session'
    });
  }
};
