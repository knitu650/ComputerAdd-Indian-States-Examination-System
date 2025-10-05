import numpy as np
import cv2
from tensorflow.keras.models import load_model
from sklearn.metrics.pairwise import cosine_similarity

class FaceRecognizer:
    """Face recognition and verification system"""
    
    def __init__(self, model_path='models/face_recognition_model.h5'):
        self.model = load_model(model_path)
        self.embeddings_db = {}  # Store user face embeddings
        self.threshold = 0.6  # Similarity threshold
    
    def extract_embedding(self, face_image):
        """
        Extract face embedding (feature vector)
        
        Args:
            face_image: preprocessed face image
            
        Returns:
            numpy array of face embedding
        """
        # Preprocess
        if face_image.shape != (224, 224, 3):
            face_image = cv2.resize(face_image, (224, 224))
        
        face_image = face_image.astype('float32') / 255.0
        face_image = np.expand_dims(face_image, axis=0)
        
        # Get embedding from second-to-last layer
        embedding_model = Model(
            inputs=self.model.input,
            outputs=self.model.layers[-2].output
        )
        
        embedding = embedding_model.predict(face_image)
        embedding = embedding.flatten()
        embedding = embedding / np.linalg.norm(embedding)  # Normalize
        
        return embedding
    
    def register_face(self, user_id, face_image):
        """Register user's face embedding"""
        embedding = self.extract_embedding(face_image)
        self.embeddings_db[user_id] = embedding
        return True
    
    def verify_face(self, user_id, face_image):
        """
        Verify if face matches registered user
        
        Returns:
            (is_match, confidence)
        """
        if user_id not in self.embeddings_db:
            return False, 0.0
        
        embedding = self.extract_embedding(face_image)
        registered_embedding = self.embeddings_db[user_id]
        
        # Calculate cosine similarity
        similarity = cosine_similarity(
            embedding.reshape(1, -1),
            registered_embedding.reshape(1, -1)
        )[0][0]
        
        is_match = similarity >= self.threshold
        
        return is_match, float(similarity)
    
    def identify_face(self, face_image, top_k=5):
        """
        Identify face from database
        
        Returns:
            List of (user_id, confidence) tuples
        """
        if not self.embeddings_db:
            return []
        
        embedding = self.extract_embedding(face_image)
        
        similarities = []
        for user_id, registered_embedding in self.embeddings_db.items():
            similarity = cosine_similarity(
                embedding.reshape(1, -1),
                registered_embedding.reshape(1, -1)
            )[0][0]
            similarities.append((user_id, float(similarity)))
        
        # Sort by similarity
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        return similarities[:top_k]

if __name__ == '__main__':
    recognizer = FaceRecognizer()
    print("Face recognizer initialized")
