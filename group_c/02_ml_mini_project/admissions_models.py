from pathlib import Path
import json

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

BASE = Path(__file__).parent
DATA_DIR = BASE / "data"
OUT_DIR = BASE / "outputs"
OUT_DIR.mkdir(exist_ok=True)


def load_data() -> pd.DataFrame:
    path = DATA_DIR / "admissions.csv"
    sample = DATA_DIR / "admissions_sample.csv"
    df = pd.read_csv(path if path.exists() else sample)

    # Normalize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    if "serial_no." in df.columns:
        df = df.drop(columns=["serial_no."])
    if "serial_no" in df.columns:
        df = df.drop(columns=["serial_no"])
    if "chance_of_admit" not in df.columns:
        for c in df.columns:
            if "chance" in c and "admit" in c:
                df = df.rename(columns={c: "chance_of_admit"})
                break
    return df


def train_models(df: pd.DataFrame) -> dict:
    if "chance_of_admit" not in df.columns:
        raise ValueError("Dataset must include Chance of Admit column")

    X = df.drop(columns=["chance_of_admit"])
    y = df["chance_of_admit"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    models = {
        "linear": Pipeline([("scale", StandardScaler()), ("model", LinearRegression())]),
        "random_forest": RandomForestRegressor(n_estimators=200, random_state=42),
        "gboost": GradientBoostingRegressor(random_state=42)
    }

    results = {}
    best_name = None
    best_rmse = None
    best_model = None

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        rmse = mean_squared_error(y_test, preds, squared=False)
        r2 = r2_score(y_test, preds)
        results[name] = {"rmse": float(rmse), "r2": float(r2)}

        if best_rmse is None or rmse < best_rmse:
            best_rmse = rmse
            best_name = name
            best_model = model

    joblib.dump(best_model, OUT_DIR / "best_model.pkl")

    pred_df = pd.DataFrame({
        "actual": y_test.values,
        "predicted": best_model.predict(X_test)
    })
    pred_df.to_csv(OUT_DIR / "predictions_sample.csv", index=False)

    return {"best_model": best_name, "metrics": results}


def main() -> None:
    df = load_data()
    report = train_models(df)
    (OUT_DIR / "metrics.json").write_text(json.dumps(report, indent=2))
    print("Training complete. Outputs saved to", OUT_DIR)


if __name__ == "__main__":
    main()
