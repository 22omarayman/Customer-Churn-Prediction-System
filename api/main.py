from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from src.predict import predict_proba, THRESHOLD

app = FastAPI(title="Customer Churn Prediction API")

class CustomerInput(BaseModel):
    Tenure_Months: float
    Monthly_Charges: float
    Total_Charges: float
    Contract: str
    Payment_Method: str
    Internet_Service: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: CustomerInput):
    df = pd.DataFrame([{
        "Tenure Months": payload.Tenure_Months,
        "Monthly Charges": payload.Monthly_Charges,
        "Total Charges": payload.Total_Charges,
        "Contract": payload.Contract,
        "Payment Method": payload.Payment_Method,
        "Internet Service": payload.Internet_Service,
    }])

    p = float(predict_proba(df)[0])
    return {
        "churn_probability": p,
        "churn_prediction": int(p >= THRESHOLD),
        "threshold": THRESHOLD
    }
