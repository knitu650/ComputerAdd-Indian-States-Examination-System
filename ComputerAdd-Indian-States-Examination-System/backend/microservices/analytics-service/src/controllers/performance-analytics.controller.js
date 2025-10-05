const Result = require('../models/Result');

exports.getUserPerformance = async (req, res) => {
  try {
    const { userId } = req.params;
    
    const results = await Result.find({ userId }).sort({ createdAt: -1 });
    
    if (!results.length) {
      return res.json({
        success: true,
        data: {
          totalExams: 0,
          averageScore: 0,
          trend: 'N/A'
        }
      });
    }
    
    const totalExams = results.length;
    const averageScore = results.reduce((sum, r) => sum + r.percentage, 0) / totalExams;
    
    // Calculate trend
    const recentScores = results.slice(0, 5).map(r => r.percentage);
    const trend = this.calculateTrend(recentScores);
    
    // Topic-wise performance
    const topicPerformance = this.calculateTopicPerformance(results);
    
    // Difficulty-wise performance
    const difficultyPerformance = this.calculateDifficultyPerformance(results);
    
    res.json({
      success: true,
      data: {
        totalExams,
        averageScore: averageScore.toFixed(2),
        trend,
        topicPerformance,
        difficultyPerformance,
        recentResults: results.slice(0, 10)
      }
    });
    
  } catch (error) {
    console.error('Get performance error:', error);
    res.status(500).json({
      success: false,
      message: 'Failed to get performance analytics'
    });
  }
};

exports.calculateTrend = function(scores) {
  if (scores.length < 2) return 'stable';
  
  const firstHalf = scores.slice(0, Math.floor(scores.length / 2));
  const secondHalf = scores.slice(Math.floor(scores.length / 2));
  
  const avgFirst = firstHalf.reduce((a, b) => a + b, 0) / firstHalf.length;
  const avgSecond = secondHalf.reduce((a, b) => a + b, 0) / secondHalf.length;
  
  if (avgSecond > avgFirst + 5) return 'improving';
  if (avgSecond < avgFirst - 5) return 'declining';
  return 'stable';
};

exports.calculateTopicPerformance = function(results) {
  const topicScores = {};
  
  results.forEach(result => {
    if (result.topicWiseAnalysis) {
      result.topicWiseAnalysis.forEach(topic => {
        if (!topicScores[topic.topic]) {
          topicScores[topic.topic] = {
            total: 0,
            correct: 0
          };
        }
        topicScores[topic.topic].total += topic.totalQuestions;
        topicScores[topic.topic].correct += topic.correctAnswers;
      });
    }
  });
  
  return Object.entries(topicScores).map(([topic, data]) => ({
    topic,
    percentage: (data.correct / data.total * 100).toFixed(2)
  }));
};

exports.calculateDifficultyPerformance = function(results) {
  const difficulties = { easy: { total: 0, correct: 0 }, 
                        medium: { total: 0, correct: 0 }, 
                        hard: { total: 0, correct: 0 } };
  
  results.forEach(result => {
    if (result.difficultyAnalysis) {
      ['easy', 'medium', 'hard'].forEach(level => {
        if (result.difficultyAnalysis[level]) {
          difficulties[level].total += result.difficultyAnalysis[level].attempted;
          difficulties[level].correct += result.difficultyAnalysis[level].correct;
        }
      });
    }
  });
  
  return difficulties;
};
