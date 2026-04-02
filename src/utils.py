import joblib
import json
import os
import pandas as pd
import logging
from src.config import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_model(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)
    logger.info(f"Model saved to {path}")

def load_model(path):
    if not os.path.exists(path):
        return None
    return joblib.load(path)

def save_preprocessor(preprocessor, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(preprocessor, path)
    logger.info(f"Preprocessor saved to {path}")

def load_preprocessor(path):
    if not os.path.exists(path):
        return None
    return joblib.load(path)

def save_metadata(metadata, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(metadata, f, indent=4)
    logger.info(f"Metadata saved to {path}")

def load_metadata(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        return json.load(f)

def clean_dataframe(df, target_col):
    # Map target columns if they are string "R", "S", "I" to full names
    if target_col in df.columns:
        df[target_col] = df[target_col].replace({
            'R': 'Resistant', 'r': 'Resistant',
            'S': 'Susceptible', 's': 'Susceptible',
            'I': 'Intermediate', 'i': 'Intermediate'
        })
    return df
