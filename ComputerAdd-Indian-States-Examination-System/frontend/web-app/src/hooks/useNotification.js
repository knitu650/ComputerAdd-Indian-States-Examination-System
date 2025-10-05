import { useState, useCallback } from 'react';

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
