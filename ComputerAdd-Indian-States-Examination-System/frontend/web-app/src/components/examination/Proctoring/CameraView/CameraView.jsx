import React, { useRef, useEffect, useState } from 'react';
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
