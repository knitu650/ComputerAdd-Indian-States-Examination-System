const wrtc = require('wrtc');

class WebRTCService {
  
  constructor() {
    this.peerConnections = new Map();
  }
  
  createPeerConnection(userId) {
    const pc = new wrtc.RTCPeerConnection({
      iceServers: [
        { urls: 'stun:stun.l.google.com:19302' }
      ]
    });
    
    this.peerConnections.set(userId, pc);
    
    return pc;
  }
  
  async createOffer(userId) {
    const pc = this.peerConnections.get(userId);
    
    if (!pc) {
      throw new Error('Peer connection not found');
    }
    
    const offer = await pc.createOffer();
    await pc.setLocalDescription(offer);
    
    return offer;
  }
  
  async handleAnswer(userId, answer) {
    const pc = this.peerConnections.get(userId);
    
    if (!pc) {
      throw new Error('Peer connection not found');
    }
    
    await pc.setRemoteDescription(new wrtc.RTCSessionDescription(answer));
  }
  
  async addIceCandidate(userId, candidate) {
    const pc = this.peerConnections.get(userId);
    
    if (!pc) {
      throw new Error('Peer connection not found');
    }
    
    await pc.addIceCandidate(new wrtc.RTCIceCandidate(candidate));
  }
  
  closePeerConnection(userId) {
    const pc = this.peerConnections.get(userId);
    
    if (pc) {
      pc.close();
      this.peerConnections.delete(userId);
    }
  }
}

module.exports = new WebRTCService();
