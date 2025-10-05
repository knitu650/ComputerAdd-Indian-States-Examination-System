import numpy as np
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
