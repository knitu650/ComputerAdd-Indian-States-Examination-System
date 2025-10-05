import { io } from 'socket.io-client';

class ProctoringSocket {
  constructor() {
    this.socket = null;
    this.isConnected = false;
  }

  connect(examId, token) {
    if (this.socket) {
      this.disconnect();
    }

    this.socket = io(`${process.env.REACT_APP_WS_URL || 'http://localhost:3003'}`, {
      auth: {
        token
      },
      query: {
        examId
      }
    });

    this.socket.on('connect', () => {
      this.isConnected = true;
      console.log('Proctoring socket connected');
    });

    this.socket.on('disconnect', () => {
      this.isConnected = false;
      console.log('Proctoring socket disconnected');
    });

    return this.socket;
  }

  disconnect() {
    if (this.socket) {
      this.socket.disconnect();
      this.socket = null;
      this.isConnected = false;
    }
  }

  sendFrame(frameData) {
    if (this.socket && this.isConnected) {
      this.socket.emit('video-frame', frameData);
    }
  }

  onViolation(callback) {
    if (this.socket) {
      this.socket.on('violation-detected', callback);
    }
  }

  offViolation(callback) {
    if (this.socket) {
      this.socket.off('violation-detected', callback);
    }
  }
}

export default new ProctoringSocket();
