from pathlib import Path
import joblib
import pandas as pd
import numpy as np

from .preprocess import preprocess_input

BASE_DIR = Path(__file__).resolve().parents[1]  # project root
MODEL_PATH = BASE_DIR / "models" / "churn_model.joblib"
FEATURES_PATH = BASE_DIR / "models" / "features.joblib"

THRESHOLD = 0.40  # your tuned threshold

_model = joblib.load(MODEL_PATH)
_feature_cols = joblib.load(FEATURES_PATH)

def predict_proba(df_raw: pd.DataFrame) -> np.ndarray:
    df = preprocess_input(df_raw)
    X = pd.get_dummies(df, drop_first=True)
    X = X.reindex(columns=_feature_cols, fill_value=0)
    return _model.predict_proba(X)[:, 1]

def predict_label(df_raw: pd.DataFrame) -> np.ndarray:
    proba = predict_proba(df_raw)
    return (proba >= THRESHOLD).astype(int)
