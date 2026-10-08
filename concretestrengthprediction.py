# ============================================
# 📌 Concrete Strength Prediction (Final Version)
# ============================================

# 1️⃣ Import Libraries
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, RandomizedSearchCV, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import shap
from xgboost import XGBRegressor

# 2️⃣ Load Dataset
BASE_DIR = Path(__file__).resolve().parent
data_path = BASE_DIR / "data.xls"
df = pd.read_excel(data_path)

# 3️⃣ Rename columns for simplicity
df.columns = [
    "Cement", "BlastFurnaceSlag", "FlyAsh", "Water", "Superplasticizer",
    "CoarseAggregate", "FineAggregate", "Age", "ConcreteStrength"
]
print("✅ Dataset Loaded Successfully\n")
print(df.head())

# 4️⃣ Feature Engineering
df['Water_Cement'] = df['Water'] / df['Cement']
df['Coarse_Fine'] = df['CoarseAggregate'] / df['FineAggregate']
df['Age_Cement'] = df['Age'] / df['Cement']
df['Age_log'] = np.log1p(df['Age'])

# 5️⃣ Features & Target
X = df.drop(columns=['ConcreteStrength'])
y = df['ConcreteStrength']

# 6️⃣ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}")

# 7️⃣ Initialize Models
rf = RandomForestRegressor(random_state=42)
xgb = XGBRegressor(random_state=42, objective='reg:squarederror')

# 8️⃣ Hyperparameter Tuning for Random Forest (Randomized Search)
param_dist = {
    'n_estimators': [100, 200, 300, 400],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 4, 6, 8],
    'min_samples_leaf': [1, 2, 3, 4]
}
rnd_search = RandomizedSearchCV(
    estimator=rf,
    param_distributions=param_dist,
    n_iter=20,
    cv=5,
    n_jobs=-1,
    scoring='r2',
    random_state=42,
    verbose=1
)
rnd_search.fit(X_train, y_train)
rf_best = rnd_search.best_estimator_
print("\n✅ Best Random Forest Parameters:", rnd_search.best_params_)

# 9️⃣ Fit XGBoost Model
xgb.fit(X_train, y_train)

# 🔟 Model Evaluation Function
def evaluate_model(model, X_test, y_test, name="Model"):
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print(f"\n📊 {name} Evaluation:")
    print(f"R² Score: {r2:.3f}")
    print(f"MAE: {mae:.3f}")
    print(f"RMSE: {rmse:.3f}")
    return y_pred, r2, mae, rmse

# 1️⃣1️⃣ Evaluate Both Models
y_pred_rf, r2_rf, _, _ = evaluate_model(rf_best, X_test, y_test, "Random Forest")
y_pred_xgb, r2_xgb, _, _ = evaluate_model(xgb, X_test, y_test, "XGBoost")

# 1️⃣2️⃣ Cross-Validation for Random Forest
cv_scores = cross_val_score(rf_best, X, y, cv=10, scoring='r2')
print(f"\n🔁 10-Fold CV R² Mean: {cv_scores.mean():.3f}")

# 1️⃣3️⃣ Feature Importance Visualization (Random Forest)
importances = rf_best.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(8,5))
plt.bar(range(X.shape[1]), importances[indices], align="center", color='skyblue')
plt.xticks(range(X.shape[1]), X.columns[indices], rotation=45)
plt.title("Feature Importance (Random Forest)")
plt.tight_layout()
plt.show()

# 1️⃣4️⃣ SHAP Explainability
explainer = shap.TreeExplainer(rf_best)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)

models_dir = BASE_DIR / "models"
models_dir.mkdir(parents=True, exist_ok=True)

# 1️⃣5️⃣ Save Trained Random Forest Model
model_path = models_dir / "rf_best.pkl"
joblib.dump(rf_best, model_path)
print(f"\n✅ Model saved as {model_path}")

# 1️⃣6️⃣ Visualize Actual vs Predicted (Random Forest)
plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred_rf, alpha=0.6, edgecolor="k", color="teal")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.title("Actual vs Predicted Strength (Random Forest)")
plt.xlabel("Actual (MPa)")
plt.ylabel("Predicted (MPa)")
plt.tight_layout()
plt.show()
