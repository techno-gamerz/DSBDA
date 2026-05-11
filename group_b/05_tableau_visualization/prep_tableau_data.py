from pathlib import Path
import pandas as pd

BASE = Path(__file__).parent
DATA_DIR = BASE / "data"
OUT_DIR = BASE / "outputs"
OUT_DIR.mkdir(exist_ok=True)


def load_df(name: str, sample_name: str) -> pd.DataFrame:
    path = DATA_DIR / name
    sample = DATA_DIR / sample_name
    return pd.read_csv(path if path.exists() else sample)


def prep_iris() -> None:
    iris = load_df("iris.csv", "iris_sample.csv")
    iris["sepal_area"] = iris["sepal_length"] * iris["sepal_width"]
    iris["petal_area"] = iris["petal_length"] * iris["petal_width"]
    iris.to_csv(OUT_DIR / "iris_tableau.csv", index=False)


def prep_adult() -> None:
    adult = load_df("adult.csv", "adult_sample.csv")

    adult["age_group"] = pd.cut(
        adult["age"],
        bins=[0, 25, 35, 45, 55, 65, 100],
        labels=["<=25", "26-35", "36-45", "46-55", "56-65", "65+"]
    )

    adult["hours_group"] = pd.cut(
        adult["hours_per_week"],
        bins=[0, 20, 40, 60, 100],
        labels=["<=20", "21-40", "41-60", "60+"]
    )

    adult["income_binary"] = adult["income"].map({"<=50K": 0, ">50K": 1})
    adult["record_date"] = pd.date_range(
        start="2020-01-01", periods=len(adult), freq="D"
    )

    adult.to_csv(OUT_DIR / "adult_tableau.csv", index=False)

    edges = adult[["occupation", "education"]].dropna()
    edges.to_csv(OUT_DIR / "adult_network_edges.csv", index=False)


def main() -> None:
    prep_iris()
    prep_adult()
    print("Prepared Tableau files in", OUT_DIR)


if __name__ == "__main__":
    main()
