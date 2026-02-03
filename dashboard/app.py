import streamlit as st
import pandas as pd
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.predict import predict_proba, THRESHOLD

st.set_page_config(page_title="Churn Dashboard", layout="wide")
st.title("📉 Customer Churn Prediction Dashboard")

col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure Months", min_value=0.0, value=10.0)
    monthly = st.number_input("Monthly Charges", min_value=0.0, value=80.0)
    total = st.number_input("Total Charges", min_value=0.0, value=500.0)

with col2:
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    payment = st.selectbox("Payment Method", [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ])
    internet = st.selectbox("Internet Service", ["Fiber optic", "DSL", "No"])

if st.button("Predict"):
    df = pd.DataFrame([{
        "Tenure Months": tenure,
        "Monthly Charges": monthly,
        "Total Charges": total,
        "Contract": contract,
        "Payment Method": payment,
        "Internet Service": internet,
    }])

    p = float(predict_proba(df)[0])
    st.metric("Churn probability", f"{p:.2%}")
    st.write("Prediction:", "🔴 Likely to churn" if p >= THRESHOLD else "🟢 Likely to stay")
    st.caption(f"Threshold used: {THRESHOLD}")
