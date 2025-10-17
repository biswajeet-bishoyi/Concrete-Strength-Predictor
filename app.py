import streamlit as st
import pandas as pd
import numpy as np
import joblib

# --- ADD CUSTOM CSS and STYLING HERE ---
st.markdown(
    """
    <style>
        .stApp { background-color: #191a1c !important; }
        /* ...rest of your CSS... */
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Sidebar information ---
st.sidebar.title("ℹ️ About")
st.sidebar.info(
    """
    This app predicts compressive strength of concrete mixes.
    🔹 Powered by Machine Learning  
    🔹 Best for use with realistic mix proportions.
    """
)
st.markdown('<i class="fas fa-flask"></i>', unsafe_allow_html=True)

# --- Main Title ---
st.title("Concrete Strength Predictor")
st.write("Enter concrete mix properties:")

# --- Collect user input FIRST ---
cement = st.number_input("Cement (kg/m³)", min_value=0.0, value=300.0)
slag = st.number_input("Blast Furnace Slag (kg/m³)", min_value=0.0, value=0.0)
flyash = st.number_input("Fly Ash (kg/m³)", min_value=0.0, value=0.0)
water = st.number_input("Water (kg/m³)", min_value=0.0, value=180.0)
superplasticizer = st.number_input("Superplasticizer (kg/m³)", min_value=0.0, value=10.0)
coarseagg = st.number_input("Coarse Aggregate (kg/m³)", min_value=0.0, value=970.0)
fineagg = st.number_input("Fine Aggregate (kg/m³)", min_value=1.0, value=780.0)
age = st.number_input("Age (days)", min_value=1, value=28)

# --- Input validation and warnings (DO THIS AFTER input blocks) ---
if cement <= 0:
    st.error("🚫 Cement must be greater than zero.")
if water / max(cement, 1) > 1:  # avoid division by zero
    st.warning("⚠️ Water-cement ratio is unusually high (>1.0). Check mix design!")

# --- Load the trained model ---
model = joblib.load(r"C:\kanha\college\projects\concrete strength\models\rf_best.pkl")

# --- Feature engineering (must match your training features) ---
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

if st.button("Predict Strength"):
    prediction = model.predict(df)[0]
    st.success(f"Predicted Strength: {prediction:.2f} MPa")
