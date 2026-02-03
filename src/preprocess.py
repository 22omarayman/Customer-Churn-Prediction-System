import pandas as pd

NUM_COLS = ["Tenure Months", "Monthly Charges", "Total Charges"]

SERVICE_COLS = [
    "Phone Service", "Multiple Lines", "Online Security", "Online Backup",
    "Device Protection", "Tech Support", "Streaming TV", "Streaming Movies",
]

def preprocess_input(df: pd.DataFrame) -> pd.DataFrame:
    """
    Inference-safe preprocessing (matches Kaggle logic):
    - strip column names
    - convert numeric columns
    - fill missing values
    - feature engineering: AvgMonthlySpend, IsNewCustomer, IsLongContract, ServicesCount
    """
    df = df.copy()
    df.columns = df.columns.str.strip()

    # Convert numeric fields
    for c in NUM_COLS:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # Fill numeric missing
    for c in NUM_COLS:
        if c in df.columns:
            df[c] = df[c].fillna(df[c].median())

    # Fill categorical missing
    cat_cols = df.select_dtypes(include="object").columns
    for c in cat_cols:
        df[c] = df[c].fillna("Unknown")

    # Feature engineering
    if "Total Charges" in df.columns and "Tenure Months" in df.columns:
        df["AvgMonthlySpend"] = df["Total Charges"] / (df["Tenure Months"] + 1)

    if "Tenure Months" in df.columns:
        df["IsNewCustomer"] = (df["Tenure Months"] < 12).astype(int)

    if "Contract" in df.columns:
        df["IsLongContract"] = df["Contract"].isin(["One year", "Two year"]).astype(int)

    # ServicesCount
    present = [c for c in SERVICE_COLS if c in df.columns]
    for c in present:
        df[c] = df[c].fillna("No")

    if present:
        df["ServicesCount"] = (df[present] == "Yes").sum(axis=1)
    else:
        df["ServicesCount"] = 0

    return df
