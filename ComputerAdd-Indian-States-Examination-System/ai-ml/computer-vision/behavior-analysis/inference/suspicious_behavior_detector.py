import numpy as np
from collections import deque
from datetime import datetime

class SuspiciousBehaviorDetector:
    """Detect suspicious behaviors during exam"""
    
    def __init__(self, window_size=30):
        self.window_size = window_size
        self.behavior_history = deque(maxlen=window_size)
        self.violation_threshold = 0.7
        
        # Behavior patterns
        self.behaviors = {
            'multiple_faces': {'weight': 1.0, 'threshold': 1},
            'looking_away': {'weight': 0.6, 'threshold': 15},
            'unauthorized_object': {'weight': 1.0, 'threshold': 1},
            'frequent_movement': {'weight': 0.5, 'threshold': 20},
            'no_face_detected': {'weight': 0.8, 'threshold': 10}
        }
    
    def analyze_frame(self, analysis_result):
        """
        Analyze single frame for suspicious behavior
        
        Args:
            analysis_result: Dict containing detection results
            
        Returns:
            Dict with behavior analysis
        """
        suspicious_score = 0.0
        detected_behaviors = []
        
        # Check multiple faces
        if analysis_result.get('num_faces', 1) > 1:
            suspicious_score += self.behaviors['multiple_faces']['weight']
            detected_behaviors.append('multiple_faces')
        
        # Check no face
        if analysis_result.get('num_faces', 1) == 0:
            suspicious_score += self.behaviors['no_face_detected']['weight']
            detected_behaviors.append('no_face_detected')
        
        # Check looking away
        if analysis_result.get('looking_away', False):
            suspicious_score += self.behaviors['looking_away']['weight']
            detected_behaviors.append('looking_away')
        
        # Check unauthorized objects
        if analysis_result.get('has_unauthorized_objects', False):
            suspicious_score += self.behaviors['unauthorized_object']['weight']
            detected_behaviors.append('unauthorized_object')
        
        behavior_data = {
            'timestamp': datetime.now(),
            'score': suspicious_score,
            'behaviors': detected_behaviors
        }
        
        self.behavior_history.append(behavior_data)
        
        return behavior_data
    
    def get_violation_report(self):
        """Generate violation report from behavior history"""
        if not self.behavior_history:
            return {'has_violation': False}
        
        # Count occurrences of each behavior
        behavior_counts = {}
        total_score = 0.0
        
        for entry in self.behavior_history:
            total_score += entry['score']
            for behavior in entry['behaviors']:
                behavior_counts[behavior] = behavior_counts.get(behavior, 0) + 1
        
        # Check for violations
        violations = []
        for behavior, count in behavior_counts.items():
            if count >= self.behaviors[behavior]['threshold']:
                violations.append({
                    'behavior': behavior,
                    'count': count,
                    'severity': 'high' if self.behaviors[behavior]['weight'] >= 0.8 else 'medium'
                })
        
        avg_score = total_score / len(self.behavior_history)
        
        return {
            'has_violation': len(violations) > 0 or avg_score > self.violation_threshold,
            'violations': violations,
            'average_suspicion_score': avg_score,
            'total_frames_analyzed': len(self.behavior_history)
        }
    
    def reset(self):
        """Reset behavior history"""
        self.behavior_history.clear()

if __name__ == '__main__':
    detector = SuspiciousBehaviorDetector()
    print("Suspicious behavior detector initialized")
