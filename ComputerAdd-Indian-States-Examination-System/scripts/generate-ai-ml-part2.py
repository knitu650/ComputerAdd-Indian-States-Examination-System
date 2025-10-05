#!/usr/bin/env python3
"""AI/ML Suite Part 2: ML Models, Pipelines, Configs, Utils"""

import os

BASE_DIR = "/workspace/ComputerAdd-Indian-States-Examination-System"

def create_file(filepath, content):
    full_path = os.path.join(BASE_DIR, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {filepath}")

AI_ML_PART2_FILES = {
    # ====================  MACHINE LEARNING ====================
    
    "ai-ml/machine-learning/adaptive-testing/inference/adaptive_engine.py": '''import numpy as np
from sklearn.linear_model import LogisticRegression

class AdaptiveTestingEngine:
    """Adaptive testing using Item Response Theory (IRT)"""
    
    def __init__(self):
        self.theta = 0.0  # Initial ability estimate
        self.questions_asked = []
        self.responses = []
        self.min_questions = 10
        self.max_questions = 30
        self.precision_threshold = 0.3
    
    def estimate_ability(self):
        """Estimate student ability using maximum likelihood"""
        if not self.responses:
            return 0.0
        
        # Simple ability estimation
        correct = sum(self.responses)
        total = len(self.responses)
        
        if total == 0:
            return 0.0
        
        # Convert to theta scale (-3 to 3)
        proportion_correct = correct / total
        
        if proportion_correct == 1.0:
            return 3.0
        elif proportion_correct == 0.0:
            return -3.0
        else:
            # Logit transform
            theta = np.log(proportion_correct / (1 - proportion_correct))
            return np.clip(theta, -3, 3)
    
    def select_next_question(self, question_pool):
        """
        Select next question that maximizes information
        
        Args:
            question_pool: List of available questions with difficulty
            
        Returns:
            Selected question
        """
        current_ability = self.estimate_ability()
        
        # Filter out already asked questions
        available_questions = [
            q for q in question_pool
            if q['id'] not in [qa['id'] for qa in self.questions_asked]
        ]
        
        if not available_questions:
            return None
        
        # Select question closest to current ability
        best_question = min(
            available_questions,
            key=lambda q: abs(q['difficulty'] - current_ability)
        )
        
        return best_question
    
    def record_response(self, question, response):
        """Record student response"""
        self.questions_asked.append(question)
        self.responses.append(int(response))
        
        # Update ability estimate
        self.theta = self.estimate_ability()
    
    def should_stop(self):
        """Determine if test should stop"""
        if len(self.questions_asked) < self.min_questions:
            return False
        
        if len(self.questions_asked) >= self.max_questions:
            return True
        
        # Check if ability estimate is stable
        if len(self.responses) >= 5:
            recent_estimates = []
            for i in range(len(self.responses) - 4, len(self.responses) + 1):
                # Calculate ability at each point
                correct = sum(self.responses[:i])
                total = i
                if total > 0:
                    prop = correct / total
                    if 0 < prop < 1:
                        estimate = np.log(prop / (1 - prop))
                        recent_estimates.append(estimate)
            
            if recent_estimates:
                variance = np.var(recent_estimates)
                if variance < self.precision_threshold:
                    return True
        
        return False
    
    def get_final_score(self):
        """Get final ability score and confidence"""
        ability = self.estimate_ability()
        
        # Calculate confidence based on number of questions
        confidence = min(1.0, len(self.questions_asked) / self.max_questions)
        
        # Convert theta to percentage score (0-100)
        # theta ranges from -3 to 3
        percentage_score = ((ability + 3) / 6) * 100
        percentage_score = np.clip(percentage_score, 0, 100)
        
        return {
            'ability_estimate': ability,
            'percentage_score': percentage_score,
            'questions_answered': len(self.questions_asked),
            'confidence': confidence
        }

if __name__ == '__main__':
    engine = AdaptiveTestingEngine()
    print("Adaptive testing engine initialized")
''',

    "ai-ml/machine-learning/recommendation-engine/inference/recommender_engine.py": '''import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngine:
    """Recommend study materials and exams to students"""
    
    def __init__(self):
        self.user_profiles = {}
        self.content_features = {}
        self.interaction_matrix = None
    
    def build_user_profile(self, user_id, exam_history, performance):
        """Build user profile from exam history"""
        profile = {
            'user_id': user_id,
            'topics_mastered': [],
            'topics_weak': [],
            'difficulty_level': self._estimate_difficulty_level(performance),
            'learning_pace': self._estimate_learning_pace(exam_history),
            'preferred_topics': self._get_preferred_topics(exam_history)
        }
        
        self.user_profiles[user_id] = profile
        return profile
    
    def recommend_exams(self, user_id, available_exams, top_k=5):
        """
        Recommend exams for user
        
        Returns:
            List of recommended exam IDs
        """
        if user_id not in self.user_profiles:
            # Cold start: recommend popular exams
            return self._recommend_popular(available_exams, top_k)
        
        user_profile = self.user_profiles[user_id]
        
        # Score each exam
        scores = []
        for exam in available_exams:
            score = self._calculate_exam_score(user_profile, exam)
            scores.append((exam['id'], score))
        
        # Sort by score and return top k
        scores.sort(key=lambda x: x[1], reverse=True)
        recommendations = [exam_id for exam_id, _ in scores[:top_k]]
        
        return recommendations
    
    def recommend_study_materials(self, user_id, topic, top_k=10):
        """Recommend study materials for a topic"""
        if user_id not in self.user_profiles:
            return []
        
        user_profile = self.user_profiles[user_id]
        difficulty = user_profile['difficulty_level']
        
        # Filter materials by topic and difficulty
        recommendations = [
            {
                'title': f'Study Material on {topic}',
                'difficulty': difficulty,
                'type': 'article',
                'relevance': 0.9
            }
        ]
        
        return recommendations[:top_k]
    
    def _estimate_difficulty_level(self, performance):
        """Estimate appropriate difficulty level for user"""
        avg_score = np.mean([p['score'] for p in performance])
        
        if avg_score >= 85:
            return 'hard'
        elif avg_score >= 60:
            return 'medium'
        else:
            return 'easy'
    
    def _estimate_learning_pace(self, exam_history):
        """Estimate user's learning pace"""
        if len(exam_history) < 2:
            return 'normal'
        
        # Calculate time between exams
        times = [h['timestamp'] for h in exam_history]
        gaps = np.diff(times)
        avg_gap = np.mean(gaps)
        
        if avg_gap < 3:  # days
            return 'fast'
        elif avg_gap < 7:
            return 'normal'
        else:
            return 'slow'
    
    def _get_preferred_topics(self, exam_history):
        """Get user's preferred topics"""
        topic_counts = {}
        
        for exam in exam_history:
            for topic in exam.get('topics', []):
                topic_counts[topic] = topic_counts.get(topic, 0) + 1
        
        # Return top 3 topics
        sorted_topics = sorted(
            topic_counts.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        return [topic for topic, _ in sorted_topics[:3]]
    
    def _calculate_exam_score(self, user_profile, exam):
        """Calculate recommendation score for an exam"""
        score = 0.0
        
        # Difficulty match
        if exam['difficulty'] == user_profile['difficulty_level']:
            score += 0.4
        
        # Topic match
        for topic in exam.get('topics', []):
            if topic in user_profile['preferred_topics']:
                score += 0.3
            if topic in user_profile['topics_weak']:
                score += 0.3
        
        return score
    
    def _recommend_popular(self, exams, top_k):
        """Recommend popular exams (cold start)"""
        # Sort by number of attempts
        sorted_exams = sorted(
            exams,
            key=lambda x: x.get('attempts', 0),
            reverse=True
        )
        
        return [e['id'] for e in sorted_exams[:top_k]]

if __name__ == '__main__':
    engine = RecommendationEngine()
    print("Recommendation engine initialized")
''',

    "ai-ml/machine-learning/anomaly-detection/inference/anomaly_detector.py": '''import numpy as np
from sklearn.ensemble import IsolationForest
from collections import deque

class AnomalyDetector:
    """Detect anomalous behavior patterns in exam taking"""
    
    def __init__(self, contamination=0.1):
        self.model = IsolationForest(
            contamination=contamination,
            random_state=42
        )
        self.feature_history = deque(maxlen=1000)
        self.is_trained = False
    
    def extract_features(self, event_data):
        """
        Extract features from event data
        
        Args:
            event_data: Dict with timing, clicks, answers, etc.
            
        Returns:
            Feature vector
        """
        features = [
            event_data.get('time_per_question', 60),  # seconds
            event_data.get('num_answer_changes', 0),
            event_data.get('time_between_questions', 5),
            event_data.get('mouse_movements', 100),
            event_data.get('keyboard_events', 50),
            event_data.get('browser_focus_loss', 0),
            event_data.get('copy_paste_events', 0),
            event_data.get('rapid_answering_streak', 0)
        ]
        
        return np.array(features)
    
    def train(self, historical_data):
        """Train anomaly detector on historical data"""
        features = []
        for event in historical_data:
            feat = self.extract_features(event)
            features.append(feat)
        
        X = np.array(features)
        self.model.fit(X)
        self.is_trained = True
        
        return self
    
    def detect_anomaly(self, event_data):
        """
        Detect if event data is anomalous
        
        Returns:
            (is_anomaly, anomaly_score)
        """
        features = self.extract_features(event_data)
        features = features.reshape(1, -1)
        
        if not self.is_trained:
            # Use rule-based detection if not trained
            return self._rule_based_detection(event_data)
        
        # Predict (-1 for anomaly, 1 for normal)
        prediction = self.model.predict(features)[0]
        
        # Get anomaly score (lower = more anomalous)
        score = self.model.score_samples(features)[0]
        
        is_anomaly = prediction == -1
        
        return is_anomaly, float(score)
    
    def _rule_based_detection(self, event_data):
        """Rule-based anomaly detection (fallback)"""
        anomaly_score = 0.0
        
        # Check for suspicious patterns
        if event_data.get('time_per_question', 60) < 5:
            anomaly_score -= 0.3  # Too fast
        
        if event_data.get('num_answer_changes', 0) > 5:
            anomaly_score -= 0.2  # Too many changes
        
        if event_data.get('copy_paste_events', 0) > 0:
            anomaly_score -= 0.5  # Copy-paste detected
        
        if event_data.get('browser_focus_loss', 0) > 3:
            anomaly_score -= 0.4  # Left browser multiple times
        
        is_anomaly = anomaly_score < -0.5
        
        return is_anomaly, anomaly_score
    
    def analyze_session(self, session_events):
        """Analyze entire exam session for anomalies"""
        anomalies = []
        
        for i, event in enumerate(session_events):
            is_anomaly, score = self.detect_anomaly(event)
            
            if is_anomaly:
                anomalies.append({
                    'event_index': i,
                    'event': event,
                    'score': score
                })
        
        return {
            'total_events': len(session_events),
            'anomalies_detected': len(anomalies),
            'anomaly_rate': len(anomalies) / len(session_events) if session_events else 0,
            'anomalies': anomalies
        }

if __name__ == '__main__':
    detector = AnomalyDetector()
    print("Anomaly detector initialized")
''',

    # ==================== PIPELINES ====================
    
    "ai-ml/pipelines/training/training_pipeline.py": '''import os
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
''',

    "ai-ml/pipelines/inference/real_time_inference.py": '''import time
import numpy as np
from queue import Queue
from threading import Thread

class RealTimeInferencePipeline:
    """Real-time inference pipeline for proctoring"""
    
    def __init__(self, models):
        self.models = models
        self.input_queue = Queue(maxsize=100)
        self.output_queue = Queue(maxsize=100)
        self.is_running = False
        
        self.inference_thread = None
    
    def start(self):
        """Start inference pipeline"""
        self.is_running = True
        self.inference_thread = Thread(target=self._inference_loop)
        self.inference_thread.start()
        
        print("Real-time inference pipeline started")
    
    def stop(self):
        """Stop inference pipeline"""
        self.is_running = False
        if self.inference_thread:
            self.inference_thread.join()
        
        print("Real-time inference pipeline stopped")
    
    def process_frame(self, frame):
        """Add frame to processing queue"""
        if not self.input_queue.full():
            self.input_queue.put({
                'frame': frame,
                'timestamp': time.time()
            })
    
    def get_results(self, timeout=1.0):
        """Get inference results"""
        try:
            return self.output_queue.get(timeout=timeout)
        except:
            return None
    
    def _inference_loop(self):
        """Main inference loop"""
        while self.is_running:
            try:
                # Get input
                data = self.input_queue.get(timeout=1.0)
                
                frame = data['frame']
                timestamp = data['timestamp']
                
                # Run inference
                results = self._run_inference(frame)
                
                # Add timestamp
                results['timestamp'] = timestamp
                results['latency'] = time.time() - timestamp
                
                # Put results
                if not self.output_queue.full():
                    self.output_queue.put(results)
                
            except:
                continue
    
    def _run_inference(self, frame):
        """Run all models on frame"""
        results = {}
        
        # Face detection
        if 'face_detector' in self.models:
            faces = self.models['face_detector'].detect_faces(frame)
            results['num_faces'] = len(faces)
            results['faces'] = faces
        
        # Object detection
        if 'object_detector' in self.models:
            objects = self.models['object_detector'].detect_objects(frame)
            results['objects'] = objects
            results['has_unauthorized_objects'] = len(objects) > 0
        
        # Pose analysis
        if 'pose_analyzer' in self.models:
            pose = self.models['pose_analyzer'].analyze_pose(frame)
            results['pose'] = pose
            if pose:
                results['looking_away'] = pose.get('is_looking_away', False)
        
        # Behavior analysis
        if 'behavior_detector' in self.models:
            behavior = self.models['behavior_detector'].analyze_frame(results)
            results['behavior'] = behavior
        
        return results

if __name__ == '__main__':
    models = {}
    pipeline = RealTimeInferencePipeline(models)
    print("Real-time inference pipeline initialized")
''',

    "ai-ml/pipelines/monitoring/model_monitoring.py": '''import numpy as np
from datetime import datetime
from collections import deque

class ModelMonitor:
    """Monitor model performance and data drift"""
    
    def __init__(self, model_name):
        self.model_name = model_name
        self.predictions_history = deque(maxlen=10000)
        self.metrics_history = deque(maxlen=1000)
        
        self.alert_thresholds = {
            'accuracy_drop': 0.1,
            'latency_increase': 2.0,
            'error_rate': 0.05
        }
    
    def log_prediction(self, input_data, prediction, ground_truth=None, latency=None):
        """Log a model prediction"""
        record = {
            'timestamp': datetime.now(),
            'input_shape': input_data.shape if hasattr(input_data, 'shape') else None,
            'prediction': prediction,
            'ground_truth': ground_truth,
            'latency': latency,
            'is_correct': ground_truth == prediction if ground_truth is not None else None
        }
        
        self.predictions_history.append(record)
    
    def calculate_metrics(self, window_size=100):
        """Calculate recent performance metrics"""
        recent = list(self.predictions_history)[-window_size:]
        
        if not recent:
            return {}
        
        # Accuracy
        correct = [r for r in recent if r.get('is_correct')]
        accuracy = len(correct) / len(recent) if recent else 0
        
        # Latency
        latencies = [r['latency'] for r in recent if r.get('latency')]
        avg_latency = np.mean(latencies) if latencies else 0
        p95_latency = np.percentile(latencies, 95) if latencies else 0
        
        # Prediction distribution
        predictions = [r['prediction'] for r in recent]
        unique_preds = set(predictions)
        
        metrics = {
            'timestamp': datetime.now(),
            'window_size': len(recent),
            'accuracy': accuracy,
            'avg_latency': avg_latency,
            'p95_latency': p95_latency,
            'prediction_diversity': len(unique_preds) / len(predictions) if predictions else 0
        }
        
        self.metrics_history.append(metrics)
        
        return metrics
    
    def detect_anomalies(self):
        """Detect anomalous behavior in model performance"""
        if len(self.metrics_history) < 10:
            return []
        
        recent_metrics = list(self.metrics_history)[-10:]
        anomalies = []
        
        # Check for accuracy drop
        recent_accuracy = [m['accuracy'] for m in recent_metrics]
        avg_accuracy = np.mean(recent_accuracy)
        
        if avg_accuracy < (1 - self.alert_thresholds['accuracy_drop']):
            anomalies.append({
                'type': 'accuracy_drop',
                'severity': 'high',
                'value': avg_accuracy,
                'message': f'Accuracy dropped to {avg_accuracy:.2f}'
            })
        
        # Check for latency increase
        recent_latency = [m['avg_latency'] for m in recent_metrics]
        avg_latency = np.mean(recent_latency)
        
        if len(self.metrics_history) > 20:
            historical_latency = np.mean([
                m['avg_latency']
                for m in list(self.metrics_history)[-20:-10]
            ])
            
            if avg_latency > historical_latency * self.alert_thresholds['latency_increase']:
                anomalies.append({
                    'type': 'latency_increase',
                    'severity': 'medium',
                    'value': avg_latency,
                    'message': f'Latency increased to {avg_latency:.3f}s'
                })
        
        return anomalies
    
    def generate_report(self):
        """Generate monitoring report"""
        metrics = self.calculate_metrics()
        anomalies = self.detect_anomalies()
        
        report = {
            'model_name': self.model_name,
            'report_time': datetime.now().isoformat(),
            'total_predictions': len(self.predictions_history),
            'recent_metrics': metrics,
            'anomalies': anomalies,
            'status': 'healthy' if not anomalies else 'warning'
        }
        
        return report

if __name__ == '__main__':
    monitor = ModelMonitor('face_recognition')
    print("Model monitor initialized")
''',

    # ==================== CONFIGS ====================
    
    "ai-ml/configs/model_configs/cv_models.yaml": '''# Computer Vision Models Configuration

face_detection:
  model_type: cnn
  input_shape: [224, 224, 3]
  architecture:
    - conv2d: {filters: 32, kernel: 3, activation: relu}
    - maxpool: {pool_size: 2}
    - conv2d: {filters: 64, kernel: 3, activation: relu}
    - maxpool: {pool_size: 2}
    - conv2d: {filters: 128, kernel: 3, activation: relu}
    - maxpool: {pool_size: 2}
    - flatten: {}
    - dense: {units: 512, activation: relu}
    - dropout: {rate: 0.5}
    - dense: {units: 1, activation: sigmoid}
  
  training:
    optimizer: adam
    learning_rate: 0.001
    loss: binary_crossentropy
    metrics: [accuracy]
    batch_size: 32
    epochs: 50

face_recognition:
  model_type: resnet50
  input_shape: [224, 224, 3]
  num_classes: 1000
  pretrained: imagenet
  
  fine_tuning:
    freeze_layers: 140
    trainable_layers: 10
  
  training:
    optimizer: adam
    learning_rate: 0.0001
    loss: categorical_crossentropy
    metrics: [accuracy, top_5_accuracy]
    batch_size: 16
    epochs: 100

object_detection:
  model_type: yolo_v5
  input_shape: [640, 640, 3]
  classes:
    - cell_phone
    - book
    - calculator
    - laptop
    - tablet
  
  confidence_threshold: 0.5
  nms_threshold: 0.4
  
  training:
    optimizer: sgd
    learning_rate: 0.01
    momentum: 0.9
    weight_decay: 0.0005
    batch_size: 16
    epochs: 300

pose_estimation:
  model_type: mediapipe
  min_detection_confidence: 0.5
  min_tracking_confidence: 0.5
  model_complexity: 1
''',

    "ai-ml/configs/model_configs/nlp_models.yaml": '''# NLP Models Configuration

question_generation:
  model_type: t5
  model_name: t5-base
  max_input_length: 512
  max_output_length: 128
  
  generation_params:
    num_beams: 5
    temperature: 0.8
    top_k: 50
    top_p: 0.95
    do_sample: true
    num_return_sequences: 3
  
  training:
    optimizer: adamw
    learning_rate: 0.0001
    warmup_steps: 500
    weight_decay: 0.01
    batch_size: 4
    epochs: 10

answer_evaluation:
  model_type: sentence_transformer
  model_name: all-MiniLM-L6-v2
  max_length: 512
  
  similarity_thresholds:
    correct: 0.9
    partially_correct: 0.7
    needs_improvement: 0.5
  
  training:
    optimizer: adam
    learning_rate: 0.00002
    batch_size: 16
    epochs: 5

multilingual_support:
  languages:
    - en
    - hi
    - ta
    - te
    - kn
    - ml
  
  model_type: mbert
  model_name: bert-base-multilingual-cased
  
  translation:
    model: m2m100
    max_length: 512
''',

    "ai-ml/configs/training_configs/hyperparameters.yaml": '''# Hyperparameters Configuration

computer_vision:
  learning_rate: 0.001
  batch_size: 32
  epochs: 50
  optimizer: adam
  weight_decay: 0.0001
  
  augmentation:
    rotation_range: 20
    width_shift_range: 0.2
    height_shift_range: 0.2
    horizontal_flip: true
    zoom_range: 0.2

natural_language_processing:
  learning_rate: 0.0001
  batch_size: 16
  epochs: 10
  optimizer: adamw
  warmup_steps: 500
  weight_decay: 0.01
  
  max_sequence_length: 512
  gradient_accumulation_steps: 4

machine_learning:
  adaptive_testing:
    min_questions: 10
    max_questions: 30
    precision_threshold: 0.3
    ability_range: [-3, 3]
  
  recommendation:
    num_recommendations: 5
    similarity_threshold: 0.6
    cold_start_strategy: popular
  
  anomaly_detection:
    contamination: 0.1
    n_estimators: 100
    max_samples: 256

callbacks:
  early_stopping:
    patience: 5
    restore_best_weights: true
    monitor: val_loss
  
  reduce_lr:
    patience: 3
    factor: 0.5
    min_lr: 0.000001
  
  model_checkpoint:
    save_best_only: true
    monitor: val_accuracy
''',

    # ==================== UTILS ====================
    
    "ai-ml/utils/data_utils.py": '''import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class DataUtils:
    """Utility functions for data processing"""
    
    @staticmethod
    def load_indian_states_data(filepath):
        """Load Indian states knowledge base"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    @staticmethod
    def split_data(X, y, test_size=0.2, val_size=0.1, random_state=42):
        """Split data into train, validation, and test sets"""
        # First split: train+val and test
        X_temp, X_test, y_temp, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        
        # Second split: train and val
        val_ratio = val_size / (1 - test_size)
        X_train, X_val, y_train, y_val = train_test_split(
            X_temp, y_temp, test_size=val_ratio, random_state=random_state
        )
        
        return X_train, X_val, X_test, y_train, y_val, y_test
    
    @staticmethod
    def normalize_features(X, method='standard'):
        """Normalize features"""
        if method == 'standard':
            mean = np.mean(X, axis=0)
            std = np.std(X, axis=0)
            X_normalized = (X - mean) / (std + 1e-8)
        elif method == 'minmax':
            min_val = np.min(X, axis=0)
            max_val = np.max(X, axis=0)
            X_normalized = (X - min_val) / (max_val - min_val + 1e-8)
        else:
            X_normalized = X
        
        return X_normalized
    
    @staticmethod
    def balance_dataset(X, y, method='oversample'):
        """Balance imbalanced dataset"""
        unique, counts = np.unique(y, return_counts=True)
        
        if method == 'oversample':
            max_count = max(counts)
            X_balanced = []
            y_balanced = []
            
            for cls in unique:
                cls_indices = np.where(y == cls)[0]
                cls_X = X[cls_indices]
                cls_y = y[cls_indices]
                
                # Oversample to max_count
                if len(cls_indices) < max_count:
                    indices = np.random.choice(
                        cls_indices,
                        size=max_count,
                        replace=True
                    )
                    cls_X = X[indices]
                    cls_y = y[indices]
                
                X_balanced.append(cls_X)
                y_balanced.append(cls_y)
            
            X_balanced = np.vstack(X_balanced)
            y_balanced = np.concatenate(y_balanced)
            
            # Shuffle
            indices = np.random.permutation(len(X_balanced))
            X_balanced = X_balanced[indices]
            y_balanced = y_balanced[indices]
            
            return X_balanced, y_balanced
        
        return X, y

if __name__ == '__main__':
    print("Data utils module loaded")
''',

    "ai-ml/utils/evaluation_metrics.py": '''import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.metrics import confusion_matrix, roc_auc_score

class EvaluationMetrics:
    """Comprehensive evaluation metrics for models"""
    
    @staticmethod
    def classification_metrics(y_true, y_pred, y_prob=None):
        """Calculate classification metrics"""
        accuracy = accuracy_score(y_true, y_pred)
        
        precision, recall, f1, support = precision_recall_fscore_support(
            y_true, y_pred, average='weighted'
        )
        
        cm = confusion_matrix(y_true, y_pred)
        
        metrics = {
            'accuracy': float(accuracy),
            'precision': float(precision),
            'recall': float(recall),
            'f1_score': float(f1),
            'confusion_matrix': cm.tolist()
        }
        
        # Add ROC-AUC if probabilities provided
        if y_prob is not None:
            try:
                if len(np.unique(y_true)) == 2:
                    auc = roc_auc_score(y_true, y_prob)
                else:
                    auc = roc_auc_score(y_true, y_prob, multi_class='ovr')
                metrics['roc_auc'] = float(auc)
            except:
                pass
        
        return metrics
    
    @staticmethod
    def regression_metrics(y_true, y_pred):
        """Calculate regression metrics"""
        mse = np.mean((y_true - y_pred) ** 2)
        rmse = np.sqrt(mse)
        mae = np.mean(np.abs(y_true - y_pred))
        
        # R² score
        ss_res = np.sum((y_true - y_pred) ** 2)
        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        r2 = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
        
        return {
            'mse': float(mse),
            'rmse': float(rmse),
            'mae': float(mae),
            'r2_score': float(r2)
        }
    
    @staticmethod
    def ranking_metrics(y_true, y_scores, k=5):
        """Calculate ranking metrics (for recommendations)"""
        # Mean Reciprocal Rank
        reciprocal_ranks = []
        for true_items, scores in zip(y_true, y_scores):
            # Get top k recommendations
            top_k_indices = np.argsort(scores)[-k:][::-1]
            
            # Find rank of first relevant item
            for rank, idx in enumerate(top_k_indices, 1):
                if idx in true_items:
                    reciprocal_ranks.append(1.0 / rank)
                    break
            else:
                reciprocal_ranks.append(0.0)
        
        mrr = np.mean(reciprocal_ranks)
        
        # Precision@K and Recall@K
        precisions = []
        recalls = []
        
        for true_items, scores in zip(y_true, y_scores):
            top_k_indices = np.argsort(scores)[-k:][::-1]
            
            relevant_in_top_k = len(set(top_k_indices) & set(true_items))
            
            precision = relevant_in_top_k / k
            recall = relevant_in_top_k / len(true_items) if true_items else 0
            
            precisions.append(precision)
            recalls.append(recall)
        
        return {
            'mrr': float(mrr),
            f'precision@{k}': float(np.mean(precisions)),
            f'recall@{k}': float(np.mean(recalls))
        }

if __name__ == '__main__':
    print("Evaluation metrics module loaded")
''',

    # Continue with requirements.txt
    "ai-ml/requirements.txt": '''# Core ML/DL Frameworks
tensorflow==2.13.0
torch==2.0.1
transformers==4.33.0
scikit-learn==1.3.0

# Computer Vision
opencv-python==4.8.0.76
mediapipe==0.10.3
pillow==10.0.0

# NLP
nltk==3.8.1
spacy==3.6.1
sentencepiece==0.1.99

# Data Processing
numpy==1.24.3
pandas==2.0.3
scipy==1.11.2

# Utilities
pyyaml==6.0.1
tqdm==4.66.1
joblib==1.3.2

# Monitoring
tensorboard==2.13.0
mlflow==2.6.0

# API
fastapi==0.103.1
uvicorn==0.23.2
pydantic==2.3.0
''',
}

print(f"🚀 Generating {len(AI_ML_PART2_FILES)} additional AI/ML files...")
for filepath, content in AI_ML_PART2_FILES.items():
    create_file(filepath, content)

print(f"\n✅ Successfully created {len(AI_ML_PART2_FILES)} files!")
print("\n🤖 Created Components:")
print("  ✅ ML - Adaptive Testing Engine")
print("  ✅ ML - Recommendation Engine")
print("  ✅ ML - Anomaly Detection")
print("  ✅ Pipelines - Training & Inference")
print("  ✅ Pipelines - Model Monitoring")
print("  ✅ Configs - Models & Hyperparameters")
print("  ✅ Utils - Data & Evaluation")
print("  ✅ requirements.txt with all dependencies")
print("\n🎉 AI/ML Suite Part 2 Complete!")
