import pandas as pd
import numpy as np
from src.config import INV_LABEL_MAP
from src.utils import load_model, load_preprocessor, load_metadata

def load_inference_artifacts():
    model = load_model(str(load_model.__defaults__[0]) if hasattr(load_model, '__defaults__') and load_model.__defaults__ else 'models/trained_model.pkl') # will use correct paths below
    pass # just a dummy function call, writing actual logic below

def run_prediction(df, model_path, preprocessor_path, metadata_path):
    model = load_model(model_path)
    preprocessor = load_preprocessor(preprocessor_path)
    metadata = load_metadata(metadata_path)
    
    if model is None or preprocessor is None or metadata is None:
        raise ValueError("Model artifacts not found. Please train a model first.")
        
    features = metadata['features']
    
    # Fill missing features with nan
    for f in features:
        if f not in df.columns:
            df[f] = np.nan
            
    X = df[features]
    X_processed = preprocessor.transform(X)
    
    preds = model.predict(X_processed)
    probs = model.predict_proba(X_processed)
    
    pred_labels = [INV_LABEL_MAP.get(p, "Unknown") for p in preds]
    max_probs = np.max(probs, axis=1) * 100
    
    results = df.copy()
    results['Predicted_Class'] = pred_labels
    results['Confidence_%'] = max_probs.round(2)
    
    # Add probabilities for all classes
    for k, v in INV_LABEL_MAP.items():
        if k < probs.shape[1]:
            results[f'Prob_{v}_%'] = (probs[:, k] * 100).round(2)
            
    return results
