import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
MODEL_DIR = BASE_DIR / 'models'

# Model File Paths
MODEL_PATH = MODEL_DIR / 'trained_model.pkl'
PREPROCESSOR_PATH = MODEL_DIR / 'preprocessor.pkl'
METADATA_PATH = MODEL_DIR / 'metadata.json'

# Data
SAMPLE_DATA_PATH = DATA_DIR / 'sample_dataset.csv'

# ML configuration
LABEL_MAP = {
    'Resistant': 0,
    'Intermediate': 1,
    'Susceptible': 2
}

INV_LABEL_MAP = {v: k for k, v in LABEL_MAP.items()}

# Common features to drop or ignore
ID_COLUMNS = ['Isolate_ID', 'ID', 'Patient_ID', 'Sample_ID']

RANDOM_STATE = 42
