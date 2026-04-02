import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from src.config import LABEL_MAP

def create_preprocessor(df, target_col, ignore_cols=None):
    if ignore_cols is None:
        ignore_cols = []
    
    features = [c for c in df.columns if c != target_col and c not in ignore_cols]
    
    numeric_features = df[features].select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_features = df[features].select_dtypes(include=['object', 'category']).columns.tolist()
    
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    return preprocessor, features, numeric_features, categorical_features

def preprocess_target(df, target_col):
    df = df.copy()
    df[target_col] = df[target_col].map(LABEL_MAP)
    # Drop rows where target couldn't be mapped
    df = df.dropna(subset=[target_col])
    return df
