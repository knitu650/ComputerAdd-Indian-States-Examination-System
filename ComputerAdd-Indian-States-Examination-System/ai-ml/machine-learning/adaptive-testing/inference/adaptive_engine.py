import numpy as np
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
