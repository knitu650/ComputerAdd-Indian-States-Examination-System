import cv2
import numpy as np

class LivenessDetector:
    """Detect if face is live or spoofed"""
    
    def __init__(self):
        self.texture_threshold = 0.6
        self.motion_threshold = 0.3
    
    def detect_liveness(self, frames):
        """
        Detect if face in frames is live
        
        Args:
            frames: List of consecutive frames
            
        Returns:
            (is_live, confidence)
        """
        # Texture analysis
        texture_score = self._analyze_texture(frames[0])
        
        # Motion analysis
        motion_score = self._analyze_motion(frames)
        
        # Combined score
        liveness_score = (texture_score + motion_score) / 2
        is_live = liveness_score > 0.5
        
        return is_live, float(liveness_score)
    
    def _analyze_texture(self, frame):
        """Analyze image texture"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Calculate LBP (Local Binary Pattern)
        lbp = self._calculate_lbp(gray)
        
        # Analyze texture diversity
        hist, _ = np.histogram(lbp, bins=256, range=(0, 256))
        hist = hist.astype('float')
        hist /= (hist.sum() + 1e-7)
        
        # Higher entropy = more diverse texture = real face
        entropy = -np.sum(hist * np.log2(hist + 1e-7))
        
        # Normalize to 0-1
        texture_score = min(entropy / 8.0, 1.0)
        
        return texture_score
    
    def _calculate_lbp(self, image):
        """Calculate Local Binary Pattern"""
        lbp = np.zeros_like(image)
        
        for i in range(1, image.shape[0]-1):
            for j in range(1, image.shape[1]-1):
                center = image[i, j]
                code = 0
                
                code |= (image[i-1, j-1] > center) << 7
                code |= (image[i-1, j] > center) << 6
                code |= (image[i-1, j+1] > center) << 5
                code |= (image[i, j+1] > center) << 4
                code |= (image[i+1, j+1] > center) << 3
                code |= (image[i+1, j] > center) << 2
                code |= (image[i+1, j-1] > center) << 1
                code |= (image[i, j-1] > center) << 0
                
                lbp[i, j] = code
        
        return lbp
    
    def _analyze_motion(self, frames):
        """Analyze motion between frames"""
        if len(frames) < 2:
            return 0.5
        
        # Calculate optical flow
        prev_gray = cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY)
        curr_gray = cv2.cvtColor(frames[-1], cv2.COLOR_BGR2GRAY)
        
        flow = cv2.calcOpticalFlowFarneback(
            prev_gray, curr_gray, None,
            0.5, 3, 15, 3, 5, 1.2, 0
        )
        
        # Calculate motion magnitude
        magnitude = np.sqrt(flow[..., 0]**2 + flow[..., 1]**2)
        motion_score = np.mean(magnitude) / 10.0  # Normalize
        
        return min(motion_score, 1.0)
