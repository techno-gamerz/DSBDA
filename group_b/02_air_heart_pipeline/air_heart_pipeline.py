from pathlib import Path
import json
import sqlite3

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

BASE = Path(__file__).parent
DATA_DIR = BASE / "data"
OUT_DIR = BASE / "outputs"
OUT_DIR.mkdir(exist_ok=True)


def load_air_quality() -> pd.DataFrame:
    path = DATA_DIR / "air_quality.csv"
    sample = DATA_DIR / "air_quality_sample.csv"
    return pd.read_csv(path if path.exists() else sample)


def load_heart_disease() -> pd.DataFrame:
    path = DATA_DIR / "heart_disease.csv"
    sample = DATA_DIR / "heart_disease_sample.csv"
    return pd.read_csv(path if path.exists() else sample)


def clean_air_quality(df: pd.DataFrame) -> pd.DataFrame:
    air = df.copy()
    air["Date"] = air["Date"].astype(str)
    air["Time"] = air["Time"].astype(str)
    air["datetime"] = pd.to_datetime(
        air["Date"] + " " + air["Time"], errors="coerce", dayfirst=True
    )
    air = air.drop_duplicates()

    num_cols = [c for c in air.columns if c not in ["Date", "Time", "datetime"]]
    for col in num_cols:
        air[col] = pd.to_numeric(air[col], errors="coerce")
        air[col] = air[col].replace(-200, np.nan)
        air[col] = air[col].fillna(air[col].median())

    if "CO" in air.columns:
        air["CO"] = air["CO"].clip(lower=0)
    if "Temp" in air.columns:
        air["Temp"] = air["Temp"].clip(lower=-20, upper=60)

    air["hour"] = air["datetime"].dt.hour
    if "CO" in air.columns:
        air["co_log"] = np.log1p(air["CO"].astype(float))

    return air


def clean_heart_disease(df: pd.DataFrame) -> pd.DataFrame:
    heart = df.copy().replace("?", np.nan)
    for col in heart.columns:
        heart[col] = pd.to_numeric(heart[col], errors="coerce")
    heart = heart.drop_duplicates()

    if "target" in heart.columns:
        heart = heart.dropna(subset=["target"])

    for col in heart.columns:
        if heart[col].dtype.kind in "biufc":
            heart[col] = heart[col].fillna(heart[col].median())

    if "trestbps" in heart.columns:
        heart["trestbps"] = heart["trestbps"].clip(lower=80, upper=240)
    if "chol" in heart.columns:
        heart["chol"] = heart["chol"].clip(lower=100, upper=600)
    if "thalach" in heart.columns:
        heart["thalach"] = heart["thalach"].clip(lower=60, upper=220)
    if "oldpeak" in heart.columns:
        heart["oldpeak"] = heart["oldpeak"].clip(lower=0, upper=6)

    return heart


def integrate_to_sqlite(air: pd.DataFrame, heart: pd.DataFrame, db_path: Path) -> None:
    with sqlite3.connect(db_path) as conn:
        air.to_sql("air_quality", conn, if_exists="replace", index=False)
        heart.to_sql("heart_disease", conn, if_exists="replace", index=False)
        summary = pd.DataFrame({
            "table": ["air_quality", "heart_disease"],
            "rows": [len(air), len(heart)],
            "cols": [len(air.columns), len(heart.columns)]
        })
        summary.to_sql("data_inventory", conn, if_exists="replace", index=False)


def build_model(heart: pd.DataFrame) -> dict:
    if "target" not in heart.columns:
        raise ValueError("heart_disease dataset must include a target column")

    features = [c for c in heart.columns if c != "target"]
    X = heart[features]
    y = heart["target"].astype(int)

    stratify = y if y.nunique() > 1 else None
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=stratify
    )

    model = LogisticRegression(max_iter=1000, solver="liblinear")
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    metrics = {
        "accuracy": float(accuracy_score(y_test, preds)),
        "report": classification_report(y_test, preds, output_dict=True)
    }

    joblib.dump(model, OUT_DIR / "heart_model.pkl")

    return metrics


def main() -> None:
    air_raw = load_air_quality()
    heart_raw = load_heart_disease()

    air = clean_air_quality(air_raw)
    heart = clean_heart_disease(heart_raw)

    air.to_csv(OUT_DIR / "air_quality_clean.csv", index=False)
    heart.to_csv(OUT_DIR / "heart_disease_clean.csv", index=False)

    scaler = StandardScaler()
    feature_cols = [c for c in heart.columns if c != "target"]
    scaled = scaler.fit_transform(heart[feature_cols])
    scaled_df = pd.DataFrame(scaled, columns=[f"{c}_z" for c in feature_cols])
    scaled_df["target"] = heart["target"].values
    scaled_df.to_csv(OUT_DIR / "heart_scaled.csv", index=False)

    air_preview = air.head(50).copy()
    air_preview["source"] = "air"
    heart_preview = heart.head(50).copy()
    heart_preview["source"] = "heart"
    integration_preview = pd.concat(
        [air_preview, heart_preview], ignore_index=True, sort=False
    )
    integration_preview.to_csv(OUT_DIR / "integration_preview.csv", index=False)

    integrate_to_sqlite(air, heart, OUT_DIR / "health_env.db")

    metrics = build_model(heart)
    (OUT_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2))

    print("Pipeline complete. Outputs saved to", OUT_DIR)


if __name__ == "__main__":
    main()
