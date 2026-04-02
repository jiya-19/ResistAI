import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from src.config import *
from src.preprocess import create_preprocessor, preprocess_target
from src.utils import save_model, save_preprocessor, save_metadata, clean_dataframe
from src.evaluate import evaluate_model
import time

try:
    from xgboost import XGBClassifier
    XGB_AVAILABLE = True
except ImportError:
    XGB_AVAILABLE = False

def train_pipeline(df, target_col, model_type="RandomForest", ignore_cols=None, test_size=0.2):
    start_time = time.time()
    
    # Clean df
    df = clean_dataframe(df, target_col)
    
    # Map target
    df = preprocess_target(df, target_col)
    
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    # Define ignore columns
    if ignore_cols is None:
        ignore_cols = [c for c in ID_COLUMNS if c in X.columns]
        
    preprocessor, features, num_features, cat_features = create_preprocessor(X, target_col, ignore_cols)
    
    # Only keep selected features
    X = X[features]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=RANDOM_STATE, stratify=y)
    
    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)
    
    if model_type == "XGBoost" and XGB_AVAILABLE:
        model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss', random_state=RANDOM_STATE)
    else:
        model = RandomForestClassifier(n_estimators=100, random_state=RANDOM_STATE, class_weight='balanced')
        
    model.fit(X_train_processed, y_train)
    
    y_pred = model.predict(X_test_processed)
    
    classes_present = sorted(y_test.unique())
    target_names = [INV_LABEL_MAP[c] for c in classes_present]
    eval_metrics = evaluate_model(y_test, y_pred, target_names=target_names)
    
    metadata = {
        'model_type': model_type,
        'features': features,
        'num_features': num_features,
        'cat_features': cat_features,
        'target_col': target_col,
        'ignore_cols': ignore_cols,
        'classes': target_names,
        'metrics': eval_metrics,
        'training_time': time.time() - start_time
    }
    
    save_model(model, MODEL_PATH)
    save_preprocessor(preprocessor, PREPROCESSOR_PATH)
    save_metadata(metadata, METADATA_PATH)
    
    return model, preprocessor, metadata, eval_metrics
