import re
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

class TextProcessor:
    """Text processing utilities"""
    
    def __init__(self):
        try:
            self.stop_words = set(stopwords.words('english'))
        except:
            self.stop_words = set()
    
    def clean_text(self, text):
        """Clean and normalize text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove special characters (keep punctuation)
        text = re.sub(r'[^\w\s.,!?-]', '', text)
        
        return text.strip()
    
    def tokenize_sentences(self, text):
        """Split text into sentences"""
        return sent_tokenize(text)
    
    def tokenize_words(self, text):
        """Split text into words"""
        return word_tokenize(text)
    
    def remove_stopwords(self, tokens):
        """Remove stopwords from token list"""
        return [t for t in tokens if t.lower() not in self.stop_words]
    
    def extract_keywords(self, text, top_k=5):
        """Extract key terms from text"""
        # Simple frequency-based extraction
        tokens = self.tokenize_words(text.lower())
        tokens = self.remove_stopwords(tokens)
        
        # Count frequencies
        freq = {}
        for token in tokens:
            if token not in string.punctuation:
                freq[token] = freq.get(token, 0) + 1
        
        # Sort by frequency
        sorted_terms = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        return [term for term, _ in sorted_terms[:top_k]]
    
    def normalize_answer(self, answer):
        """Normalize answer for comparison"""
        # Convert to lowercase
        answer = answer.lower()
        
        # Remove punctuation
        answer = answer.translate(str.maketrans('', '', string.punctuation))
        
        # Remove extra whitespace
        answer = ' '.join(answer.split())
        
        return answer
