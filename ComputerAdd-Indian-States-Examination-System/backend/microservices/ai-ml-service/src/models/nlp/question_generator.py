from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
from typing import List, Dict

class QuestionGenerator:
    def __init__(self, model_name: str = "t5-base"):
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
    
    def generate_questions(self, context: str, num_questions: int = 5, 
                          question_type: str = "factual") -> List[Dict]:
        """Generate questions from given context"""
        
        # Prepare input
        input_text = f"generate {question_type} questions: {context}"
        input_ids = self.tokenizer.encode(
            input_text, 
            return_tensors="pt", 
            max_length=512,
            truncation=True
        ).to(self.device)
        
        # Generate questions
        outputs = self.model.generate(
            input_ids,
            max_length=200,
            num_return_sequences=num_questions,
            num_beams=5,
            early_stopping=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95
        )
        
        questions = []
        for output in outputs:
            question = self.tokenizer.decode(output, skip_special_tokens=True)
            questions.append({
                "question": question,
                "type": question_type,
                "context": context[:100] + "..."
            })
        
        return questions
    
    def generate_distractors(self, question: str, correct_answer: str, 
                            num_distractors: int = 3) -> List[str]:
        """Generate distractor options for MCQ"""
        
        input_text = f"generate distractors for question: {question} with answer: {correct_answer}"
        input_ids = self.tokenizer.encode(
            input_text,
            return_tensors="pt",
            max_length=256,
            truncation=True
        ).to(self.device)
        
        outputs = self.model.generate(
            input_ids,
            max_length=100,
            num_return_sequences=num_distractors,
            num_beams=num_distractors + 2,
            temperature=0.9
        )
        
        distractors = []
        for output in outputs:
            distractor = self.tokenizer.decode(output, skip_special_tokens=True)
            distractors.append(distractor)
        
        return distractors
    
    def generate_state_questions(self, state_name: str, category: str = "geography") -> List[Dict]:
        """Generate questions specific to Indian states"""
        
        templates = {
            "geography": f"Generate geography questions about {state_name}, India",
            "history": f"Generate historical questions about {state_name}, India",
            "culture": f"Generate cultural questions about {state_name}, India",
            "economy": f"Generate economy-related questions about {state_name}, India"
        }
        
        context = templates.get(category, templates["geography"])
        return self.generate_questions(context, num_questions=5)
