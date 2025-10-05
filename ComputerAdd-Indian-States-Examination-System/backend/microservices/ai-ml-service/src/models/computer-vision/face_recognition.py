import cv2
import numpy as np
import tensorflow as tf
from typing import Dict, List, Tuple

class FaceRecognitionModel:
    def __init__(self, model_path: str = None):
        self.model = self.load_model(model_path)
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
    
    def load_model(self, model_path: str = None):
        """Load pre-trained face recognition model"""
        if model_path:
            return tf.keras.models.load_model(model_path)
        # Default model architecture
        return self.build_default_model()
    
    def build_default_model(self):
        """Build default face recognition model"""
        model = tf.keras.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation='relu'),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(256, activation='sigmoid')
        ])
        return model
    
    def detect_faces(self, image: np.ndarray) -> List[Tuple[int, int, int, int]]:
        """Detect faces in image"""
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )
        return faces
    
    def extract_face_embeddings(self, image: np.ndarray, face_coords: Tuple) -> np.ndarray:
        """Extract face embeddings"""
        x, y, w, h = face_coords
        face = image[y:y+h, x:x+w]
        face_resized = cv2.resize(face, (224, 224))
        face_normalized = face_resized / 255.0
        face_batch = np.expand_dims(face_normalized, axis=0)
        
        embeddings = self.model.predict(face_batch, verbose=0)
        return embeddings[0]
    
    def verify_identity(self, embedding1: np.ndarray, embedding2: np.ndarray, 
                       threshold: float = 0.6) -> Dict:
        """Verify if two face embeddings match"""
        distance = np.linalg.norm(embedding1 - embedding2)
        similarity = 1 / (1 + distance)
        
        return {
            "match": similarity >= threshold,
            "confidence": float(similarity),
            "distance": float(distance)
        }
    
    def analyze_frame(self, frame: np.ndarray, reference_embedding: np.ndarray = None) -> Dict:
        """Analyze video frame for proctoring"""
        faces = self.detect_faces(frame)
        
        result = {
            "face_detected": len(faces) > 0,
            "face_count": len(faces),
            "multiple_persons": len(faces) > 1,
            "no_face": len(faces) == 0,
            "faces": []
        }
        
        if reference_embedding is not None and len(faces) > 0:
            for face in faces:
                embedding = self.extract_face_embeddings(frame, face)
                verification = self.verify_identity(reference_embedding, embedding)
                result["faces"].append({
                    "coordinates": face.tolist(),
                    "verified": verification["match"],
                    "confidence": verification["confidence"]
                })
        
        return result
