import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class DataUtils:
    """Utility functions for data processing"""
    
    @staticmethod
    def load_indian_states_data(filepath):
        """Load Indian states knowledge base"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    
    @staticmethod
    def split_data(X, y, test_size=0.2, val_size=0.1, random_state=42):
        """Split data into train, validation, and test sets"""
        # First split: train+val and test
        X_temp, X_test, y_temp, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        
        # Second split: train and val
        val_ratio = val_size / (1 - test_size)
        X_train, X_val, y_train, y_val = train_test_split(
            X_temp, y_temp, test_size=val_ratio, random_state=random_state
        )
        
        return X_train, X_val, X_test, y_train, y_val, y_test
    
    @staticmethod
    def normalize_features(X, method='standard'):
        """Normalize features"""
        if method == 'standard':
            mean = np.mean(X, axis=0)
            std = np.std(X, axis=0)
            X_normalized = (X - mean) / (std + 1e-8)
        elif method == 'minmax':
            min_val = np.min(X, axis=0)
            max_val = np.max(X, axis=0)
            X_normalized = (X - min_val) / (max_val - min_val + 1e-8)
        else:
            X_normalized = X
        
        return X_normalized
    
    @staticmethod
    def balance_dataset(X, y, method='oversample'):
        """Balance imbalanced dataset"""
        unique, counts = np.unique(y, return_counts=True)
        
        if method == 'oversample':
            max_count = max(counts)
            X_balanced = []
            y_balanced = []
            
            for cls in unique:
                cls_indices = np.where(y == cls)[0]
                cls_X = X[cls_indices]
                cls_y = y[cls_indices]
                
                # Oversample to max_count
                if len(cls_indices) < max_count:
                    indices = np.random.choice(
                        cls_indices,
                        size=max_count,
                        replace=True
                    )
                    cls_X = X[indices]
                    cls_y = y[indices]
                
                X_balanced.append(cls_X)
                y_balanced.append(cls_y)
            
            X_balanced = np.vstack(X_balanced)
            y_balanced = np.concatenate(y_balanced)
            
            # Shuffle
            indices = np.random.permutation(len(X_balanced))
            X_balanced = X_balanced[indices]
            y_balanced = y_balanced[indices]
            
            return X_balanced, y_balanced
        
        return X, y

if __name__ == '__main__':
    print("Data utils module loaded")
