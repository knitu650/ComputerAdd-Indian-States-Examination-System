from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import random

class QuestionGenerator:
    """Generate questions from context using T5"""
    
    def __init__(self, model_path='models/t5_qa_generator'):
        self.tokenizer = T5Tokenizer.from_pretrained(model_path)
        self.model = T5ForConditionalGeneration.from_pretrained(model_path)
        self.model.eval()
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
    
    def generate_question(self, context, max_length=128, num_questions=1):
        """
        Generate questions from context
        
        Args:
            context: Text context
            max_length: Max length of generated question
            num_questions: Number of questions to generate
            
        Returns:
            List of generated questions
        """
        input_text = f"generate question: {context}"
        
        input_ids = self.tokenizer(
            input_text,
            max_length=512,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        ).input_ids.to(self.device)
        
        outputs = self.model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=num_questions,
            num_beams=5,
            temperature=0.8,
            top_k=50,
            top_p=0.95,
            do_sample=True
        )
        
        questions = [
            self.tokenizer.decode(output, skip_special_tokens=True)
            for output in outputs
        ]
        
        return questions
    
    def generate_mcq_question(self, context, answer):
        """
        Generate MCQ question with answer
        
        Returns:
            Dict with question and answer
        """
        questions = self.generate_question(context, num_questions=1)
        question = questions[0] if questions else "What is the correct answer?"
        
        return {
            'question': question,
            'answer': answer,
            'context': context
        }
    
    def batch_generate(self, contexts, batch_size=8):
        """Generate questions for multiple contexts"""
        questions = []
        
        for i in range(0, len(contexts), batch_size):
            batch = contexts[i:i+batch_size]
            
            for context in batch:
                qs = self.generate_question(context, num_questions=1)
                questions.extend(qs)
        
        return questions

if __name__ == '__main__':
    generator = QuestionGenerator()
    
    # Example
    context = "Andhra Pradesh is a state in southern India. Its capital is Amaravati."
    questions = generator.generate_question(context)
    print("Generated questions:", questions)
