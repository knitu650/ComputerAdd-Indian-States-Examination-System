import React, { useEffect } from 'react';
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
