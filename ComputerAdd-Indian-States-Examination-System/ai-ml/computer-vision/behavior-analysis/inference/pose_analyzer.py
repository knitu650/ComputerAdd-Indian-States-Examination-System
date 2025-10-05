import cv2
import numpy as np
import mediapipe as mp

class PoseAnalyzer:
    """Analyze student pose and posture during exam"""
    
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            enable_segmentation=False,
            min_detection_confidence=0.5
        )
        
        self.mp_drawing = mp.solutions.drawing_utils
    
    def analyze_pose(self, image):
        """
        Analyze pose in image
        
        Returns:
            Dict with pose landmarks and analysis
        """
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image_rgb)
        
        if not results.pose_landmarks:
            return None
        
        landmarks = results.pose_landmarks.landmark
        
        analysis = {
            'landmarks': landmarks,
            'is_sitting': self.check_sitting_posture(landmarks),
            'head_angle': self.calculate_head_angle(landmarks),
            'is_looking_away': self.check_looking_away(landmarks)
        }
        
        return analysis
    
    def check_sitting_posture(self, landmarks):
        """Check if person is in sitting posture"""
        # Simple check based on shoulder and hip positions
        left_shoulder = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER]
        left_hip = landmarks[self.mp_pose.PoseLandmark.LEFT_HIP]
        
        # If shoulders are significantly above hips, likely sitting
        vertical_diff = left_shoulder.y - left_hip.y
        
        return vertical_diff < -0.1  # Threshold for sitting
    
    def calculate_head_angle(self, landmarks):
        """Calculate head tilt angle"""
        left_eye = landmarks[self.mp_pose.PoseLandmark.LEFT_EYE]
        right_eye = landmarks[self.mp_pose.PoseLandmark.RIGHT_EYE]
        nose = landmarks[self.mp_pose.PoseLandmark.NOSE]
        
        # Calculate angle
        dx = right_eye.x - left_eye.x
        dy = right_eye.y - left_eye.y
        angle = np.arctan2(dy, dx) * 180 / np.pi
        
        return angle
    
    def check_looking_away(self, landmarks):
        """Check if person is looking away from screen"""
        nose = landmarks[self.mp_pose.PoseLandmark.NOSE]
        left_eye = landmarks[self.mp_pose.PoseLandmark.LEFT_EYE]
        right_eye = landmarks[self.mp_pose.PoseLandmark.RIGHT_EYE]
        
        # Simple check based on nose position relative to eyes
        eye_center_x = (left_eye.x + right_eye.x) / 2
        nose_offset = abs(nose.x - eye_center_x)
        
        return nose_offset > 0.05  # Threshold for looking away

if __name__ == '__main__':
    analyzer = PoseAnalyzer()
    print("Pose analyzer initialized")
