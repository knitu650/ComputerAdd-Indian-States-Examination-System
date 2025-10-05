export const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const ROUTES = {
  HOME: '/',
  LOGIN: '/login',
  REGISTER: '/register',
  DASHBOARD: '/dashboard',
  EXAMS: '/exams',
  PROFILE: '/profile',
  RESULTS: '/results'
};

export const EXAM_STATUS = {
  NOT_STARTED: 'not_started',
  IN_PROGRESS: 'in_progress',
  COMPLETED: 'completed',
  EXPIRED: 'expired'
};

export const QUESTION_TYPES = {
  MCQ: 'mcq',
  TRUE_FALSE: 'true-false',
  IMAGE_BASED: 'image-based',
  AUDIO: 'audio'
};

export const USER_ROLES = {
  STUDENT: 'student',
  EXAMINER: 'examiner',
  ADMIN: 'admin'
};
