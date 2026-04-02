def validate_uploaded_file(df, required_cols=None):
    errors = []
    
    if df is None or df.empty:
        errors.append("Dataset is empty.")
        return False, errors
        
    if required_cols:
        missing = [c for c in required_cols if c not in df.columns]
        if missing:
            errors.append(f"Missing required columns: {', '.join(missing)}")
            
    # Check for too many missing values
    if df.isnull().sum().sum() > (df.shape[0] * df.shape[1] * 0.5):
        errors.append("Dataset has more than 50% missing values. Prediction might be unreliable.")
        
    return len(errors) == 0, errors
