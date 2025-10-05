import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
import numpy as np

class FaceRecognitionTrainer:
    """Train face recognition model using transfer learning"""
    
    def __init__(self, num_classes=1000, img_size=(224, 224)):
        self.num_classes = num_classes
        self.img_size = img_size
        self.model = self.build_model()
    
    def build_model(self):
        """Build model using ResNet50 as base"""
        base_model = ResNet50(
            weights='imagenet',
            include_top=False,
            input_shape=(*self.img_size, 3)
        )
        
        # Freeze base model layers
        for layer in base_model.layers[:-10]:
            layer.trainable = False
        
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(1024, activation='relu')(x)
        x = Dropout(0.5)(x)
        x = Dense(512, activation='relu')(x)
        x = Dropout(0.3)(x)
        outputs = Dense(self.num_classes, activation='softmax')(x)
        
        model = Model(inputs=base_model.input, outputs=outputs)
        
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
            loss='categorical_crossentropy',
            metrics=['accuracy', 'top_k_categorical_accuracy']
        )
        
        return model
    
    def train(self, train_data, val_data, epochs=100):
        """Train face recognition model"""
        history = self.model.fit(
            train_data,
            validation_data=val_data,
            epochs=epochs,
            callbacks=[
                tf.keras.callbacks.ModelCheckpoint(
                    'models/face_recognition_best.h5',
                    save_best_only=True,
                    monitor='val_accuracy'
                ),
                tf.keras.callbacks.EarlyStopping(patience=10),
                tf.keras.callbacks.TensorBoard(log_dir='./logs')
            ]
        )
        
        return history
    
    def save_model(self, path='models/face_recognition_model.h5'):
        """Save trained model"""
        self.model.save(path)
        print(f"Model saved to {path}")

if __name__ == '__main__':
    trainer = FaceRecognitionTrainer()
    print("Face recognition trainer initialized")
