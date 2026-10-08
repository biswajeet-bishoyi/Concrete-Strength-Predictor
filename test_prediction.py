from pathlib import Path
import unittest
import numpy as np
import pandas as pd
import joblib

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "rf_best.pkl"
if not MODEL_PATH.exists() and (BASE_DIR / "rf_best.pkl").exists():
    MODEL_PATH = BASE_DIR / "rf_best.pkl"

def create_feature_df(cement, slag, flyash, water, superplasticizer, coarseagg, fineagg, age):
    """Utility function to reproduce the exact feature engineering pipeline."""
    return pd.DataFrame([{
        "Cement": float(cement),
        "BlastFurnaceSlag": float(slag),
        "FlyAsh": float(flyash),
        "Water": float(water),
        "Superplasticizer": float(superplasticizer),
        "CoarseAggregate": float(coarseagg),
        "FineAggregate": float(fineagg),
        "Age": int(age),
        "Water_Cement": float(water) / float(cement) if cement > 0 else 0.0,
        "Coarse_Fine": float(coarseagg) / float(fineagg) if fineagg > 0 else 0.0,
        "Age_Cement": float(age) / float(cement) if cement > 0 else 0.0,
        "Age_log": float(np.log1p(age))
    }])

class TestConcreteStrengthPrediction(unittest.TestCase):

    def setUp(self):
        self.assertTrue(MODEL_PATH.exists(), f"Model artifact missing at {MODEL_PATH}")
        self.model = joblib.load(MODEL_PATH)

    def test_feature_engineering_columns(self):
        df = create_feature_df(300, 0, 0, 180, 10, 970, 780, 28)
        expected_cols = [
            "Cement", "BlastFurnaceSlag", "FlyAsh", "Water", "Superplasticizer",
            "CoarseAggregate", "FineAggregate", "Age", "Water_Cement", "Coarse_Fine",
            "Age_Cement", "Age_log"
        ]
        self.assertEqual(list(df.columns), expected_cols)
        self.assertEqual(df.shape, (1, 12))

    def test_benchmark_prediction(self):
        df = create_feature_df(300, 0, 0, 180, 10, 970, 780, 28)
        pred = self.model.predict(df)[0]
        # Standard concrete with these proportions typically ranges between 30 and 45 MPa
        self.assertTrue(25.0 <= pred <= 55.0, f"Expected realistic prediction, got {pred:.2f} MPa")

    def test_strength_increases_with_curing_age(self):
        df_early = create_feature_df(320, 50, 0, 175, 8, 980, 760, 3)
        df_mature = create_feature_df(320, 50, 0, 175, 8, 980, 760, 28)
        
        pred_early = self.model.predict(df_early)[0]
        pred_mature = self.model.predict(df_mature)[0]
        
        self.assertGreater(
            pred_mature, pred_early,
            f"28-day strength ({pred_mature:.2f} MPa) should exceed 3-day strength ({pred_early:.2f} MPa)"
        )

    def test_higher_water_reduces_strength(self):
        df_low_water = create_feature_df(350, 0, 0, 160, 10, 970, 780, 28)
        df_high_water = create_feature_df(350, 0, 0, 230, 0, 970, 780, 28)
        
        pred_low_w = self.model.predict(df_low_water)[0]
        pred_high_w = self.model.predict(df_high_water)[0]
        
        self.assertGreater(
            pred_low_w, pred_high_w,
            f"Lower water mix ({pred_low_w:.2f} MPa) should be stronger than high water mix ({pred_high_w:.2f} MPa)"
        )

    def test_zero_division_guard(self):
        df_zero_cement = create_feature_df(0, 100, 50, 180, 5, 970, 780, 28)
        self.assertEqual(df_zero_cement["Water_Cement"].iloc[0], 0.0)
        self.assertEqual(df_zero_cement["Age_Cement"].iloc[0], 0.0)

if __name__ == "__main__":
    unittest.main()
