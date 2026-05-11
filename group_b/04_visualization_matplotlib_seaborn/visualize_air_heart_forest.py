from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

BASE = Path(__file__).parent
DATA_DIR = BASE / "data"
OUT_DIR = BASE / "outputs"
OUT_DIR.mkdir(exist_ok=True)


def load_df(name: str, sample_name: str) -> pd.DataFrame:
    path = DATA_DIR / name
    sample = DATA_DIR / sample_name
    return pd.read_csv(path if path.exists() else sample)


def plot_air_quality() -> None:
    air = load_df("air_quality.csv", "air_quality_sample.csv")
    air["datetime"] = pd.to_datetime(
        air["Date"].astype(str) + " " + air["Time"].astype(str),
        errors="coerce",
        dayfirst=True
    )

    plt.figure(figsize=(8, 4))
    plt.plot(air["datetime"], air["CO"], color="steelblue")
    plt.title("Air quality - CO over time")
    plt.xlabel("Datetime")
    plt.ylabel("CO")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "air_co_timeseries.png", dpi=150)
    plt.close()


def plot_heart_corr() -> None:
    heart = load_df("heart_disease.csv", "heart_disease_sample.csv")
    heart = heart.apply(pd.to_numeric, errors="coerce")
    corr = heart.corr(numeric_only=True)

    plt.figure(figsize=(7, 6))
    sns.heatmap(corr, cmap="Blues", linewidths=0.5)
    plt.title("Heart disease - correlation heatmap")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "heart_corr_heatmap.png", dpi=150)
    plt.close()


def plot_forest_area() -> None:
    forest = load_df("forest_fires.csv", "forest_fires_sample.csv")
    forest["area"] = pd.to_numeric(forest["area"], errors="coerce").fillna(0)
    avg_by_month = forest.groupby("month", as_index=False)["area"].mean()

    plt.figure(figsize=(6, 4))
    sns.barplot(data=avg_by_month, x="month", y="area", color="seagreen")
    plt.title("Forest fires - avg burned area by month")
    plt.xlabel("Month")
    plt.ylabel("Average area")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "forest_area_by_month.png", dpi=150)
    plt.close()


def main() -> None:
    plot_air_quality()
    plot_heart_corr()
    plot_forest_area()
    print("Plots saved to", OUT_DIR)


if __name__ == "__main__":
    main()
