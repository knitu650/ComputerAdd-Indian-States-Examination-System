import os
import json
from datetime import datetime
import tensorflow as tf

class ModelTrainingPipeline:
    """Complete training pipeline for AI/ML models"""
    
    def __init__(self, config):
        self.config = config
        self.model_type = config.get('model_type')
        self.output_dir = config.get('output_dir', 'models')
        
        os.makedirs(self.output_dir, exist_ok=True)
    
    def load_data(self):
        """Load and prepare training data"""
        print("Loading training data...")
        
        train_path = self.config.get('train_data_path')
        val_path = self.config.get('val_data_path')
        
        # Load data based on type
        if self.model_type == 'computer_vision':
            train_data = self._load_image_data(train_path)
            val_data = self._load_image_data(val_path)
        elif self.model_type == 'nlp':
            train_data = self._load_text_data(train_path)
            val_data = self._load_text_data(val_path)
        else:
            train_data = self._load_tabular_data(train_path)
            val_data = self._load_tabular_data(val_path)
        
        return train_data, val_data
    
    def preprocess_data(self, data):
        """Preprocess data"""
        print("Preprocessing data...")
        
        # Apply preprocessing based on model type
        if self.model_type == 'computer_vision':
            return self._preprocess_images(data)
        elif self.model_type == 'nlp':
            return self._preprocess_text(data)
        else:
            return self._preprocess_tabular(data)
    
    def build_model(self):
        """Build model architecture"""
        print(f"Building {self.model_type} model...")
        
        model_config = self.config.get('model_config', {})
        
        # Build model based on type
        if self.model_type == 'computer_vision':
            model = self._build_cv_model(model_config)
        elif self.model_type == 'nlp':
            model = self._build_nlp_model(model_config)
        else:
            model = self._build_ml_model(model_config)
        
        return model
    
    def train_model(self, model, train_data, val_data):
        """Train the model"""
        print("Training model...")
        
        epochs = self.config.get('epochs', 10)
        batch_size = self.config.get('batch_size', 32)
        
        callbacks = self._setup_callbacks()
        
        history = model.fit(
            train_data,
            validation_data=val_data,
            epochs=epochs,
            batch_size=batch_size,
            callbacks=callbacks
        )
        
        return history
    
    def evaluate_model(self, model, test_data):
        """Evaluate trained model"""
        print("Evaluating model...")
        
        results = model.evaluate(test_data)
        
        return results
    
    def save_model(self, model, metrics):
        """Save trained model and metadata"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        model_name = f"{self.model_type}_{timestamp}"
        
        model_path = os.path.join(self.output_dir, f"{model_name}.h5")
        model.save(model_path)
        
        # Save metadata
        metadata = {
            'model_name': model_name,
            'model_type': self.model_type,
            'training_date': timestamp,
            'config': self.config,
            'metrics': metrics
        }
        
        metadata_path = os.path.join(self.output_dir, f"{model_name}_metadata.json")
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"Model saved to {model_path}")
        
        return model_path
    
    def run(self):
        """Run complete training pipeline"""
        print("=" * 50)
        print("Starting Training Pipeline")
        print("=" * 50)
        
        # Load data
        train_data, val_data = self.load_data()
        
        # Preprocess
        train_data = self.preprocess_data(train_data)
        val_data = self.preprocess_data(val_data)
        
        # Build model
        model = self.build_model()
        
        # Train
        history = self.train_model(model, train_data, val_data)
        
        # Evaluate
        metrics = self.evaluate_model(model, val_data)
        
        # Save
        model_path = self.save_model(model, metrics)
        
        print("=" * 50)
        print("Training Pipeline Complete!")
        print(f"Model saved to: {model_path}")
        print("=" * 50)
        
        return model, history
    
    def _setup_callbacks(self):
        """Setup training callbacks"""
        callbacks = [
            tf.keras.callbacks.EarlyStopping(
                patience=5,
                restore_best_weights=True
            ),
            tf.keras.callbacks.ReduceLROnPlateau(
                patience=3,
                factor=0.5
            ),
            tf.keras.callbacks.TensorBoard(
                log_dir='./logs'
            )
        ]
        
        return callbacks
    
    def _load_image_data(self, path):
        """Load image data"""
        # Placeholder
        return None
    
    def _load_text_data(self, path):
        """Load text data"""
        # Placeholder
        return None
    
    def _load_tabular_data(self, path):
        """Load tabular data"""
        # Placeholder
        return None
    
    def _preprocess_images(self, data):
        """Preprocess image data"""
        return data
    
    def _preprocess_text(self, data):
        """Preprocess text data"""
        return data
    
    def _preprocess_tabular(self, data):
        """Preprocess tabular data"""
        return data
    
    def _build_cv_model(self, config):
        """Build computer vision model"""
        # Placeholder
        return None
    
    def _build_nlp_model(self, config):
        """Build NLP model"""
        # Placeholder
        return None
    
    def _build_ml_model(self, config):
        """Build ML model"""
        # Placeholder
        return None

if __name__ == '__main__':
    config = {
        'model_type': 'computer_vision',
        'train_data_path': 'data/train',
        'val_data_path': 'data/val',
        'epochs': 10,
        'batch_size': 32
    }
    
    pipeline = ModelTrainingPipeline(config)
    print("Training pipeline initialized")
