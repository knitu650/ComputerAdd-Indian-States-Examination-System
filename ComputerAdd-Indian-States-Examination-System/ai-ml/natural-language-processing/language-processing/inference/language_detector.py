from collections import Counter
import re

class LanguageDetector:
    """Detect language of text"""
    
    def __init__(self):
        # Character ranges for Indian scripts
        self.language_patterns = {
            'hindi': r'[ऀ-ॿ]',
            'tamil': r'[஀-௿]',
            'telugu': r'[ఀ-౿]',
            'kannada': r'[ಀ-೿]',
            'malayalam': r'[ഀ-ൿ]',
            'gujarati': r'[઀-૿]',
            'bengali': r'[ঀ-৿]',
            'punjabi': r'[਀-੿]'
        }
    
    def detect_language(self, text):
        """
        Detect language of text
        
        Returns:
            (language, confidence)
        """
        if not text:
            return 'unknown', 0.0
        
        # Check for English (ASCII characters)
        ascii_ratio = sum(ord(c) < 128 for c in text) / len(text)
        if ascii_ratio > 0.9:
            return 'english', ascii_ratio
        
        # Check for Indian languages
        scores = {}
        for lang, pattern in self.language_patterns.items():
            matches = len(re.findall(pattern, text))
            scores[lang] = matches / len(text)
        
        if scores:
            best_lang = max(scores.items(), key=lambda x: x[1])
            if best_lang[1] > 0.5:
                return best_lang[0], best_lang[1]
        
        return 'unknown', 0.0
    
    def is_multilingual(self, text):
        """Check if text contains multiple languages"""
        detected_langs = []
        
        for lang, pattern in self.language_patterns.items():
            if re.search(pattern, text):
                detected_langs.append(lang)
        
        return len(detected_langs) > 1, detected_langs
