const axios = require('axios');

exports.startMonitoring = async (req, res) => {
  try {
    const { examId, userId } = req.body;
    
    // Initialize monitoring session
    const session = {
      examId,
      userId,
      startTime: new Date(),
      violations: [],
      snapshots: []
    };
    
    // Store in Redis or MongoDB
    // await monitoringService.createSession(session);
    
    res.json({
      success: true,
      message: 'Monitoring started',
      data: session
    });
    
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Failed to start monitoring'
    });
  }
};

exports.processFrame = async (req, res) => {
  try {
    const { examId, userId, frameData } = req.body;
    
    // Send frame to AI/ML service for analysis
    const aiResponse = await axios.post('http://ai-ml-service:5000/api/v1/cv/analyze-frame', {
      image: frameData,
      userId
    });
    
    const analysis = aiResponse.data.data;
    
    // Check for violations
    const violations = [];
    
    if (analysis.numFaces > 1) {
      violations.push({
        type: 'multiple_faces',
        severity: 'high',
        timestamp: new Date()
      });
    }
    
    if (analysis.numFaces === 0) {
      violations.push({
        type: 'no_face_detected',
        severity: 'medium',
        timestamp: new Date()
      });
    }
    
    if (analysis.hasUnauthorizedObjects) {
      violations.push({
        type: 'unauthorized_objects',
        severity: 'high',
        timestamp: new Date()
      });
    }
    
    res.json({
      success: true,
      data: {
        analysis,
        violations
      }
    });
    
  } catch (error) {
    console.error('Process frame error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to process frame'
    });
  }
};

exports.getViolations = async (req, res) => {
  try {
    const { examId, userId } = req.params;
    
    // Get violations from database
    // const violations = await monitoringService.getViolations(examId, userId);
    
    res.json({
      success: true,
      data: []
    });
    
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Failed to get violations'
    });
  }
};
