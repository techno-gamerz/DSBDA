from pathlib import Path
import pandas as pd

BASE = Path(__file__).parent
DATA_DIR = BASE / "data"
OUT_DIR = BASE / "outputs"
OUT_DIR.mkdir(exist_ok=True)


def load_primary() -> pd.DataFrame:
    primary = DATA_DIR / "facebook_metrics.csv"
    sample = DATA_DIR / "facebook_metrics_sample.csv"
    return pd.read_csv(primary if primary.exists() else sample)


def main() -> None:
    df = load_primary()
    df2 = pd.read_csv(DATA_DIR / "facebook_metrics_secondary_sample.csv")

    subset_cols = df[[
        "Page total likes",
        "Type",
        "Post Month",
        "Lifetime Post Total Reach"
    ]]

    subset_rows = df[df["Type"] == "Photo"].head(5)

    merged = df.merge(df2, on="Post Month", how="left")

    sorted_df = df.sort_values(["Page total likes", "Post Month"], ascending=[False, True])

    transposed = (
        df[["Post Month", "Post Weekday", "Lifetime Post Total Reach"]]
        .head(5)
        .set_index("Post Month")
        .T
    )

    reshaped = df.melt(
        id_vars=["Type", "Post Month"],
        value_vars=["Lifetime Post Total Reach", "Lifetime Engaged Users"],
        var_name="metric",
        value_name="value"
    )

    cast_wide = (
        reshaped.pivot_table(
            index=["Type", "Post Month"],
            columns="metric",
            values="value",
            aggfunc="mean"
        )
        .reset_index()
    )
    cast_wide.columns = [str(c) for c in cast_wide.columns]

    subset_cols.to_csv(OUT_DIR / "subset_cols.csv", index=False)
    subset_rows.to_csv(OUT_DIR / "subset_rows.csv", index=False)
    merged.to_csv(OUT_DIR / "merged.csv", index=False)
    sorted_df.to_csv(OUT_DIR / "sorted.csv", index=False)
    transposed.to_csv(OUT_DIR / "transposed.csv")
    reshaped.to_csv(OUT_DIR / "reshaped.csv", index=False)
    cast_wide.to_csv(OUT_DIR / "cast_wide.csv", index=False)

    print("Saved outputs to", OUT_DIR)


if __name__ == "__main__":
    main()
