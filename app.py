import streamlit as st
import pandas as pd
import numpy as np
import joblib

# --- Custom CSS for a modern look ---
st.markdown(
    """
    <style>
        .stApp { background-color: #191a1c !important; }
        .stNumberInput, .stTextInput input {
            background-color: #24252a !important;
            color: #f5f5f5 !important;
        }
        .css-1emrehy .stButton>button {
            background: linear-gradient(90deg, #007bff, #00c6ff) !important;
            color: white !important;
            border-radius: 8px;
            border: 0;
            padding: 0.7em 2em;
            margin-top: 1em;
            font-size: 1.2em;
        }
        .stAlert-success, .stAlert-info, .stAlert-warning, .stAlert-error {
            border-radius: 10px;
        }
        h1, h2, h3 {
            color: #21e6c1 !important;
            text-align: center !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Sidebar Information ---
st.sidebar.title("ℹ️ About")
st.sidebar.info(
    """
    This app predicts compressive strength of concrete mixes.

    🔹 Powered by Machine Learning  
    🔹 Best for use with realistic mix proportions.
    """
)

# --- Main Title and Instructions ---
st.title("Concrete Strength Predictor")
st.markdown("""
Enter your concrete mix properties below.  
- All values must be realistic and non-negative.
- Typical ranges:  
    Cement: 100–600 kg/m³, Water: 120–250 kg/m³, Age: 1–365 days, etc.
---
""")

# --- Load Model (relative path!) ---
try:
    model = joblib.load("rf_best.pkl")
except Exception:
    st.error("Model file not found. Please make sure 'rf_best.pkl' is in the repo.")

# --- Input Section ---
cement = st.number_input("Cement (kg/m³)", min_value=0.0, max_value=700.0, value=300.0, step=1.0)
slag = st.number_input("Blast Furnace Slag (kg/m³)", min_value=0.0, max_value=400.0, value=0.0, step=1.0)
flyash = st.number_input("Fly Ash (kg/m³)", min_value=0.0, max_value=400.0, value=0.0, step=1.0)
water = st.number_input("Water (kg/m³)", min_value=0.0, max_value=400.0, value=180.0, step=1.0)
superplasticizer = st.number_input("Superplasticizer (kg/m³)", min_value=0.0, max_value=30.0, value=10.0, step=0.5)
coarseagg = st.number_input("Coarse Aggregate (kg/m³)", min_value=0.0, max_value=1300.0, value=970.0, step=1.0)
fineagg = st.number_input("Fine Aggregate (kg/m³)", min_value=1.0, max_value=1100.0, value=780.0, step=1.0)
age = st.number_input("Age (days)", min_value=1, max_value=365, value=28, step=1)

# --- Input validation and warnings ---
if cement <= 0:
    st.error("🚫 Cement must be greater than zero.")
if water / max(cement, 1) > 1:
    st.warning("⚠️ Water-cement ratio is unusually high (>1.0). Check mix design!")

# --- Feature Engineering for Prediction ---
df = pd.DataFrame([{
    "Cement": cement,
    "BlastFurnaceSlag": slag,
    "FlyAsh": flyash,
    "Water": water,
    "Superplasticizer": superplasticizer,
    "CoarseAggregate": coarseagg,
    "FineAggregate": fineagg,
    "Age": age,
    "Water_Cement": water/cement if cement > 0 else 0,
    "Coarse_Fine": coarseagg/fineagg if fineagg > 0 else 0,
    "Age_Cement": age/cement if cement > 0 else 0,
    "Age_log": np.log1p(age)
}])

# --- Prediction and Display ---
if st.button("Predict Strength") and cement > 0 and fineagg > 0:
    try:
        prediction = model.predict(df)[0]
        st.success(f"**Predicted Compressive Strength:** {prediction:.2f} MPa")
        st.info("Note: Prediction is based on your input. Lab results may vary.")
    except Exception as e:
        st.error(f"Prediction error: {e}")

st.markdown("---")
st.markdown("Created by [Your Name]. For academic demonstration only.")

