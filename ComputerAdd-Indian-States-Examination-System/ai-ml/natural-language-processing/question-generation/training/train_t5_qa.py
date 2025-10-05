from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import Trainer, TrainingArguments
import torch
from torch.utils.data import Dataset

class QuestionGenerationDataset(Dataset):
    """Dataset for question generation training"""
    
    def __init__(self, contexts, questions, tokenizer, max_length=512):
        self.contexts = contexts
        self.questions = questions
        self.tokenizer = tokenizer
        self.max_length = max_length
    
    def __len__(self):
        return len(self.contexts)
    
    def __getitem__(self, idx):
        context = self.contexts[idx]
        question = self.questions[idx]
        
        # Prepare input: "generate question: <context>"
        input_text = f"generate question: {context}"
        
        input_encoding = self.tokenizer(
            input_text,
            max_length=self.max_length,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        
        target_encoding = self.tokenizer(
            question,
            max_length=128,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        
        return {
            'input_ids': input_encoding['input_ids'].squeeze(),
            'attention_mask': input_encoding['attention_mask'].squeeze(),
            'labels': target_encoding['input_ids'].squeeze()
        }

class T5QuestionGeneratorTrainer:
    """Train T5 model for question generation"""
    
    def __init__(self, model_name='t5-base'):
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name)
    
    def train(self, train_contexts, train_questions, val_contexts, val_questions):
        """Train the model"""
        train_dataset = QuestionGenerationDataset(
            train_contexts, train_questions, self.tokenizer
        )
        
        val_dataset = QuestionGenerationDataset(
            val_contexts, val_questions, self.tokenizer
        )
        
        training_args = TrainingArguments(
            output_dir='./results',
            num_train_epochs=10,
            per_device_train_batch_size=4,
            per_device_eval_batch_size=4,
            warmup_steps=500,
            weight_decay=0.01,
            logging_dir='./logs',
            logging_steps=100,
            evaluation_strategy='epoch',
            save_strategy='epoch',
            load_best_model_at_end=True
        )
        
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset
        )
        
        trainer.train()
        
        return trainer
    
    def save_model(self, path='models/t5_qa_generator'):
        """Save trained model"""
        self.model.save_pretrained(path)
        self.tokenizer.save_pretrained(path)

if __name__ == '__main__':
    trainer = T5QuestionGeneratorTrainer()
    print("T5 Question Generator trainer initialized")
