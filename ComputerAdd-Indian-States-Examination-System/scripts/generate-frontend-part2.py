#!/usr/bin/env python3
"""Frontend Generator Part 2 - More Components and Pages"""

import os
import json

BASE_DIR = "/workspace/ComputerAdd-Indian-States-Examination-System"

def create_file(filepath, content):
    full_path = os.path.join(BASE_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {filepath}")

FRONTEND_PART2 = {
    # QUESTION TYPES
    
    "frontend/web-app/src/components/examination/QuestionTypes/TrueFalseQuestion/TrueFalseQuestion.jsx": '''import React from 'react';
import styles from './TrueFalseQuestion.module.css';

const TrueFalseQuestion = ({ question, answer, onAnswer }) => {
  return (
    <div className={styles.container}>
      <h3 className={styles.question}>{question.text}</h3>
      
      {question.image && (
        <img src={question.image} alt="Question" className={styles.image} />
      )}
      
      <div className={styles.options}>
        <button
          className={`${styles.option} ${answer === 'true' ? styles.selected : ''}`}
          onClick={() => onAnswer('true')}
        >
          <span className={styles.icon}>✓</span>
          True
        </button>
        
        <button
          className={`${styles.option} ${answer === 'false' ? styles.selected : ''}`}
          onClick={() => onAnswer('false')}
        >
          <span className={styles.icon}>✗</span>
          False
        </button>
      </div>
    </div>
  );
};

export default TrueFalseQuestion;
''',

    "frontend/web-app/src/components/examination/QuestionTypes/TrueFalseQuestion/TrueFalseQuestion.module.css": '''
.container {
  padding: 1.5rem;
}

.question {
  font-size: 1.25rem;
  color: #1f2937;
  margin: 0 0 1.5rem;
  line-height: 1.6;
}

.image {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin-bottom: 1.5rem;
}

.options {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.option {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  padding: 1.5rem;
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 1.125rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.option:hover {
  border-color: #3b82f6;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2);
}

.option.selected {
  background: #3b82f6;
  border-color: #3b82f6;
  color: white;
}

.icon {
  font-size: 1.5rem;
  font-weight: 700;
}

@media (max-width: 640px) {
  .options {
    grid-template-columns: 1fr;
  }
}
''',

    "frontend/web-app/src/components/examination/QuestionTypes/ImageBasedQuestion/ImageBasedQuestion.jsx": '''import React, { useState } from 'react';
import { FaSearchPlus, FaSearchMinus } from 'react-icons/fa';
import styles from './ImageBasedQuestion.module.css';

const ImageBasedQuestion = ({ question, answer, onAnswer }) => {
  const [zoom, setZoom] = useState(1);
  const [lightbox, setLightbox] = useState(false);

  return (
    <div className={styles.container}>
      <h3 className={styles.question}>{question.text}</h3>
      
      <div className={styles.imageContainer}>
        <img 
          src={question.image} 
          alt="Question" 
          className={styles.image}
          style={{ transform: `scale(${zoom})` }}
          onClick={() => setLightbox(true)}
        />
        
        <div className={styles.zoomControls}>
          <button 
            onClick={() => setZoom(Math.min(zoom + 0.25, 2))}
            className={styles.zoomBtn}
          >
            <FaSearchPlus />
          </button>
          <button 
            onClick={() => setZoom(Math.max(zoom - 0.25, 0.5))}
            className={styles.zoomBtn}
          >
            <FaSearchMinus />
          </button>
        </div>
      </div>

      <div className={styles.options}>
        {question.options.map((option, index) => (
          <button
            key={index}
            className={`${styles.option} ${answer === option ? styles.selected : ''}`}
            onClick={() => onAnswer(option)}
          >
            <span className={styles.optionLabel}>{String.fromCharCode(65 + index)}.</span>
            {option}
          </button>
        ))}
      </div>

      {lightbox && (
        <div className={styles.lightbox} onClick={() => setLightbox(false)}>
          <img src={question.image} alt="Enlarged" className={styles.lightboxImage} />
        </div>
      )}
    </div>
  );
};

export default ImageBasedQuestion;
''',

    "frontend/web-app/src/components/examination/QuestionTypes/ImageBasedQuestion/ImageBasedQuestion.module.css": '''
.container {
  padding: 1.5rem;
}

.question {
  font-size: 1.25rem;
  color: #1f2937;
  margin: 0 0 1.5rem;
}

.imageContainer {
  position: relative;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  overflow: hidden;
  margin-bottom: 1.5rem;
  cursor: zoom-in;
}

.image {
  width: 100%;
  height: auto;
  transition: transform 0.3s;
}

.zoomControls {
  position: absolute;
  top: 1rem;
  right: 1rem;
  display: flex;
  gap: 0.5rem;
}

.zoomBtn {
  background: rgba(255, 255, 255, 0.9);
  border: none;
  border-radius: 8px;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s;
}

.zoomBtn:hover {
  background: white;
  transform: scale(1.1);
}

.options {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.option {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.5rem;
  background: white;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  text-align: left;
  cursor: pointer;
  transition: all 0.3s;
}

.option:hover {
  border-color: #3b82f6;
  transform: translateX(4px);
}

.option.selected {
  background: #dbeafe;
  border-color: #3b82f6;
}

.optionLabel {
  font-weight: 700;
  color: #3b82f6;
  min-width: 30px;
}

.lightbox {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  cursor: zoom-out;
  animation: fadeIn 0.3s;
}

.lightboxImage {
  max-width: 90%;
  max-height: 90%;
  object-fit: contain;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
''',

    # RESULTS COMPONENTS
    
    "frontend/web-app/src/components/examination/Results/ScoreCard/ScoreCard.jsx": '''import React from 'react';
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import styles from './ScoreCard.module.css';

const ScoreCard = ({ result }) => {
  const percentage = result.percentage || 0;
  const grade = result.grade || 'N/A';
  
  const getColor = (percentage) => {
    if (percentage >= 90) return '#10b981';
    if (percentage >= 75) return '#3b82f6';
    if (percentage >= 60) return '#f59e0b';
    return '#ef4444';
  };

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h2 className={styles.title}>Exam Result</h2>
        <span className={`${styles.badge} ${styles[grade.toLowerCase().replace('+', 'plus')]}`}>
          Grade {grade}
        </span>
      </div>

      <div className={styles.content}>
        <div className={styles.scoreCircle}>
          <CircularProgressbar
            value={percentage}
            text={`${percentage.toFixed(1)}%`}
            styles={buildStyles({
              textSize: '1.5rem',
              pathColor: getColor(percentage),
              textColor: getColor(percentage),
              trailColor: '#e5e7eb',
              pathTransitionDuration: 1.5,
            })}
          />
        </div>

        <div className={styles.stats}>
          <div className={styles.statItem}>
            <span className={styles.statLabel}>Total Marks</span>
            <span className={styles.statValue}>{result.totalMarks}</span>
          </div>
          
          <div className={styles.statItem}>
            <span className={styles.statLabel}>Marks Obtained</span>
            <span className={styles.statValue}>{result.obtainedMarks}</span>
          </div>
          
          <div className={styles.statItem}>
            <span className={styles.statLabel}>Correct Answers</span>
            <span className={styles.statValue}>
              {result.questionResults?.filter(q => q.isCorrect).length || 0}
            </span>
          </div>
          
          <div className={styles.statItem}>
            <span className={styles.statLabel}>Wrong Answers</span>
            <span className={styles.statValue}>
              {result.questionResults?.filter(q => !q.isCorrect).length || 0}
            </span>
          </div>
        </div>
      </div>

      <div className={styles.footer}>
        <div className={styles.message}>
          {percentage >= 90 && '🎉 Outstanding Performance!'}
          {percentage >= 75 && percentage < 90 && '👏 Great Job!'}
          {percentage >= 60 && percentage < 75 && '✓ Good Effort!'}
          {percentage < 60 && '💪 Keep Practicing!'}
        </div>
      </div>
    </div>
  );
};

export default ScoreCard;
''',

    "frontend/web-app/src/components/examination/Results/ScoreCard/ScoreCard.module.css": '''
.container {
  background: white;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  animation: slideUp 0.5s ease-out;
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.title {
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0;
}

.badge {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-weight: 600;
  font-size: 0.875rem;
  background: rgba(255, 255, 255, 0.2);
}

.content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 2rem;
  padding: 2rem;
}

.scoreCircle {
  width: 200px;
  height: 200px;
  margin: 0 auto;
  animation: scaleIn 0.8s ease-out;
}

.stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.statItem {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: 1rem;
  background: #f8fafc;
  border-radius: 12px;
}

.statLabel {
  font-size: 0.875rem;
  color: #64748b;
  font-weight: 600;
}

.statValue {
  font-size: 2rem;
  font-weight: 700;
  color: #1e293b;
}

.footer {
  padding: 1.5rem;
  background: #f8fafc;
  text-align: center;
}

.message {
  font-size: 1.125rem;
  font-weight: 600;
  color: #475569;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes scaleIn {
  from {
    transform: scale(0);
  }
  to {
    transform: scale(1);
  }
}

@media (max-width: 768px) {
  .content {
    grid-template-columns: 1fr;
  }
  
  .scoreCircle {
    width: 150px;
    height: 150px;
  }
}
''',

    # UI COMPONENTS
    
    "frontend/web-app/src/components/ui/Button/Button.jsx": '''import React from 'react';
import styles from './Button.module.css';

const Button = ({ 
  children, 
  variant = 'primary', 
  size = 'medium',
  fullWidth = false,
  loading = false,
  disabled = false,
  icon,
  ...props 
}) => {
  const className = [
    styles.button,
    styles[variant],
    styles[size],
    fullWidth ? styles.fullWidth : '',
    loading ? styles.loading : '',
  ].filter(Boolean).join(' ');

  return (
    <button 
      className={className} 
      disabled={disabled || loading}
      {...props}
    >
      {loading && <span className={styles.spinner} />}
      {!loading && icon && <span className={styles.icon}>{icon}</span>}
      <span>{children}</span>
    </button>
  );
};

export default Button;
''',

    "frontend/web-app/src/components/ui/Button/Button.module.css": '''
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
}

.button::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(255, 255, 255, 0.2);
  transform: translateX(-100%);
  transition: transform 0.3s;
}

.button:hover::before {
  transform: translateX(0);
}

.primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.primary:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
}

.secondary {
  background: white;
  color: #667eea;
  border: 2px solid #667eea;
}

.secondary:hover:not(:disabled) {
  background: #667eea;
  color: white;
}

.danger {
  background: #ef4444;
  color: white;
}

.danger:hover:not(:disabled) {
  background: #dc2626;
  transform: translateY(-2px);
}

.success {
  background: #10b981;
  color: white;
}

.success:hover:not(:disabled) {
  background: #059669;
}

.small {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
}

.medium {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
}

.large {
  padding: 1rem 2rem;
  font-size: 1.125rem;
}

.fullWidth {
  width: 100%;
}

.loading {
  pointer-events: none;
  opacity: 0.7;
}

.spinner {
  width: 1rem;
  height: 1rem;
  border: 2px solid currentColor;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

.button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
''',

    "frontend/web-app/src/components/ui/Card/Card.jsx": '''import React from 'react';
import styles from './Card.module.css';

const Card = ({ 
  children, 
  title, 
  subtitle,
  footer,
  hoverable = false,
  className = '' 
}) => {
  return (
    <div className={`${styles.card} ${hoverable ? styles.hoverable : ''} ${className}`}>
      {(title || subtitle) && (
        <div className={styles.header}>
          {title && <h3 className={styles.title}>{title}</h3>}
          {subtitle && <p className={styles.subtitle}>{subtitle}</p>}
        </div>
      )}
      
      <div className={styles.content}>
        {children}
      </div>
      
      {footer && (
        <div className={styles.footer}>
          {footer}
        </div>
      )}
    </div>
  );
};

export default Card;
''',

    "frontend/web-app/src/components/ui/Card/Card.module.css": '''
.card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  overflow: hidden;
  transition: all 0.3s;
}

.card.hoverable:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.header {
  padding: 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.title {
  margin: 0 0 0.5rem;
  font-size: 1.25rem;
  font-weight: 700;
  color: #1f2937;
}

.subtitle {
  margin: 0;
  font-size: 0.875rem;
  color: #6b7280;
}

.content {
  padding: 1.5rem;
}

.footer {
  padding: 1rem 1.5rem;
  background: #f9fafb;
  border-top: 1px solid #e5e7eb;
}
''',

    # ADDITIONAL HOOKS
    
    "frontend/web-app/src/hooks/useProctoring.js": '''import { useState, useEffect, useCallback } from 'react';
import { useWebSocket } from './useWebSocket';

export const useProctoring = (examId) => {
  const [violations, setViolations] = useState([]);
  const [isMonitoring, setIsMonitoring] = useState(false);
  const socket = useWebSocket(`/proctoring/${examId}`);

  useEffect(() => {
    if (socket) {
      socket.on('violation-detected', (violation) => {
        setViolations(prev => [...prev, violation]);
      });

      socket.on('monitoring-status', (status) => {
        setIsMonitoring(status.active);
      });
    }

    return () => {
      if (socket) {
        socket.off('violation-detected');
        socket.off('monitoring-status');
      }
    };
  }, [socket]);

  const sendFrame = useCallback((frameBlob) => {
    if (socket && isMonitoring) {
      const reader = new FileReader();
      reader.onloadend = () => {
        socket.emit('video-frame', {
          examId,
          frame: reader.result,
          timestamp: Date.now()
        });
      };
      reader.readAsDataURL(frameBlob);
    }
  }, [socket, examId, isMonitoring]);

  const startMonitoring = useCallback(() => {
    if (socket) {
      socket.emit('start-proctoring', { examId });
      setIsMonitoring(true);
    }
  }, [socket, examId]);

  const stopMonitoring = useCallback(() => {
    if (socket) {
      socket.emit('stop-proctoring', { examId });
      setIsMonitoring(false);
    }
  }, [socket, examId]);

  return {
    violations,
    isMonitoring,
    sendFrame,
    startMonitoring,
    stopMonitoring
  };
};
''',

    "frontend/web-app/src/hooks/useWebRTC.js": '''import { useState, useEffect, useRef } from 'react';

export const useWebRTC = (config = {}) => {
  const [stream, setStream] = useState(null);
  const [error, setError] = useState(null);
  const [isActive, setIsActive] = useState(false);
  const peerConnectionRef = useRef(null);

  const startCamera = async (constraints = { video: true, audio: false }) => {
    try {
      const mediaStream = await navigator.mediaDevices.getUserMedia(constraints);
      setStream(mediaStream);
      setIsActive(true);
      setError(null);
      return mediaStream;
    } catch (err) {
      setError(err.message);
      console.error('Camera error:', err);
      return null;
    }
  };

  const stopCamera = () => {
    if (stream) {
      stream.getTracks().forEach(track => track.stop());
      setStream(null);
      setIsActive(false);
    }
  };

  const createPeerConnection = (configuration) => {
    const pc = new RTCPeerConnection(configuration || {
      iceServers: [
        { urls: 'stun:stun.l.google.com:19302' },
        { urls: 'stun:stun1.l.google.com:19302' },
      ]
    });

    peerConnectionRef.current = pc;
    return pc;
  };

  const addStreamToPeerConnection = (mediaStream) => {
    if (peerConnectionRef.current && mediaStream) {
      mediaStream.getTracks().forEach(track => {
        peerConnectionRef.current.addTrack(track, mediaStream);
      });
    }
  };

  useEffect(() => {
    return () => {
      stopCamera();
      if (peerConnectionRef.current) {
        peerConnectionRef.current.close();
      }
    };
  }, []);

  return {
    stream,
    error,
    isActive,
    startCamera,
    stopCamera,
    createPeerConnection,
    addStreamToPeerConnection,
    peerConnection: peerConnectionRef.current
  };
};
''',

    "frontend/web-app/src/hooks/useNotification.js": '''import { useState, useCallback } from 'react';

export const useNotification = () => {
  const [notifications, setNotifications] = useState([]);

  const showNotification = useCallback(({ type, message, duration = 5000 }) => {
    const id = Date.now();
    const notification = { id, type, message, duration };
    
    setNotifications(prev => [...prev, notification]);

    if (duration > 0) {
      setTimeout(() => {
        removeNotification(id);
      }, duration);
    }

    return id;
  }, []);

  const removeNotification = useCallback((id) => {
    setNotifications(prev => prev.filter(n => n.id !== id));
  }, []);

  const success = useCallback((message, duration) => {
    return showNotification({ type: 'success', message, duration });
  }, [showNotification]);

  const error = useCallback((message, duration) => {
    return showNotification({ type: 'error', message, duration });
  }, [showNotification]);

  const info = useCallback((message, duration) => {
    return showNotification({ type: 'info', message, duration });
  }, [showNotification]);

  const warning = useCallback((message, duration) => {
    return showNotification({ type: 'warning', message, duration });
  }, [showNotification]);

  return {
    notifications,
    showNotification,
    removeNotification,
    success,
    error,
    info,
    warning
  };
};
''',
}

print(f"🚀 Generating {len(FRONTEND_PART2)} more frontend files...")
for filepath, content in FRONTEND_PART2.items():
    create_file(filepath, content)

print(f"\n✅ Successfully created {len(FRONTEND_PART2)} files!")
print("\n📦 Created:")
print("  ✅ Question Types (TrueFalse, ImageBased)")
print("  ✅ Results Components (ScoreCard)")
print("  ✅ UI Components (Button, Card)")
print("  ✅ Additional Hooks (useProctoring, useWebRTC, useNotification)")
