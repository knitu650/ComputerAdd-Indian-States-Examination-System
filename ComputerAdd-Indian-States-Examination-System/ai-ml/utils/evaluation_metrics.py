import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.metrics import confusion_matrix, roc_auc_score

class EvaluationMetrics:
    """Comprehensive evaluation metrics for models"""
    
    @staticmethod
    def classification_metrics(y_true, y_pred, y_prob=None):
        """Calculate classification metrics"""
        accuracy = accuracy_score(y_true, y_pred)
        
        precision, recall, f1, support = precision_recall_fscore_support(
            y_true, y_pred, average='weighted'
        )
        
        cm = confusion_matrix(y_true, y_pred)
        
        metrics = {
            'accuracy': float(accuracy),
            'precision': float(precision),
            'recall': float(recall),
            'f1_score': float(f1),
            'confusion_matrix': cm.tolist()
        }
        
        # Add ROC-AUC if probabilities provided
        if y_prob is not None:
            try:
                if len(np.unique(y_true)) == 2:
                    auc = roc_auc_score(y_true, y_prob)
                else:
                    auc = roc_auc_score(y_true, y_prob, multi_class='ovr')
                metrics['roc_auc'] = float(auc)
            except:
                pass
        
        return metrics
    
    @staticmethod
    def regression_metrics(y_true, y_pred):
        """Calculate regression metrics"""
        mse = np.mean((y_true - y_pred) ** 2)
        rmse = np.sqrt(mse)
        mae = np.mean(np.abs(y_true - y_pred))
        
        # R² score
        ss_res = np.sum((y_true - y_pred) ** 2)
        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        r2 = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
        
        return {
            'mse': float(mse),
            'rmse': float(rmse),
            'mae': float(mae),
            'r2_score': float(r2)
        }
    
    @staticmethod
    def ranking_metrics(y_true, y_scores, k=5):
        """Calculate ranking metrics (for recommendations)"""
        # Mean Reciprocal Rank
        reciprocal_ranks = []
        for true_items, scores in zip(y_true, y_scores):
            # Get top k recommendations
            top_k_indices = np.argsort(scores)[-k:][::-1]
            
            # Find rank of first relevant item
            for rank, idx in enumerate(top_k_indices, 1):
                if idx in true_items:
                    reciprocal_ranks.append(1.0 / rank)
                    break
            else:
                reciprocal_ranks.append(0.0)
        
        mrr = np.mean(reciprocal_ranks)
        
        # Precision@K and Recall@K
        precisions = []
        recalls = []
        
        for true_items, scores in zip(y_true, y_scores):
            top_k_indices = np.argsort(scores)[-k:][::-1]
            
            relevant_in_top_k = len(set(top_k_indices) & set(true_items))
            
            precision = relevant_in_top_k / k
            recall = relevant_in_top_k / len(true_items) if true_items else 0
            
            precisions.append(precision)
            recalls.append(recall)
        
        return {
            'mrr': float(mrr),
            f'precision@{k}': float(np.mean(precisions)),
            f'recall@{k}': float(np.mean(recalls))
        }

if __name__ == '__main__':
    print("Evaluation metrics module loaded")
