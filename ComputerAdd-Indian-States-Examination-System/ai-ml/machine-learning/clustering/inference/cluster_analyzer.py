import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

class ClusterAnalyzer:
    """Analyze and interpret student clusters"""
    
    def __init__(self, n_clusters=5):
        self.n_clusters = n_clusters
        self.model = KMeans(n_clusters=n_clusters, random_state=42)
        self.pca = PCA(n_components=2)
    
    def fit(self, features):
        """Fit clustering model"""
        self.model.fit(features)
        return self
    
    def predict(self, features):
        """Predict cluster for new data"""
        return self.model.predict(features)
    
    def analyze_clusters(self, features, labels):
        """Analyze cluster characteristics"""
        cluster_stats = []
        
        for i in range(self.n_clusters):
            cluster_data = features[labels == i]
            
            stats = {
                'cluster_id': i,
                'size': len(cluster_data),
                'centroid': self.model.cluster_centers_[i].tolist(),
                'mean': np.mean(cluster_data, axis=0).tolist(),
                'std': np.std(cluster_data, axis=0).tolist()
            }
            
            cluster_stats.append(stats)
        
        return cluster_stats
    
    def get_cluster_profiles(self, labels, student_data):
        """Generate profiles for each cluster"""
        profiles = {}
        
        for i in range(self.n_clusters):
            cluster_students = [s for j, s in enumerate(student_data) if labels[j] == i]
            
            profiles[i] = {
                'description': self._generate_description(cluster_students),
                'characteristics': self._extract_characteristics(cluster_students),
                'recommendations': self._generate_recommendations(cluster_students)
            }
        
        return profiles
    
    def _generate_description(self, students):
        """Generate human-readable cluster description"""
        if not students:
            return "Empty cluster"
        
        avg_score = np.mean([s.get('avg_score', 0) for s in students])
        
        if avg_score >= 80:
            return "High performers"
        elif avg_score >= 60:
            return "Average performers"
        else:
            return "Needs improvement"
    
    def _extract_characteristics(self, students):
        """Extract common characteristics"""
        return {
            'avg_score': np.mean([s.get('avg_score', 0) for s in students]),
            'avg_time': np.mean([s.get('avg_time', 0) for s in students]),
            'completion_rate': np.mean([s.get('completion_rate', 0) for s in students])
        }
    
    def _generate_recommendations(self, students):
        """Generate recommendations for cluster"""
        char = self._extract_characteristics(students)
        
        recommendations = []
        
        if char['avg_score'] < 60:
            recommendations.append("Focus on fundamental concepts")
            recommendations.append("Provide additional practice materials")
        
        if char['completion_rate'] < 0.7:
            recommendations.append("Improve engagement strategies")
        
        return recommendations
