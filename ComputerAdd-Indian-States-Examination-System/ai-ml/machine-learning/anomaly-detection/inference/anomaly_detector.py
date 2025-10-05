import numpy as np
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
