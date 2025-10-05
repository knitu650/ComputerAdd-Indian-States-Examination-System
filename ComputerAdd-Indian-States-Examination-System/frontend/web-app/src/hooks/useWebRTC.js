import { useState, useEffect, useRef } from 'react';

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
