import numpy as np
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
