import random
import numpy as np
from transformers import pipeline
import nltk
from nltk.corpus import wordnet

class DistractorGenerator:
    """Generate distractors (wrong options) for MCQ questions"""
    
    def __init__(self):
        # Download required NLTK data
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet')
        
        self.similarity_threshold = 0.6
    
    def generate_distractors(self, correct_answer, context, num_distractors=3):
        """
        Generate distractors for a correct answer
        
        Args:
            correct_answer: The correct answer
            context: Context/question text
            num_distractors: Number of distractors to generate
            
        Returns:
            List of distractors
        """
        distractors = []
        
        # Method 1: WordNet synonyms/related words
        wordnet_distractors = self._get_wordnet_distractors(correct_answer)
        distractors.extend(wordnet_distractors[:num_distractors])
        
        # Method 2: Similar entities from context
        if len(distractors) < num_distractors:
            context_distractors = self._get_context_distractors(
                correct_answer, context
            )
            distractors.extend(context_distractors)
        
        # Method 3: Common wrong answers (domain-specific)
        if len(distractors) < num_distractors:
            common_distractors = self._get_common_distractors(correct_answer)
            distractors.extend(common_distractors)
        
        # Remove duplicates and the correct answer
        distractors = list(set(distractors))
        distractors = [d for d in distractors if d.lower() != correct_answer.lower()]
        
        # Shuffle and return requested number
        random.shuffle(distractors)
        return distractors[:num_distractors]
    
    def _get_wordnet_distractors(self, answer):
        """Get distractors using WordNet"""
        distractors = []
        
        # Get synsets for the answer
        synsets = wordnet.synsets(answer.replace(' ', '_'))
        
        for synset in synsets[:3]:  # Check first 3 synsets
            # Get hypernyms (broader terms)
            for hypernym in synset.hypernyms():
                for lemma in hypernym.lemmas()[:2]:
                    name = lemma.name().replace('_', ' ')
                    if name != answer:
                        distractors.append(name)
            
            # Get hyponyms (more specific terms)
            for hyponym in synset.hyponyms()[:2]:
                for lemma in hyponym.lemmas()[:1]:
                    name = lemma.name().replace('_', ' ')
                    if name != answer:
                        distractors.append(name)
        
        return distractors
    
    def _get_context_distractors(self, answer, context):
        """Extract similar entities from context"""
        # Simple extraction based on proper nouns and capitalized words
        words = context.split()
        
        potential_distractors = []
        for i, word in enumerate(words):
            if word[0].isupper() and word.lower() != answer.lower():
                # Check if it's part of a multi-word entity
                entity = word
                j = i + 1
                while j < len(words) and words[j][0].isupper():
                    entity += ' ' + words[j]
                    j += 1
                
                if entity != answer:
                    potential_distractors.append(entity)
        
        return potential_distractors
    
    def _get_common_distractors(self, answer):
        """Get common distractors for Indian states questions"""
        # Indian state capitals (common distractors)
        indian_capitals = [
            'New Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore',
            'Hyderabad', 'Ahmedabad', 'Pune', 'Jaipur', 'Lucknow',
            'Chandigarh', 'Bhopal', 'Thiruvananthapuram', 'Patna'
        ]
        
        # State names
        indian_states = [
            'Maharashtra', 'Karnataka', 'Tamil Nadu', 'Andhra Pradesh',
            'Kerala', 'Gujarat', 'Rajasthan', 'Uttar Pradesh', 'Bihar',
            'West Bengal', 'Madhya Pradesh', 'Punjab', 'Haryana'
        ]
        
        # Combine and filter
        all_options = indian_capitals + indian_states
        distractors = [opt for opt in all_options if opt != answer]
        
        return random.sample(distractors, min(5, len(distractors)))

if __name__ == '__main__':
    generator = DistractorGenerator()
    
    answer = "Amaravati"
    context = "Andhra Pradesh is a state in southern India. Its capital is Amaravati."
    
    distractors = generator.generate_distractors(answer, context)
    print(f"Correct Answer: {answer}")
    print(f"Distractors: {distractors}")
