# 🧪 Concrete Strength Predictor

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?logo=plotly&logoColor=white)](https://plotly.com/)

**An empirical civil engineering machine learning application predicting compressive strength (in MPa) of concrete mixtures across constituent proportions and curing age.**

[Report Bug](https://github.com/biswajeet-bishoyi/Concrete-Strength-Predictor/issues) • [Request Feature](https://github.com/biswajeet-bishoyi/Concrete-Strength-Predictor/issues)

</div>

---

## 🌟 Overview

Accurately predicting the 28-day and long-term compressive strength of concrete is essential for quality control, structural safety, and sustainable mix optimization. The **Concrete Strength Predictor** pairs a tuned Random Forest regression model trained on 1,030 physical mix designs with an engineering-grade laboratory dashboard, embodied carbon calculators, and economic batch cost analysis.

---

## 🚀 Key Features

- **🌲 Tuned Machine Learning Regressor**: Random Forest regressor with cross-validated hyperparameter tuning achieving $R^2 \approx 0.85+$ and low MAE (~4.5 MPa).
- **🎨 Engineering Laboratory UI**: Dark palette (Concrete Charcoal `#141517`, Brass Gold `#E8B84F`, and JetBrains Mono) designed for laboratory environments and desktop field use.
- **🧱 Grouped Constituent Proportions**:
  - **Binders**: Cement, Blast Furnace Slag, Fly Ash
  - **Liquids & Modifiers**: Water, Superplasticizer
  - **Aggregates**: Coarse Aggregate, Fine Aggregate
  - **Curing**: Age (1 to 365 days)
- **🔍 Real-Time Input Diagnostics**: Boundary checking against physical impossibility, zero/negative inputs, high $w/c$ warnings ($w/c > 1.0$), and pozzolanic replacement thresholds.
- **📈 Multi-Age Maturity Curves**: Interactive Plotly trajectory predicting strength progression from day 1 to day 365 with milestone benchmarks (3, 7, 14, 28, 90, 365 days).
- **🌱 Embodied Carbon & Sustainability Index**: Cradle-to-gate carbon calculator based on the Inventory of Carbon & Energy (ICE) database. Quantifies net $\text{CO}_2$ savings from supplementary cementitious materials (slag & fly ash) and Eco-Efficiency ($	ext{MPa} \text{ per } 100\text{ kg CO}_2\text{e}$).
- **💰 Economic & Cost Analysis**: Material batch costing in Indian Rupees (₹/m³) and cost per unit strength (₹/MPa) with customizable regional price rates.
- **🧪 Automated Unit Testing**: Comprehensive test suite (`test_prediction.py`) verifying physical laws (e.g., Abrams' law: strength inversely correlates with $w/c$ ratio).

---

## 📊 Model Technical Specifications

| Metric | Random Forest (Tuned) |
|---|---|
| **Dataset Size** | 1,030 laboratory samples |
| **Data Split** | 80% Train / 20% Test |
| **Validation** | 10-Fold Cross-Validation ($R^2 \approx 0.85+$) |
| **Mean Absolute Error (MAE)** | ~4.5 MPa |
| **Root Mean Squared Error (RMSE)** | ~6.5 MPa |
| **Engineered Features** | $w/c$, $\text{Coarse}/\text{Fine}$, $\text{Age}/\text{Cement}$, $\ln(1 + \text{Age})$ |

---

## 📁 Repository Structure

```
concrete-strength/
├── app.py                         # Interactive Streamlit application
├── concretestrengthprediction.py  # Model training & evaluation pipeline
├── styles.css                     # Custom engineering design tokens
├── requirements.txt               # Python package dependencies
├── data.xls                       # Concrete compressive strength dataset
├── models/
│   └── rf_best.pkl                # Serialized best Random Forest model
└── correction/                    # Technical documentation & requirements
```

---

## 🛠️ Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch the Application
```bash
streamlit run app.py
```

### 3. (Optional) Re-train or Evaluate the Model
```bash
python concretestrengthprediction.py
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
Developed by <a href="https://github.com/biswajeet-bishoyi">Biswajeet Bishoyi</a>
</div>
