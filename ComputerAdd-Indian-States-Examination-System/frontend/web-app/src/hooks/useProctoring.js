import { useState, useEffect, useCallback } from 'react';
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
