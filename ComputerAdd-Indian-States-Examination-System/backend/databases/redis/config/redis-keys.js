module.exports = {
  // Session keys
  SESSION: (userId) => `session:${userId}`,
  
  // Exam session keys
  EXAM_SESSION: (userId, examId) => `exam:session:${userId}:${examId}`,
  
  // Cache keys
  USER_CACHE: (userId) => `cache:user:${userId}`,
  EXAM_CACHE: (examId) => `cache:exam:${examId}`,
  QUESTIONS_CACHE: (examId) => `cache:questions:${examId}`,
  
  // Rate limiting keys
  RATE_LIMIT: (ip) => `ratelimit:${ip}`,
  
  // Real-time data
  ACTIVE_EXAMS: 'active:exams',
  ONLINE_USERS: 'online:users',
  
  // Leaderboard
  LEADERBOARD: (examId) => `leaderboard:${examId}`,
  GLOBAL_LEADERBOARD: 'leaderboard:global',
  
  // Proctoring
  PROCTORING_DATA: (userId, examId) => `proctoring:${userId}:${examId}`,
  VIOLATIONS: (userId, examId) => `violations:${userId}:${examId}`
};
