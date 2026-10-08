# 🏗️ Concrete Strength Predictor

A civil engineering machine learning web application that predicts the compressive strength (in MPa) of concrete mixtures given their constituent proportions and curing age.

---

## 🚀 Features

- **Empirical ML Model**: Powered by a tuned Random Forest regressor trained on 1,030 physical mix designs ($R^2 \approx 0.85+$).
- **Engineering-Grade Material UI**: Dark palette (Concrete Charcoal `#141517`, Brass Gold `#e8b84f`, and JetBrains Mono) designed specifically for laboratory and engineering workflows.
- **Grouped Mix Proportions**:
  - **Binders**: Cement, Blast Furnace Slag, Fly Ash
  - **Liquids & Modifiers**: Water, Superplasticizer
  - **Aggregates**: Coarse Aggregate, Fine Aggregate
  - **Curing**: Age (1 to 365 days)
- **Real-Time Diagnostics**:
  - Validates boundaries and prevents execution on non-physical zero or negative values.
  - Warns on high water-cement ratios ($w/c > 1.0$), low $w/c < 0.25$, high supplementary binder replacement, and excessive superplasticizer dosages.
- **Mix Insights & Derived Ratios**:
  - Water-Cement Ratio ($w/c$)
  - Water-Binder Ratio ($w/b$)
  - Total Binder Content ($\text{kg/m}^3$)
  - Coarse-to-Fine Aggregate Ratio
  - Wet bulk density estimation
  - Relative feature importance breakdown
- **📈 Multi-Age Maturity Curves**:
  - Interactive Plotly trajectory predicting strength from 1 to 365 days.
  - Milestone analysis comparing strength against 28-day benchmarks.
- **🌿 Embodied Carbon & Sustainability**:
  - Cradle-to-gate carbon calculator based on the ICE database.
  - Computes net $\text{CO}_2$ savings from slag and fly ash pozzolanic replacement.
  - Eco-Efficiency Index ($\text{MPa} \text{ per } 100\text{ kg CO}_2\text{e}$).
- **💰 Economic & Cost Analysis**:
  - Material batch costing in Indian Rupees ($\text{₹/m}^3$).
  - Cost per unit strength ($\text{₹/MPa}$).
  - Fully adjustable regional material price rates.
- **🧪 Automated Unit Testing**:
  - Comprehensive unit test suite (`test_prediction.py`) verifying physical laws and model consistency.

---

## 📁 Repository Structure

```
concrete strength/
├── app.py                         # Streamlit web application
├── concretestrengthprediction.py  # Model training & evaluation pipeline
├── styles.css                     # Custom design system stylesheet
├── requirements.txt               # Project dependencies
├── data.xls                       # Dataset (1,030 samples)
├── models/
│   └── rf_best.pkl                # Serialized Random Forest model
└── correction/                    # Specifications and project documentation
    ├── FRONTEND_REQUIREMENTS.md
    ├── PROJECT_LOG.md
    └── MEMORY.md
```

---

## 🛠️ Quickstart

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch Web Application
```bash
streamlit run app.py
```

### 3. (Optional) Re-train or Evaluate Model
```bash
python concretestrengthprediction.py
```

---

## 🔬 Model Technical Specs

| Metric | Random Forest (Tuned) |
|---|---|
| **Dataset Size** | 1,030 samples |
| **Split** | 80% Train / 20% Test |
| **Cross-Validation** | 10-Fold CV ($R^2 \approx 0.85+$) |
| **Mean Absolute Error (MAE)** | ~4.5 MPa |
| **Root Mean Squared Error (RMSE)** | ~6.5 MPa |
| **Engineered Features** | $w/c$, $\text{Coarse}/\text{Fine}$, $\text{Age}/\text{Cement}$, $\ln(1 + \text{Age})$ |
