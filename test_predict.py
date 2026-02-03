import pandas as pd
from src.predict import predict_proba, predict_label

sample = pd.DataFrame([{
    "Tenure Months": 10,
    "Monthly Charges": 80,
    "Total Charges": 500,
    "Contract": "Month-to-month",
    "Payment Method": "Electronic check",
    "Internet Service": "Fiber optic"
}])

print("proba:", predict_proba(sample)[0])
print("label:", predict_label(sample)[0])
