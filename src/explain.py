import pandas as pd
import numpy as np

def get_feature_importances(model, preprocessor, metadata):
    try:
        if hasattr(model, 'feature_importances_'):
            importances = model.feature_importances_
        else:
            return None
            
        # Get feature names from preprocessor if possible
        feature_names = []
        if hasattr(preprocessor, 'transformers_'):
            for name, transformer, cols in preprocessor.transformers_:
                if name == 'num':
                    feature_names.extend(cols)
                elif name == 'cat':
                    if hasattr(transformer.named_steps['onehot'], 'get_feature_names_out'):
                        cat_feats = transformer.named_steps['onehot'].get_feature_names_out(cols)
                        feature_names.extend(cat_feats)
                    else:
                        feature_names.extend([f"Cat_{i}" for i in range(len(cols))]) # Fallback
        else:
            feature_names = [f"Feature_{i}" for i in range(len(importances))]
            
        # Match lengths just in case
        min_len = min(len(importances), len(feature_names))
        
        fi_df = pd.DataFrame({
            'Feature': feature_names[:min_len],
            'Importance': importances[:min_len]
        }).sort_values('Importance', ascending=False)
        
        return fi_df
    except Exception as e:
        print(f"Error calculating feature importances: {e}")
        return None
