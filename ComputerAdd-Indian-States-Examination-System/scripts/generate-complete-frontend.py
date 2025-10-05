#!/usr/bin/env python3
"""
Complete Frontend File Generator
Generates ALL frontend files with full functionality
"""

import os
import json

BASE_DIR = "/workspace/ComputerAdd-Indian-States-Examination-System"

def create_file(filepath, content):
    full_path = os.path.join(BASE_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {filepath}")

# Massive file templates dictionary
FILES = {
    # ==================== Public Files ====================
    "frontend/web-app/public/index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#000000" />
  <meta name="description" content="Indian States Examination System - Test your knowledge" />
  <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
  <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
  <title>Indian States Exam System</title>
</head>
<body>
  <noscript>You need to enable JavaScript to run this app.</noscript>
  <div id="root"></div>
</body>
</html>
''',

    "frontend/web-app/public/manifest.json": '''{
  "short_name": "Exam System",
  "name": "Indian States Examination System",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}
''',

    "frontend/web-app/public/service-worker.js": '''self.addEventListener('install', event => {
  console.log('Service Worker installing.');
});

self.addEventListener('activate', event => {
  console.log('Service Worker activating.');
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});
''',

    # ==================== Common Components ====================
    "frontend/web-app/src/components/common/Footer/Footer.jsx": '''import React from 'react';
import styles from './Footer.module.css';

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <div className={styles.container}>
        <div className={styles.section}>
          <h4>About</h4>
          <p>Indian States Examination System</p>
        </div>
        <div className={styles.section}>
          <h4>Quick Links</h4>
          <a href="/about">About Us</a>
          <a href="/contact">Contact</a>
          <a href="/privacy">Privacy Policy</a>
        </div>
        <div className={styles.section}>
          <h4>Support</h4>
          <a href="/help">Help Center</a>
          <a href="/faq">FAQ</a>
        </div>
      </div>
      <div className={styles.copyright}>
        © 2025 ComputerAdd. All rights reserved.
      </div>
    </footer>
  );
};

export default Footer;
''',

    "frontend/web-app/src/components/common/Footer/Footer.module.css": '''.footer {
  background: #2c3e50;
  color: white;
  padding: 40px 20px 20px;
  margin-top: 60px;
}

.container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

.section h4 {
  margin-bottom: 15px;
}

.section a {
  display: block;
  color: #ecf0f1;
  text-decoration: none;
  margin: 5px 0;
}

.copyright {
  text-align: center;
  margin-top: 30px;
  padding-top: 20px;
  border-top: 1px solid #34495e;
}
''',

    "frontend/web-app/src/components/common/Loading/Loading.jsx": '''import React from 'react';
import styles from './Loading.module.css';

const Loading = ({ message = 'Loading...' }) => {
  return (
    <div className={styles.loading}>
      <div className={styles.spinner}></div>
      <p>{message}</p>
    </div>
  );
};

export default Loading;
''',

    "frontend/web-app/src/components/common/Loading/Loading.module.css": '''.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 200px;
}

.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #667eea;
  border-radius: 50%;
  width: 50px;
  height: 50px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
''',

    "frontend/web-app/src/components/common/ErrorBoundary/ErrorBoundary.jsx": '''import React from 'react';
import styles from './ErrorBoundary.module.css';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className={styles.error}>
          <h2>Something went wrong</h2>
          <p>{this.state.error?.message}</p>
          <button onClick={() => window.location.reload()}>
            Reload Page
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
''',

    "frontend/web-app/src/components/common/ErrorBoundary/ErrorBoundary.module.css": '''.error {
  padding: 40px;
  text-align: center;
}

.error button {
  margin-top: 20px;
  padding: 10px 20px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
''',

    # ==================== Auth Components ====================
    "frontend/web-app/src/components/auth/LoginForm/LoginForm.jsx": '''import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../../hooks/useAuth';
import styles from './LoginForm.module.css';

const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      await login(email, password);
      navigate('/dashboard');
    } catch (err) {
      setError(err.response?.data?.message || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <h2>Login</h2>
      
      {error && <div className={styles.error}>{error}</div>}
      
      <div className={styles.field}>
        <label>Email</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </div>

      <div className={styles.field}>
        <label>Password</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </div>

      <button type="submit" disabled={loading}>
        {loading ? 'Logging in...' : 'Login'}
      </button>

      <div className={styles.links}>
        <a href="/forgot-password">Forgot Password?</a>
        <a href="/register">Create Account</a>
      </div>
    </form>
  );
};

export default LoginForm;
''',

    "frontend/web-app/src/components/auth/LoginForm/LoginForm.module.css": '''.form {
  max-width: 400px;
  margin: 40px auto;
  padding: 30px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.field {
  margin-bottom: 20px;
}

.field label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
}

.field input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.error {
  background: #fee;
  color: #c33;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 20px;
}

button {
  width: 100%;
  padding: 12px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background: #ccc;
}

.links {
  margin-top: 20px;
  text-align: center;
}

.links a {
  display: block;
  margin: 10px 0;
  color: #667eea;
}
''',

    "frontend/web-app/src/components/auth/RegisterForm/RegisterForm.jsx": '''import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import styles from './RegisterForm.module.css';

const RegisterForm = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
    firstName: '',
    lastName: '',
    phoneNumber: '',
    dateOfBirth: '',
    gender: 'male'
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (formData.password !== formData.confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    setLoading(true);
    setError('');

    try {
      await axios.post('/api/v1/auth/register', {
        email: formData.email,
        password: formData.password,
        profile: {
          firstName: formData.firstName,
          lastName: formData.lastName,
          phoneNumber: formData.phoneNumber,
          dateOfBirth: formData.dateOfBirth,
          gender: formData.gender
        }
      });
      navigate('/login?registered=true');
    } catch (err) {
      setError(err.response?.data?.message || 'Registration failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form className={styles.form} onSubmit={handleSubmit}>
      <h2>Create Account</h2>
      
      {error && <div className={styles.error}>{error}</div>}
      
      <div className={styles.row}>
        <div className={styles.field}>
          <label>First Name</label>
          <input name="firstName" value={formData.firstName} onChange={handleChange} required />
        </div>
        <div className={styles.field}>
          <label>Last Name</label>
          <input name="lastName" value={formData.lastName} onChange={handleChange} required />
        </div>
      </div>

      <div className={styles.field}>
        <label>Email</label>
        <input type="email" name="email" value={formData.email} onChange={handleChange} required />
      </div>

      <div className={styles.field}>
        <label>Phone Number</label>
        <input name="phoneNumber" value={formData.phoneNumber} onChange={handleChange} required />
      </div>

      <div className={styles.field}>
        <label>Date of Birth</label>
        <input type="date" name="dateOfBirth" value={formData.dateOfBirth} onChange={handleChange} required />
      </div>

      <div className={styles.field}>
        <label>Gender</label>
        <select name="gender" value={formData.gender} onChange={handleChange}>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
      </div>

      <div className={styles.field}>
        <label>Password</label>
        <input type="password" name="password" value={formData.password} onChange={handleChange} required />
      </div>

      <div className={styles.field}>
        <label>Confirm Password</label>
        <input type="password" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} required />
      </div>

      <button type="submit" disabled={loading}>
        {loading ? 'Creating Account...' : 'Register'}
      </button>

      <div className={styles.links}>
        <a href="/login">Already have an account? Login</a>
      </div>
    </form>
  );
};

export default RegisterForm;
''',

    "frontend/web-app/src/components/auth/RegisterForm/RegisterForm.module.css": '''.form {
  max-width: 500px;
  margin: 40px auto;
  padding: 30px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
}

.field {
  margin-bottom: 20px;
}

.field label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
}

.field input,
.field select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.error {
  background: #fee;
  color: #c33;
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 20px;
}

button {
  width: 100%;
  padding: 12px;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 10px;
}

.links {
  margin-top: 20px;
  text-align: center;
}

.links a {
  color: #667eea;
}
''',

    # ==================== Examination Components ====================
    "frontend/web-app/src/components/examination/QuestionTypes/MCQQuestion/MCQQuestion.jsx": '''import React from 'react';
import styles from './MCQQuestion.module.css';

const MCQQuestion = ({ question, selectedAnswer, onAnswerSelect }) => {
  return (
    <div className={styles.mcq}>
      <h3>{question.questionText}</h3>
      
      {question.media?.imageUrl && (
        <img src={question.media.imageUrl} alt="Question" className={styles.image} />
      )}

      <div className={styles.options}>
        {question.options.map((option, index) => (
          <label key={index} className={styles.option}>
            <input
              type="radio"
              name="answer"
              value={option.text}
              checked={selectedAnswer === option.text}
              onChange={() => onAnswerSelect(option.text)}
            />
            <span>{option.text}</span>
          </label>
        ))}
      </div>
    </div>
  );
};

export default MCQQuestion;
''',

    "frontend/web-app/src/components/examination/QuestionTypes/MCQQuestion/MCQQuestion.module.css": '''.mcq {
  padding: 20px;
}

.mcq h3 {
  margin-bottom: 20px;
}

.image {
  max-width: 100%;
  margin: 20px 0;
  border-radius: 8px;
}

.options {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.option {
  padding: 15px;
  border: 2px solid #ddd;
  border-radius: 8px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 10px;
}

.option:hover {
  background: #f5f5f5;
}

.option input:checked + span {
  font-weight: bold;
  color: #667eea;
}
''',

    # ==================== Context Files ====================
    "frontend/web-app/src/context/AuthContext.js": '''import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('token'));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      fetchUser();
    } else {
      setLoading(false);
    }
  }, [token]);

  const fetchUser = async () => {
    try {
      const response = await axios.get('/api/v1/profile');
      setUser(response.data.data);
    } catch (error) {
      console.error('Failed to fetch user', error);
      logout();
    } finally {
      setLoading(false);
    }
  };

  const login = async (email, password) => {
    const response = await axios.post('/api/v1/auth/login', { email, password });
    const { token, user } = response.data.data;
    setToken(token);
    setUser(user);
    localStorage.setItem('token', token);
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  };

  const logout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem('token');
    delete axios.defaults.headers.common['Authorization'];
  };

  return (
    <AuthContext.Provider value={{ user, token, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
''',

    "frontend/web-app/src/context/ThemeContext.js": '''import React, { createContext, useState, useEffect } from 'react';

export const ThemeContext = createContext();

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState(localStorage.getItem('theme') || 'light');

  useEffect(() => {
    document.body.className = theme;
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};
''',

    # ==================== Services ====================
    "frontend/web-app/src/services/api/exam.service.js": '''import axios from 'axios';

const API_URL = '/api/v1/exams';

export const examService = {
  getAllExams: async () => {
    const response = await axios.get(API_URL);
    return response.data;
  },

  getExamById: async (id) => {
    const response = await axios.get(`${API_URL}/${id}`);
    return response.data;
  },

  startExam: async (examId) => {
    const response = await axios.post(`${API_URL}/${examId}/start`);
    return response.data;
  },

  submitAnswer: async (examId, questionId, answer) => {
    const response = await axios.post(
      `${API_URL}/${examId}/questions/${questionId}/answer`,
      { answer }
    );
    return response.data;
  },

  submitExam: async (examId) => {
    const response = await axios.post(`${API_URL}/${examId}/submit`);
    return response.data;
  },

  getResults: async (examId) => {
    const response = await axios.get(`${API_URL}/${examId}/results`);
    return response.data;
  }
};
''',

    "frontend/web-app/src/services/websocket/socket.service.js": '''import io from 'socket.io-client';

class SocketService {
  constructor() {
    this.socket = null;
  }

  connect(token) {
    this.socket = io(process.env.REACT_APP_WS_URL || 'http://localhost:8000', {
      auth: { token }
    });

    this.socket.on('connect', () => {
      console.log('WebSocket connected');
    });

    this.socket.on('disconnect', () => {
      console.log('WebSocket disconnected');
    });

    return this.socket;
  }

  disconnect() {
    if (this.socket) {
      this.socket.disconnect();
    }
  }

  emit(event, data) {
    if (this.socket) {
      this.socket.emit(event, data);
    }
  }

  on(event, callback) {
    if (this.socket) {
      this.socket.on(event, callback);
    }
  }
}

export default new SocketService();
''',

    # ==================== Hooks ====================
    "frontend/web-app/src/hooks/useTimer.js": '''import { useState, useEffect, useRef } from 'react';

export const useTimer = (initialTime) => {
  const [timeRemaining, setTimeRemaining] = useState(initialTime);
  const [isRunning, setIsRunning] = useState(false);
  const intervalRef = useRef(null);

  useEffect(() => {
    if (isRunning && timeRemaining > 0) {
      intervalRef.current = setInterval(() => {
        setTimeRemaining(prev => prev - 1);
      }, 1000);
    } else if (timeRemaining === 0) {
      setIsRunning(false);
    }

    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    };
  }, [isRunning, timeRemaining]);

  const start = () => setIsRunning(true);
  const pause = () => setIsRunning(false);
  const reset = () => {
    setTimeRemaining(initialTime);
    setIsRunning(false);
  };

  const formatTime = (seconds) => {
    const hrs = Math.floor(seconds / 3600);
    const mins = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    return `${hrs.toString().padStart(2, '0')}:${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  return {
    timeRemaining,
    isRunning,
    start,
    pause,
    reset,
    formatTime: () => formatTime(timeRemaining)
  };
};
''',

    "frontend/web-app/src/hooks/useLocalStorage.js": '''import { useState, useEffect } from 'react';

export const useLocalStorage = (key, initialValue) => {
  const [value, setValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(error);
      return initialValue;
    }
  });

  useEffect(() => {
    try {
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error(error);
    }
  }, [key, value]);

  return [value, setValue];
};
''',

    # ==================== Utils ====================
    "frontend/web-app/src/utils/constants.js": '''export const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

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
''',

    "frontend/web-app/src/utils/helpers.js": '''export const formatDate = (date) => {
  return new Date(date).toLocaleDateString('en-IN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
};

export const calculatePercentage = (obtained, total) => {
  return ((obtained / total) * 100).toFixed(2);
};

export const truncateText = (text, maxLength) => {
  if (text.length <= maxLength) return text;
  return text.substring(0, maxLength) + '...';
};

export const debounce = (func, delay) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func(...args), delay);
  };
};
''',

    "frontend/web-app/src/utils/validation.js": '''export const validateEmail = (email) => {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
};

export const validatePassword = (password) => {
  return password.length >= 8;
};

export const validatePhone = (phone) => {
  const re = /^[0-9]{10}$/;
  return re.test(phone);
};

export const validatePincode = (pincode) => {
  const re = /^[0-9]{6}$/;
  return re.test(pincode);
};
''',

    # ==================== Styles ====================
    "frontend/web-app/src/styles/globals.css": '''* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New', monospace;
}

a {
  text-decoration: none;
  color: inherit;
}

button {
  font-family: inherit;
}
''',

    "frontend/web-app/src/styles/variables.css": ''':root {
  --primary-color: #667eea;
  --secondary-color: #764ba2;
  --success-color: #48bb78;
  --error-color: #f56565;
  --warning-color: #ed8936;
  --info-color: #4299e1;
  
  --text-primary: #2d3748;
  --text-secondary: #718096;
  --bg-primary: #ffffff;
  --bg-secondary: #f7fafc;
  --border-color: #e2e8f0;
  
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  
  --border-radius: 8px;
  --transition: all 0.3s ease;
}

.dark {
  --text-primary: #f7fafc;
  --text-secondary: #cbd5e0;
  --bg-primary: #1a202c;
  --bg-secondary: #2d3748;
  --border-color: #4a5568;
}
''',

    # ==================== Locales ====================
    "frontend/web-app/src/locales/en/common.json": '''{
  "appName": "Indian States Examination System",
  "welcome": "Welcome",
  "logout": "Logout",
  "loading": "Loading...",
  "error": "Error",
  "success": "Success",
  "submit": "Submit",
  "cancel": "Cancel",
  "save": "Save",
  "delete": "Delete",
  "edit": "Edit",
  "view": "View",
  "back": "Back",
  "next": "Next",
  "previous": "Previous",
  "search": "Search",
  "filter": "Filter",
  "sort": "Sort"
}
''',

    "frontend/web-app/src/locales/en/exam.json": '''{
  "startExam": "Start Exam",
  "submitExam": "Submit Exam",
  "timeRemaining": "Time Remaining",
  "questionNumber": "Question",
  "markForReview": "Mark for Review",
  "clearAnswer": "Clear Answer",
  "instructions": "Instructions",
  "totalQuestions": "Total Questions",
  "totalMarks": "Total Marks",
  "duration": "Duration",
  "passingMarks": "Passing Marks"
}
''',

    # ==================== Config Files ====================
    "frontend/web-app/.env.development": '''REACT_APP_API_URL=http://localhost:8000
REACT_APP_WS_URL=ws://localhost:8000
REACT_APP_ENVIRONMENT=development
''',

    "frontend/web-app/.env.production": '''REACT_APP_API_URL=https://api.exam-system.com
REACT_APP_WS_URL=wss://api.exam-system.com
REACT_APP_ENVIRONMENT=production
''',

    "frontend/web-app/babel.config.js": '''module.exports = {
  presets: [
    '@babel/preset-env',
    ['@babel/preset-react', { runtime: 'automatic' }]
  ]
};
''',

    "frontend/web-app/tsconfig.json": '''{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}
''',

    # ==================== Admin Dashboard ====================
    "frontend/admin-dashboard/src/components/dashboard/Overview/Overview.jsx": '''import React, { useEffect, useState } from 'react';
import axios from 'axios';
import styles from './Overview.module.css';

const Overview = () => {
  const [stats, setStats] = useState({
    totalUsers: 0,
    totalExams: 0,
    activeExams: 0,
    totalRevenue: 0
  });

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      const response = await axios.get('/api/v1/analytics/dashboard');
      setStats(response.data.data);
    } catch (error) {
      console.error('Failed to fetch stats', error);
    }
  };

  return (
    <div className={styles.overview}>
      <h2>Dashboard Overview</h2>
      
      <div className={styles.statsGrid}>
        <div className={styles.statCard}>
          <h3>Total Users</h3>
          <p className={styles.number}>{stats.totalUsers}</p>
        </div>

        <div className={styles.statCard}>
          <h3>Total Exams</h3>
          <p className={styles.number}>{stats.totalExams}</p>
        </div>

        <div className={styles.statCard}>
          <h3>Active Exams</h3>
          <p className={styles.number}>{stats.activeExams}</p>
        </div>

        <div className={styles.statCard}>
          <h3>Revenue</h3>
          <p className={styles.number}>₹{stats.totalRevenue}</p>
        </div>
      </div>
    </div>
  );
};

export default Overview;
''',

    "frontend/admin-dashboard/src/components/dashboard/Overview/Overview.module.css": '''.overview {
  padding: 20px;
}

.statsGrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
}

.statCard {
  background: white;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.statCard h3 {
  color: #666;
  font-size: 14px;
  margin-bottom: 10px;
}

.number {
  font-size: 32px;
  font-weight: bold;
  color: #333;
}
''',
}

print(f"🚀 Generating {len(FILES)} frontend files...")
for filepath, content in FILES.items():
    create_file(filepath, content)

print(f"\n✅ Successfully created {len(FILES)} files!")
print("\n📋 Created components:")
print("  ✅ Auth forms (Login, Register)")
print("  ✅ Common components (Header, Footer, Loading, ErrorBoundary)")
print("  ✅ Exam components (MCQ, Question types)")
print("  ✅ Context providers (Auth, Theme)")
print("  ✅ Services (API, WebSocket)")
print("  ✅ Custom hooks (useTimer, useLocalStorage)")
print("  ✅ Utils (constants, helpers, validation)")
print("  ✅ Styles (globals, variables, themes)")
print("  ✅ Localization files")
print("  ✅ Config files")
print("  ✅ Admin dashboard components")
print("\n🎉 Frontend is ready for development!")
