# 📉 Customer Churn Prediction System (End-to-End)

This project is a complete churn prediction solution:
- ✅ Training & evaluation in a notebook (Kaggle/Jupyter)
- ✅ Saved model artifacts
- ✅ FastAPI for serving predictions (machine access)
- ✅ Streamlit dashboard for business users (human access)

---

# ✅ Step 1 — What this project does (in one minute)

## 🎯 Goal
Predict whether a telecom customer will churn (leave) using machine learning, so the business can take retention actions early.

## 🧠 Two phases
### 1) Training (Notebook)
We use the dataset to:
- clean data
- do EDA
- engineer features
- train models
- evaluate + explain
- save the final model artifacts

Output:
- `models/churn_model.joblib
- `models/features.joblib`

### 2) Deployment (VS Code)
We do NOT use the full dataset anymore.

Instead we:
- load the saved artifacts
- input one new customer
- return churn probability + label

Deployment is provided through:
- **FastAPI** → API endpoint `/predict` for other apps
- **Streamlit** → Dashboard UI for users to enter customer details

---

## 📌 Dataset
IBM Telco Customer Churn dataset  
Target:
- `Churn = 1` → customer leaves  
- `Churn = 0` → customer stays  

---

## ✅ What you can run locally
- **FastAPI docs:** `http://127.0.0.1:8000/docs`
- **Streamlit UI:** `http://localhost:8501`

---
# ✅ Step 2 — Project Structure & File Responsibilities

This project follows a clean, modular architecture:
**Training → Serving (API) → User Interface (Dashboard)**



This structure makes the system:
- ✅ Maintainable
- ✅ Reusable
- ✅ Production-ready
- ✅ Easy to extend

---

## 📂 Project Structure

```text
customer-churn-system/
│
├── models/             # Saved model artifacts
│   ├── churn_model.joblib
│   └── features.joblib
│
├── src/                # Shared ML logic
│   ├── preprocess.py
│   ├── predict.py
│   └── __init__.py
│
├── api/                # FastAPI Layer
│   └── main.py
│
├── dashboard/          # Streamlit Layer
│   └── app.py
│
├── notebooks/          # R&D / Training
│   └── churn_training.ipynb
│
├── requirements.txt    # Dependencies
└── README.md
```
---


# 📁 Folder Responsibilities

## 🔹 models/

Contains the **saved outputs from training**.

These files are generated inside the training notebook and later loaded during deployment.

### Files

### • churn_model.joblib
Stores:
- trained model weights
- learned patterns
- parameters

Think of this file as the **brain of the system**.

It allows predictions without needing the original dataset.

---

### • features.joblib
Stores:
- the exact feature column order used during training

This is critical because the model expects **the same column order** during inference.

If the order changes → predictions become incorrect.

---

## 🔹 src/

Contains the **core machine learning logic** shared by both:
- FastAPI
- Streamlit

This avoids duplicating code and ensures consistent predictions everywhere.

---

### • preprocess.py

Responsible for:
- feature engineering
- encoding categorical variables
- scaling numeric values
- preparing inputs for the model

Converts:

Raw customer input → numeric vector

---

### • predict.py

Responsible for:
- loading the saved model
- calling preprocessing
- generating probabilities
- returning churn prediction

This file is the **central prediction engine** used by:
- FastAPI
- Streamlit

---

## 🔹 api/

Contains the **FastAPI server**.

Purpose:
Expose the model as a REST API.

This allows:
- websites
- mobile apps
- CRMs
- other systems

to request predictions programmatically.

Example endpoint:

POST /predict

---

## 🔹 dashboard/

Contains the **Streamlit application**.

Purpose:
Provide a visual interface for human users.

Allows:
- sliders
- dropdown menus
- instant predictions

Designed for:
- business users
- analysts
- managers

No coding required.

---

## 🔹 notebooks/

Contains the **training notebook**.

Used only for:
- data cleaning
- EDA
- model training
- evaluation
- explainability
- exporting models

⚠️ Not used during deployment.

---

# 🧠 System Workflow

## Training Phase

Dataset  
→ Train model  
→ Save model files (.joblib)

---

## Deployment Phase

Load saved model  
→ Input one customer  
→ Predict churn probability

---

# ⚡ Important Notes

- VS Code / API does NOT load the full dataset
- Only saved model files are loaded
- Predictions are fast and production-ready
- Same logic shared between API and dashboard

---

# ▶️ How to Run

Follow these steps to get the system running locally.

### 1️⃣ Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```
### 2️⃣ Start FastAPI server
```bash
python -m uvicorn api.main:app --reload
```

API will be available at:
```bash
http://127.0.0.1:8000
```
Interactive Docs
```bash
http://127.0.0.1:8000/docs
```
### 3️⃣ Start Streamlit dashboard
```bash
streamlit run app/dashboard/app.py
```
Dashboard will open at:
```bash
http://localhost:8501
```
---

# ✅ Step 3 — Training Workflow (What happens inside the Notebook)

Location:
notebooks/churn_training.ipynb


This notebook is where the **machine learning model is built and trained**.

It is the only place where the dataset is used.

After training, we export the model and NEVER use the full dataset again.

---

# 📊 Training Pipeline Overview

The notebook follows a complete ML workflow:
```text
Load Data
↓
Clean & Preprocess
↓
EDA & Insights
↓
Feature Engineering
↓
Train Models
↓
Evaluate & Compare
↓
Explain (SHAP)
↓
Save Model Files
```

---

# 🔹 Step-by-Step Breakdown

## 1️⃣ Load Dataset
We load the IBM Telco Customer Churn dataset.

Contains:
- customer demographics
- service usage
- billing information
- contract details
- churn label

Target variable:
- Churn = 1 → customer leaves
- Churn = 0 → customer stays


---

## 2️⃣ Data Cleaning

We prepare the data for modeling:

Actions performed:
- removed leakage columns (Churn Score, CLTV, etc.)
- converted Total Charges to numeric
- handled missing values
- standardized column names

Goal:
Ensure clean and reliable input for models


---

## 3️⃣ Exploratory Data Analysis (EDA)

We analyzed customer behavior to understand churn drivers.

Key findings:

- Short tenure → high churn
- Month-to-month contracts → highest churn
- High monthly charges → higher churn
- Electronic check payments → higher churn
- Fiber optic users → higher churn

These insights guided feature engineering and model design.

---

## 4️⃣ Feature Engineering

We created additional features to improve prediction power.

Examples:

- AvgMonthlySpend
- IsNewCustomer (early tenure flag)
- IsLongContract (commitment flag)
- ServicesCount (number of services subscribed)

Goal:
Transform raw data into stronger predictive signals


---

## 5️⃣ Encoding & Scaling

Before training:

- categorical variables → encoded
- numeric features → scaled

Reason:
Models require numeric, standardized inputs


---

## 6️⃣ Model Training

We trained multiple algorithms:

- Logistic Regression
- XGBoost
- Random Forest
- LightGBM

Evaluation metric:
ROC-AUC


Results:

| Model | ROC-AUC |
|-------|---------|
| Logistic Regression | ~0.85 |
| XGBoost | ~0.85 |
| Random Forest | ~0.84 |
| LightGBM | ~0.84 |

Selected model:
Logistic Regression


Reason:
- similar performance
- simpler
- faster
- easier to interpret

---

## 7️⃣ Threshold Optimization

Default classification threshold:
0.5


We adjusted to:
0.4


Why:
- improves recall for churn class
- catches more at-risk customers

This is better for business retention strategies.

---

## 8️⃣ Explainability (SHAP)

Used SHAP to understand:

- which features influence churn most
- how each prediction is made

Top drivers:
- Monthly charges
- Tenure
- Contract type
- Payment method

This improves trust and interpretability.

---

## 9️⃣ Save Model Artifacts

Finally, we export trained objects for deployment.

Saved files:

models/churn_model.joblib
models/features.joblib


These files contain:
- trained model
- feature order

These are later loaded by FastAPI and Streamlit.

---

# 🧠 Important Concept

## Training happens ONLY here

Notebook → learn patterns → save model


## Deployment does NOT retrain

Load saved model → predict new customers


This separation ensures:
- faster predictions
- lower memory usage
- production readiness

---

# ✅ Step 4 — Deployment Phase (FastAPI + Streamlit)

After training the model in the notebook, we move to **deployment**. In this phase, we use the trained model to predict outcomes for new customers in real-time.

> [!IMPORTANT]
> The original dataset is **not** used during deployment. Only the compact, saved model files (.joblib) are loaded, ensuring the system is fast and lightweight.

---

# 🧠 The Big Picture



1. **Notebook (Training):** Data is processed and the model is trained.
2. **Export:** Model files are saved to the `models/` directory.
3. **VS Code (Deployment):** FastAPI and Streamlit load those files to perform **Inference**.

---

# 🚀 What is Inference?
Instead of training on thousands of rows, we now take **one customer's data** and return a **churn probability**. This is called inference.

### 📁 The Core Engine (`src/`)
To ensure consistency, both the API and the Dashboard use the exact same logic stored in the `src/` folder:

* **`preprocess.py`**: Converts raw customer data (e.g., "Month-to-month") into numeric vectors.
* **`predict.py`**: The **Single Source of Truth**. It loads the model, runs the preprocessing, and generates the final probability.

---

# ⚡ FastAPI (Machine Interface)
**Location:** `api/main.py`  
Exposes the model as a web service so other applications (Mobile apps, CRMs, Websites) can talk to it.

* **Endpoint:** `POST /predict`
* **Request Format:**
    ```json
    {
      "tenure": 10,
      "monthly_charges": 80,
      "contract": "Month-to-month"
    }
    ```
* **Response Format:**
    ```json
    {
      "probability": 0.87,
      "prediction": 1
    }
    ```

# 🖥️ Streamlit (Human Interface)

**Location:** `dashboard/app.py`  
Streamlit provides a visual dashboard designed for managers, analysts, and business users who need to interact with the model without writing a single line of code.



### 💡 Features
* **Interactive Controls:** Sliders for numeric data and dropdown menus for categorical options.
* **Instant Feedback:** View prediction results and churn probabilities immediately upon clicking "Predict."
* **No-Code Interface:** Designed for non-technical stakeholders to perform "What-if" analysis.

### 🔄 Internal Flow
`User Input` → `src/predict.py` → `UI Result Display`

# 🔑 FastAPI vs. Streamlit

While both tools serve the same model, they are designed for different audiences:

| Tool | Purpose | Primary User |
| :--- | :--- | :--- |
| **FastAPI** | Programmatic REST API | Other Apps & Systems (Backend) |
| **Streamlit** | Visual UI Dashboard | Humans (Business Analysts/Managers) |

> [!NOTE]
> Both interfaces use the **exact same** model and preprocessing logic from the `src/` folder. Only the way the user interacts with the data changes.

---

# ✅ Final Result

You have successfully built a production-style machine learning architecture including:

* **📦 A Trained Model:** Serialized and ready for real-time work.
* **🔌 A Machine Interface (API):** For automated system integrations and external calls.
* **📊 A Human Interface (Dashboard):** For manual business insights, "what-if" scenarios, and testing.
* **🛠️ Modular Logic:** A "Single Source of Truth" in the `src/` folder to prevent code duplication and ensure consistency.

This setup ensures your system is **fast**, **scalable**, and **easy to maintain**.

---

# ✅ Step 6 — Business Value, Skills & Final Summary

This project is not just a notebook experiment.

It demonstrates how to build a **complete production-style machine learning system** from start to finish.

---

# 💼 Business Value

Customer churn directly impacts revenue.

If a telecom company loses customers:
- revenue drops
- acquisition costs increase
- lifetime value decreases

This system helps by:

### ✅ Early Detection
Identify customers likely to churn before they leave.

### ✅ Targeted Retention
Send:
- discounts
- offers
- loyalty rewards

only to high-risk customers instead of everyone.

### ✅ Cost Optimization
Focus marketing budget on customers who actually need intervention.

### ✅ Revenue Protection
Reducing churn by even 1–2% can save millions annually.

---

# 🚀 What This System Provides

End-to-end workflow:

### Training
- clean data
- analyze behavior
- train models
- explain results
- export model

### Deployment
- API for machines (FastAPI)
- dashboard for humans (Streamlit)
- instant predictions
- production-ready structure

---

# 🧠 Technical Skills Demonstrated

This project showcases:

## Data Science
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation (ROC-AUC, Recall, F1)
- Threshold Tuning
- Explainability (SHAP)

---

## Machine Learning Engineering
- Model Serialization (joblib)
- Modular project structure
- Shared preprocessing pipelines
- Reproducible inference

---

## Backend & Deployment
- FastAPI REST APIs
- Streamlit dashboards
- Virtual environments
- Local deployment
- Production architecture

---

## Software Engineering
- Clean folder organization
- Separation of concerns
- Reusable modules
- Version control (GitHub)
- Documentation

---

# 🧩 End-to-End Flow Summary



### 🧪 Training Phase (Notebook)
1. **Dataset** → The raw historical data source.
2. **EDA & Cleaning** → Understanding and fixing data quality.
3. **Feature Engineering** → Selecting the most important variables.
4. **Train Models** → The computer learns the churn patterns.
5. **Save Model Files** → Exporting the "brain" as `.joblib` files.

### 🚀 Deployment Phase (VS Code)
1. **Load Saved Model** → Accessing the exported artifacts.
2. **Input 1 Customer** → Receiving new data from a user or API.
3. **Preprocess** → Formatting the data to match training standards.
4. **Predict Probability** → Calculating the likelihood of churn.
5. **Return Result** → Sending results back via **FastAPI** or **Streamlit**.

---

# 📌 Key Takeaway

The dataset is only used during **training**. During **deployment**, no dataset is loaded. The system relies entirely on the saved model artifacts.

This makes predictions:
- ⚡ **Fast** (Instant results)
- 🎈 **Lightweight** (Low memory usage)
- 📈 **Scalable** (Handles thousands of requests)

---

# 🎯 Final Result

You now have a complete ecosystem:
* ✅ **Trained ML Model:** Optimized for accuracy.
* ✅ **Feature Engineering Pipeline:** Consistent data handling.
* ✅ **Explainability:** Understanding *why* customers churn.
* ✅ **Saved Artifacts:** Portable and ready for any server.
* ✅ **FastAPI Service:** Ready for machine-to-machine integration.
* ✅ **Streamlit Dashboard:** Ready for business user interaction.
* ✅ **Production-ready Architecture:** Professional folder structure.
* ✅ **Full Documentation:** Clear steps for future developers.

---

# 🏁 Conclusion

This project demonstrates the transition from a **"Notebook-only analysis"** ❌ to a **"Real-world deployable machine learning system"** ✅. 

It represents a complete, practical, and business-focused ML solution ready for integration into real-world applications.
