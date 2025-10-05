from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class AnswerEvaluator:
    """Evaluate student answers using semantic similarity"""
    
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        self.model.eval()
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
    
    def get_embedding(self, text):
        """Get sentence embedding"""
        inputs = self.tokenizer(
            text,
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors='pt'
        ).to(self.device)
        
        with torch.no_grad():
            outputs = self.model(**inputs)
            # Mean pooling
            embeddings = outputs.last_hidden_state.mean(dim=1)
        
        return embeddings.cpu().numpy()
    
    def evaluate_answer(self, student_answer, correct_answer, partial_credit=True):
        """
        Evaluate student answer against correct answer
        
        Args:
            student_answer: Student's answer text
            correct_answer: Correct answer text
            partial_credit: Whether to give partial credit
            
        Returns:
            Dict with score and explanation
        """
        # Get embeddings
        student_emb = self.get_embedding(student_answer)
        correct_emb = self.get_embedding(correct_answer)
        
        # Calculate similarity
        similarity = cosine_similarity(student_emb, correct_emb)[0][0]
        
        # Determine score
        if similarity >= 0.9:
            score = 1.0
            verdict = 'Correct'
        elif similarity >= 0.7 and partial_credit:
            score = 0.7
            verdict = 'Partially Correct'
        elif similarity >= 0.5 and partial_credit:
            score = 0.5
            verdict = 'Needs Improvement'
        else:
            score = 0.0
            verdict = 'Incorrect'
        
        return {
            'score': score,
            'verdict': verdict,
            'similarity': float(similarity),
            'student_answer': student_answer,
            'correct_answer': correct_answer
        }
    
    def batch_evaluate(self, student_answers, correct_answers):
        """Evaluate multiple answers"""
        results = []
        
        for student_ans, correct_ans in zip(student_answers, correct_answers):
            result = self.evaluate_answer(student_ans, correct_ans)
            results.append(result)
        
        return results

if __name__ == '__main__':
    evaluator = AnswerEvaluator()
    
    result = evaluator.evaluate_answer(
        "The capital of Andhra Pradesh is Amaravati",
        "Amaravati is the capital city of Andhra Pradesh"
    )
    
    print("Evaluation result:", result)
