import cv2
import numpy as np

class ObjectDetector:
    """Detect unauthorized objects during exams"""
    
    def __init__(self):
        # Unauthorized objects to detect
        self.unauthorized_objects = [
            'cell phone', 'mobile phone', 'book', 'paper',
            'calculator', 'tablet', 'laptop', 'smartwatch'
        ]
        
        # Load YOLO (you would load actual model here)
        # self.net = cv2.dnn.readNet('yolo.weights', 'yolo.cfg')
        self.confidence_threshold = 0.5
    
    def detect_objects(self, image):
        """
        Detect objects in image
        
        Returns:
            List of detected objects with confidence
        """
        detected_objects = []
        
        # Placeholder for actual detection
        # In production, use YOLO or similar
        
        # Example structure:
        # for detection in detections:
        #     if detection['label'] in self.unauthorized_objects:
        #         detected_objects.append({
        #             'object': detection['label'],
        #             'confidence': detection['confidence'],
        #             'bbox': detection['bbox']
        #         })
        
        return detected_objects
    
    def check_for_violations(self, image):
        """
        Check if any unauthorized objects are present
        
        Returns:
            (has_violation, list of violations)
        """
        objects = self.detect_objects(image)
        
        violations = [
            obj for obj in objects
            if obj['confidence'] >= self.confidence_threshold
        ]
        
        return len(violations) > 0, violations
    
    def detect_phone(self, image):
        """Specific detection for phones"""
        objects = self.detect_objects(image)
        
        phone_keywords = ['phone', 'mobile', 'smartphone']
        phones = [
            obj for obj in objects
            if any(keyword in obj['object'].lower() for keyword in phone_keywords)
        ]
        
        return len(phones) > 0, phones

if __name__ == '__main__':
    detector = ObjectDetector()
    print("Object detector initialized")
