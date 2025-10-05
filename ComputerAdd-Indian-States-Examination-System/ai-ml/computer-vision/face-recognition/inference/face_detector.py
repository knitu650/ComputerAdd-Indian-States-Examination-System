import cv2
import numpy as np
from tensorflow.keras.models import load_model

class FaceDetector:
    """Real-time face detection using trained model"""
    
    def __init__(self, model_path='models/face_detection_model.h5'):
        self.model = load_model(model_path)
        self.img_size = (224, 224)
        
        # Fallback to OpenCV Haar Cascade
        self.haar_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
    
    def detect_faces(self, image):
        """
        Detect faces in image
        
        Args:
            image: numpy array (BGR format)
            
        Returns:
            List of face bounding boxes [(x, y, w, h), ...]
        """
        # Convert to grayscale for Haar Cascade
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces using Haar Cascade
        faces = self.haar_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        return faces
    
    def detect_multiple_faces(self, image):
        """Check if multiple faces are present"""
        faces = self.detect_faces(image)
        return len(faces) > 1, len(faces)
    
    def extract_face(self, image, bbox):
        """Extract face region from image"""
        x, y, w, h = bbox
        face = image[y:y+h, x:x+w]
        face = cv2.resize(face, self.img_size)
        return face
    
    def preprocess_face(self, face):
        """Preprocess face for model input"""
        face = face.astype('float32') / 255.0
        face = np.expand_dims(face, axis=0)
        return face

if __name__ == '__main__':
    detector = FaceDetector()
    print("Face detector initialized")
