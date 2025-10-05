import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
import numpy as np
import cv2

class FaceDetectionTrainer:
    """Train face detection model using CNN"""
    
    def __init__(self, img_size=(224, 224)):
        self.img_size = img_size
        self.model = self.build_model()
    
    def build_model(self):
        """Build CNN model for face detection"""
        model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(*self.img_size, 3)),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Conv2D(128, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Flatten(),
            Dense(512, activation='relu'),
            Dropout(0.5),
            Dense(1, activation='sigmoid')  # Binary: face or no face
        ])
        
        model.compile(
            optimizer='adam',
            loss='binary_crossentropy',
            metrics=['accuracy']
        )
        
        return model
    
    def train(self, train_data, val_data, epochs=50, batch_size=32):
        """Train the model"""
        history = self.model.fit(
            train_data,
            validation_data=val_data,
            epochs=epochs,
            batch_size=batch_size,
            callbacks=[
                tf.keras.callbacks.EarlyStopping(patience=5, restore_best_weights=True),
                tf.keras.callbacks.ReduceLROnPlateau(patience=3, factor=0.5)
            ]
        )
        
        return history
    
    def save_model(self, path='models/face_detection_model.h5'):
        """Save trained model"""
        self.model.save(path)
        print(f"Model saved to {path}")

if __name__ == '__main__':
    trainer = FaceDetectionTrainer()
    # trainer.train(train_data, val_data)
    print("Face detection trainer initialized")
