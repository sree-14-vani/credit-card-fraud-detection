import os
import joblib
import pandas as pd
MODEL_PATH = os.path.join("models", "fraud_model.pkl")
THRESHOLD_PATH = os.path.join("models", "threshold.pkl")
FEATURES_PATH = os.path.join("models", "feature_names.pkl")
model = joblib.load(MODEL_PATH)
threshold = joblib.load(THRESHOLD_PATH)
feature_names = joblib.load(FEATURES_PATH)
def predict_fraud(transaction_data):
    """
    Predict whether a transaction is fraudulent.
    transaction_data should contain all 30 model features.
    """
    data = pd.DataFrame([transaction_data], columns=feature_names)
    probability = model.predict_proba(data)[0][1]
    prediction = int(probability >= threshold)
    return prediction, probability