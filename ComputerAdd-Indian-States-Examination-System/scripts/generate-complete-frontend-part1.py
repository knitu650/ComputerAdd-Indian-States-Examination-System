#!/usr/bin/env python3
"""
Complete Frontend Generator - Part 1
Generates remaining common components, auth, and examination components
"""

import os

BASE_DIR = "/workspace/ComputerAdd-Indian-States-Examination-System"

def create_file(filepath, content):
    full_path = os.path.join(BASE_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {filepath}")

FRONTEND_PART1 = {
    # COMMON COMPONENTS - MISSING
    
    "frontend/web-app/src/components/common/Sidebar/Sidebar.jsx": '''import React, { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { FaHome, FaBook, FaChartBar, FaUser, FaCog, FaSignOutAlt } from 'react-icons/fa';
import styles from './Sidebar.module.css';

const Sidebar = ({ isOpen, onClose }) => {
  const location = useLocation();
  const [collapsed, setCollapsed] = useState(false);

  const menuItems = [
    { path: '/dashboard', icon: FaHome, label: 'Dashboard' },
    { path: '/exams', icon: FaBook, label: 'Exams' },
    { path: '/states', icon: FaBook, label: 'Indian States' },
    { path: '/analytics', icon: FaChartBar, label: 'Analytics' },
    { path: '/profile', icon: FaUser, label: 'Profile' },
    { path: '/settings', icon: FaCog, label: 'Settings' },
  ];

  return (
    <>
      {isOpen && <div className={styles.overlay} onClick={onClose} />}
      
      <aside className={`${styles.sidebar} ${isOpen ? styles.open : ''} ${collapsed ? styles.collapsed : ''}`}>
        <div className={styles.header}>
          <h2 className={styles.logo}>Exam Portal</h2>
          <button 
            className={styles.collapseBtn}
            onClick={() => setCollapsed(!collapsed)}
          >
            ☰
          </button>
        </div>

        <nav className={styles.nav}>
          {menuItems.map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === item.path;
            
            return (
              <Link
                key={item.path}
                to={item.path}
                className={`${styles.navItem} ${isActive ? styles.active : ''}`}
                onClick={onClose}
              >
                <Icon className={styles.icon} />
                {!collapsed && <span>{item.label}</span>}
              </Link>
            );
          })}
        </nav>

        <button className={styles.logoutBtn}>
          <FaSignOutAlt className={styles.icon} />
          {!collapsed && <span>Logout</span>}
        </button>
      </aside>
    </>
  );
};

export default Sidebar;
''',

    "frontend/web-app/src/components/common/Sidebar/Sidebar.module.css": '''
.sidebar {
  position: fixed;
  left: 0;
  top: 0;
  height: 100vh;
  width: 260px;
  background: linear-gradient(180deg, #1e3a8a 0%, #1e40af 100%);
  color: white;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 1000;
  display: flex;
  flex-direction: column;
  box-shadow: 4px 0 12px rgba(0, 0, 0, 0.1);
}

.sidebar.collapsed {
  width: 80px;
}

.overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 999;
  animation: fadeIn 0.3s;
}

.header {
  padding: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.logo {
  font-size: 1.25rem;
  font-weight: 700;
  margin: 0;
  white-space: nowrap;
}

.collapseBtn {
  background: transparent;
  border: none;
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0.5rem;
  transition: transform 0.3s;
}

.collapseBtn:hover {
  transform: rotate(90deg);
}

.nav {
  flex: 1;
  padding: 1rem 0;
  overflow-y: auto;
}

.navItem {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.5rem;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  transition: all 0.3s;
  position: relative;
}

.navItem::before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  background: white;
  transform: scaleY(0);
  transition: transform 0.3s;
}

.navItem:hover,
.navItem.active {
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.navItem.active::before {
  transform: scaleY(1);
}

.icon {
  font-size: 1.25rem;
  min-width: 1.25rem;
}

.logoutBtn {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.5rem;
  background: rgba(220, 38, 38, 0.2);
  border: none;
  color: white;
  cursor: pointer;
  transition: all 0.3s;
  width: 100%;
  margin-top: auto;
}

.logoutBtn:hover {
  background: rgba(220, 38, 38, 0.3);
}

@media (max-width: 768px) {
  .sidebar {
    transform: translateX(-100%);
  }
  
  .sidebar.open {
    transform: translateX(0);
  }
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
''',

    "frontend/web-app/src/components/common/Layout/Layout.jsx": '''import React, { useState } from 'react';
import Header from '../Header/Header';
import Sidebar from '../Sidebar/Sidebar';
import Footer from '../Footer/Footer';
import styles from './Layout.module.css';

const Layout = ({ children }) => {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  return (
    <div className={styles.layout}>
      <Header onMenuClick={() => setSidebarOpen(true)} />
      <Sidebar isOpen={sidebarOpen} onClose={() => setSidebarOpen(false)} />
      
      <main className={styles.main}>
        <div className={styles.content}>
          {children}
        </div>
      </main>
      
      <Footer />
    </div>
  );
};

export default Layout;
''',

    "frontend/web-app/src/components/common/Layout/Layout.module.css": '''
.layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: #f8fafc;
}

.main {
  flex: 1;
  padding-top: 70px;
  padding-left: 260px;
  transition: padding-left 0.3s;
}

.content {
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  animation: fadeInUp 0.5s;
}

@media (max-width: 768px) {
  .main {
    padding-left: 0;
  }
  
  .content {
    padding: 1rem;
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
''',

    "frontend/web-app/src/components/common/Notification/Notification.jsx": '''import React, { useEffect } from 'react';
import { FaCheckCircle, FaExclamationCircle, FaInfoCircle, FaTimes } from 'react-icons/fa';
import styles from './Notification.module.css';

const Notification = ({ type = 'info', message, onClose, duration = 5000 }) => {
  useEffect(() => {
    if (duration > 0) {
      const timer = setTimeout(onClose, duration);
      return () => clearTimeout(timer);
    }
  }, [duration, onClose]);

  const icons = {
    success: FaCheckCircle,
    error: FaExclamationCircle,
    info: FaInfoCircle,
    warning: FaExclamationCircle,
  };

  const Icon = icons[type];

  return (
    <div className={`${styles.notification} ${styles[type]}`}>
      <Icon className={styles.icon} />
      <p className={styles.message}>{message}</p>
      <button className={styles.closeBtn} onClick={onClose}>
        <FaTimes />
      </button>
    </div>
  );
};

export default Notification;
''',

    "frontend/web-app/src/components/common/Notification/Notification.module.css": '''
.notification {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem 1.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  animation: slideIn 0.3s ease-out;
  min-width: 300px;
  max-width: 500px;
}

.notification.success {
  background: #10b981;
  color: white;
}

.notification.error {
  background: #ef4444;
  color: white;
}

.notification.info {
  background: #3b82f6;
  color: white;
}

.notification.warning {
  background: #f59e0b;
  color: white;
}

.icon {
  font-size: 1.5rem;
}

.message {
  flex: 1;
  margin: 0;
}

.closeBtn {
  background: transparent;
  border: none;
  color: inherit;
  cursor: pointer;
  font-size: 1.25rem;
  padding: 0.25rem;
  transition: opacity 0.3s;
}

.closeBtn:hover {
  opacity: 0.7;
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}
''',

    # AUTH COMPONENTS - MISSING
    
    "frontend/web-app/src/components/auth/ForgotPassword/ForgotPassword.jsx": '''import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import styles from './ForgotPassword.module.css';

const ForgotPassword = () => {
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [sent, setSent] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      // API call to send reset email
      await new Promise(resolve => setTimeout(resolve, 1500));
      setSent(true);
    } catch (error) {
      console.error('Error:', error);
    } finally {
      setLoading(false);
    }
  };

  if (sent) {
    return (
      <div className={styles.container}>
        <div className={styles.successCard}>
          <div className={styles.successIcon}>✓</div>
          <h2>Check Your Email</h2>
          <p>
            We've sent password reset instructions to <strong>{email}</strong>
          </p>
          <button onClick={() => navigate('/login')} className={styles.backBtn}>
            Back to Login
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <h2 className={styles.title}>Forgot Password?</h2>
        <p className={styles.subtitle}>
          Enter your email address and we'll send you instructions to reset your password.
        </p>

        <form onSubmit={handleSubmit} className={styles.form}>
          <div className={styles.inputGroup}>
            <label>Email Address</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="your.email@example.com"
              required
            />
          </div>

          <button type="submit" disabled={loading} className={styles.submitBtn}>
            {loading ? 'Sending...' : 'Send Reset Link'}
          </button>
        </form>

        <button onClick={() => navigate('/login')} className={styles.linkBtn}>
          Back to Login
        </button>
      </div>
    </div>
  );
};

export default ForgotPassword;
''',

    "frontend/web-app/src/components/auth/ForgotPassword/ForgotPassword.module.css": '''
.container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 2rem;
}

.card, .successCard {
  background: white;
  padding: 3rem;
  border-radius: 16px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  max-width: 450px;
  width: 100%;
  animation: slideUp 0.5s ease-out;
}

.successCard {
  text-align: center;
}

.successIcon {
  width: 80px;
  height: 80px;
  background: #10b981;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  margin: 0 auto 1.5rem;
  animation: scaleIn 0.5s ease-out;
}

.title {
  font-size: 2rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem;
}

.subtitle {
  color: #6b7280;
  margin: 0 0 2rem;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.inputGroup {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.inputGroup label {
  font-weight: 600;
  color: #374151;
}

.inputGroup input {
  padding: 0.875rem 1rem;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  font-size: 1rem;
  transition: all 0.3s;
}

.inputGroup input:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.submitBtn {
  padding: 1rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s;
}

.submitBtn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
}

.submitBtn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.linkBtn, .backBtn {
  background: transparent;
  border: none;
  color: #667eea;
  font-weight: 600;
  cursor: pointer;
  padding: 0.5rem;
  transition: color 0.3s;
}

.linkBtn:hover, .backBtn:hover {
  color: #764ba2;
}

.backBtn {
  background: #667eea;
  color: white;
  padding: 1rem 2rem;
  border-radius: 8px;
  margin-top: 1rem;
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
''',

    "frontend/web-app/src/components/auth/TwoFactorAuth/TwoFactorAuth.jsx": '''import React, { useState, useRef, useEffect } from 'react';
import styles from './TwoFactorAuth.module.css';

const TwoFactorAuth = ({ onVerify, onResend }) => {
  const [code, setCode] = useState(['', '', '', '', '', '']);
  const [loading, setLoading] = useState(false);
  const inputRefs = useRef([]);

  useEffect(() => {
    inputRefs.current[0]?.focus();
  }, []);

  const handleChange = (index, value) => {
    if (value.length <= 1 && /^[0-9]*$/.test(value)) {
      const newCode = [...code];
      newCode[index] = value;
      setCode(newCode);

      if (value && index < 5) {
        inputRefs.current[index + 1]?.focus();
      }

      if (newCode.every(digit => digit !== '')) {
        handleSubmit(newCode.join(''));
      }
    }
  };

  const handleKeyDown = (index, e) => {
    if (e.key === 'Backspace' && !code[index] && index > 0) {
      inputRefs.current[index - 1]?.focus();
    }
  };

  const handlePaste = (e) => {
    e.preventDefault();
    const pastedData = e.clipboardData.getData('text').slice(0, 6);
    
    if (/^[0-9]{6}$/.test(pastedData)) {
      const newCode = pastedData.split('');
      setCode(newCode);
      handleSubmit(pastedData);
    }
  };

  const handleSubmit = async (fullCode) => {
    setLoading(true);
    try {
      await onVerify(fullCode);
    } catch (error) {
      setCode(['', '', '', '', '', '']);
      inputRefs.current[0]?.focus();
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.iconWrapper}>
        <div className={styles.icon}>🔐</div>
      </div>

      <h2 className={styles.title}>Two-Factor Authentication</h2>
      <p className={styles.subtitle}>
        Enter the 6-digit code sent to your registered device
      </p>

      <div className={styles.codeInputs} onPaste={handlePaste}>
        {code.map((digit, index) => (
          <input
            key={index}
            ref={(el) => (inputRefs.current[index] = el)}
            type="text"
            inputMode="numeric"
            maxLength="1"
            value={digit}
            onChange={(e) => handleChange(index, e.target.value)}
            onKeyDown={(e) => handleKeyDown(index, e)}
            className={styles.codeInput}
            disabled={loading}
          />
        ))}
      </div>

      {loading && <div className={styles.loader}>Verifying...</div>}

      <button onClick={onResend} className={styles.resendBtn}>
        Didn't receive code? Resend
      </button>
    </div>
  );
};

export default TwoFactorAuth;
''',

    "frontend/web-app/src/components/auth/TwoFactorAuth/TwoFactorAuth.module.css": '''
.container {
  text-align: center;
  padding: 2rem;
  max-width: 500px;
  margin: 0 auto;
}

.iconWrapper {
  margin-bottom: 1.5rem;
}

.icon {
  font-size: 4rem;
  animation: pulse 2s infinite;
}

.title {
  font-size: 1.75rem;
  font-weight: 700;
  color: #1f2937;
  margin: 0 0 0.5rem;
}

.subtitle {
  color: #6b7280;
  margin: 0 0 2rem;
}

.codeInputs {
  display: flex;
  gap: 0.75rem;
  justify-content: center;
  margin-bottom: 2rem;
}

.codeInput {
  width: 60px;
  height: 70px;
  font-size: 2rem;
  text-align: center;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  transition: all 0.3s;
  font-weight: 600;
}

.codeInput:focus {
  outline: none;
  border-color: #667eea;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
  transform: scale(1.05);
}

.codeInput:disabled {
  background: #f9fafb;
  cursor: not-allowed;
}

.loader {
  color: #667eea;
  font-weight: 600;
  margin: 1rem 0;
  animation: fadeIn 0.3s;
}

.resendBtn {
  background: transparent;
  border: none;
  color: #667eea;
  font-weight: 600;
  cursor: pointer;
  padding: 0.5rem 1rem;
  transition: all 0.3s;
}

.resendBtn:hover {
  color: #764ba2;
  text-decoration: underline;
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@media (max-width: 640px) {
  .codeInput {
    width: 45px;
    height: 55px;
    font-size: 1.5rem;
  }
  
  .codeInputs {
    gap: 0.5rem;
  }
}
''',

    # EXAMINATION COMPONENTS - PROCTORING
    
    "frontend/web-app/src/components/examination/Proctoring/CameraView/CameraView.jsx": '''import React, { useRef, useEffect, useState } from 'react';
import { FaCamera, FaVideo, FaVideoSlash } from 'react-icons/fa';
import styles from './CameraView.module.css';

const CameraView = ({ onFrameCapture, interval = 5000 }) => {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [stream, setStream] = useState(null);
  const [isActive, setIsActive] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    startCamera();
    return () => stopCamera();
  }, []);

  useEffect(() => {
    if (isActive && onFrameCapture) {
      const captureInterval = setInterval(() => {
        captureFrame();
      }, interval);

      return () => clearInterval(captureInterval);
    }
  }, [isActive, interval, onFrameCapture]);

  const startCamera = async () => {
    try {
      const mediaStream = await navigator.mediaDevices.getUserMedia({
        video: {
          width: { ideal: 1280 },
          height: { ideal: 720 },
          facingMode: 'user'
        },
        audio: false
      });

      setStream(mediaStream);
      if (videoRef.current) {
        videoRef.current.srcObject = mediaStream;
      }
      setIsActive(true);
      setError(null);
    } catch (err) {
      setError('Camera access denied. Proctoring requires camera permission.');
      console.error('Camera error:', err);
    }
  };

  const stopCamera = () => {
    if (stream) {
      stream.getTracks().forEach(track => track.stop());
      setStream(null);
      setIsActive(false);
    }
  };

  const captureFrame = () => {
    if (videoRef.current && canvasRef.current) {
      const video = videoRef.current;
      const canvas = canvasRef.current;
      const context = canvas.getContext('2d');

      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      context.drawImage(video, 0, 0);

      canvas.toBlob((blob) => {
        if (onFrameCapture && blob) {
          onFrameCapture(blob);
        }
      }, 'image/jpeg', 0.8);
    }
  };

  const toggleCamera = () => {
    if (isActive) {
      stopCamera();
    } else {
      startCamera();
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <div className={styles.statusIndicator}>
          <div className={`${styles.dot} ${isActive ? styles.active : ''}`} />
          <span>{isActive ? 'Proctoring Active' : 'Camera Inactive'}</span>
        </div>
        
        <button onClick={toggleCamera} className={styles.toggleBtn}>
          {isActive ? <FaVideoSlash /> : <FaVideo />}
        </button>
      </div>

      <div className={styles.videoWrapper}>
        {error ? (
          <div className={styles.error}>
            <FaCamera className={styles.errorIcon} />
            <p>{error}</p>
            <button onClick={startCamera} className={styles.retryBtn}>
              Retry
            </button>
          </div>
        ) : (
          <>
            <video
              ref={videoRef}
              autoPlay
              playsInline
              muted
              className={styles.video}
            />
            <canvas ref={canvasRef} style={{ display: 'none' }} />
            
            {isActive && (
              <div className={styles.overlay}>
                <div className={styles.scanLine} />
              </div>
            )}
          </>
        )}
      </div>

      <p className={styles.notice}>
        🔒 Your video feed is processed in real-time for proctoring purposes
      </p>
    </div>
  );
};

export default CameraView;
''',

    "frontend/web-app/src/components/examination/Proctoring/CameraView/CameraView.module.css": '''
.container {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
}

.statusIndicator {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
  color: #475569;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #cbd5e1;
  animation: pulse 2s infinite;
}

.dot.active {
  background: #10b981;
}

.toggleBtn {
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: background 0.3s;
}

.toggleBtn:hover {
  background: #2563eb;
}

.videoWrapper {
  position: relative;
  aspect-ratio: 16/9;
  background: #000;
  overflow: hidden;
}

.video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.overlay {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.scanLine {
  position: absolute;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, #10b981, transparent);
  animation: scan 3s linear infinite;
}

.error {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 2rem;
  color: #ef4444;
  text-align: center;
}

.errorIcon {
  font-size: 3rem;
  margin-bottom: 1rem;
  opacity: 0.5;
}

.retryBtn {
  margin-top: 1rem;
  padding: 0.5rem 1.5rem;
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s;
}

.retryBtn:hover {
  background: #2563eb;
}

.notice {
  padding: 1rem;
  margin: 0;
  font-size: 0.875rem;
  color: #64748b;
  text-align: center;
  background: #f8fafc;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

@keyframes scan {
  0% {
    top: 0;
  }
  100% {
    top: 100%;
  }
}
''',
}

print(f"🚀 Generating {len(FRONTEND_PART1)} frontend files (Part 1)...")
for filepath, content in FRONTEND_PART1.items():
    create_file(filepath, content)

print(f"\n✅ Successfully created {len(FRONTEND_PART1)} files!")
print("\n📦 Created:")
print("  ✅ Common Components (Sidebar, Layout, Notification)")
print("  ✅ Auth Components (ForgotPassword, TwoFactorAuth)")
print("  ✅ Proctoring Component (CameraView)")
print("\n🔄 Generating more components...")
