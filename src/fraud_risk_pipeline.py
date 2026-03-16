import pandas as pd
import numpy as np
from glob import glob
from pathlib import Path
from tqdm import tqdm


# ================================
# PATH CONFIGURATION
# ================================

DATA_DIR = Path("data")
INSPECTIONS_DIR = DATA_DIR / "raw/inspections"
GEOSPATIAL_FILE = DATA_DIR / "raw/geospatial_data.parquet"

OUTPUT_DIR = Path("outputs")


# ================================
# LOAD DATA
# ================================

def load_inspections(folder):

    files = glob(f"{folder}/*.parquet")

    dfs = []

    for file in tqdm(files, desc="Loading inspection files"):
        df = pd.read_parquet(file)
        dfs.append(df)

    inspections = pd.concat(dfs, ignore_index=True)

    return inspections


def load_geospatial_data(file):

    geo = pd.read_parquet(file)

    geo = geo.drop_duplicates(subset=["SERVICE_POINT_ID"])

    return geo


# ================================
# CREATE TARGET
# ================================

def create_target_variable(df):

    df["TARGET"] = np.where(
        df["INSPECTION_RESULT"].str.contains("CONFIRMED", case=False, na=False),
        "Fraud",
        "Normal"
    )

    return df


# ================================
# GEOHASH STATISTICS
# ================================

def compute_geohash_statistics(df):

    geohash_cols = [
        "GEOHASH5",
        "GEOHASH6",
        "GEOHASH7",
        "GEOHASH8",
        "NEIGHBORHOOD",
        "CITY"
    ]

    for geohash in geohash_cols:

        df[f"{geohash}_TOTAL"] = df.groupby(geohash)["INSPECTION_ID"].transform("count")

        fraud_count = (
            df[df["TARGET"] == "Fraud"]
            .groupby(geohash)["INSPECTION_ID"]
            .count()
        )

        df[f"{geohash}_FRAUD"] = df[geohash].map(fraud_count).fillna(0)

        df[f"{geohash}_RATE"] = (
            df[f"{geohash}_FRAUD"] /
            df[f"{geohash}_TOTAL"]
        ).fillna(0)

    return df


# ================================
# FRAUD ESTIMATION
# ================================

def estimate_fraud_probability(row):

    if row["GEOHASH8_TOTAL"] > 3 and row["GEOHASH8_FRAUD"] > 1:
        return row["GEOHASH8_RATE"]

    if row["GEOHASH7_TOTAL"] > 3 and row["GEOHASH7_FRAUD"] > 1:
        return row["GEOHASH7_RATE"]

    if row["GEOHASH6_TOTAL"] > 5 and row["GEOHASH6_FRAUD"] > 1:
        return row["GEOHASH6_RATE"]

    if row["GEOHASH5_TOTAL"] > 10 and row["GEOHASH5_FRAUD"] > 1:
        return row["GEOHASH5_RATE"]

    if row["NEIGHBORHOOD_TOTAL"] > 10 and row["NEIGHBORHOOD_FRAUD"] > 1:
        return row["NEIGHBORHOOD_RATE"]

    if row["CITY_TOTAL"] > 20 and row["CITY_FRAUD"] > 1:
        return row["CITY_RATE"]

    return 0.0


# ================================
# MAIN PIPELINE
# ================================

def run_pipeline():

    print("Loading inspection data...")
    inspections = load_inspections(INSPECTIONS_DIR)

    print("Loading geospatial data...")
    geo = load_geospatial_data(GEOSPATIAL_FILE)

    print("Creating target variable...")
    inspections = create_target_variable(inspections)

    print("Computing geospatial statistics...")
    inspections = compute_geohash_statistics(inspections)

    print("Merging datasets...")
    dataset = geo.merge(inspections, on="SERVICE_POINT_ID", how="left")

    print("Estimating fraud probability...")
    dataset["FRAUD_RISK_SCORE"] = dataset.apply(
        estimate_fraud_probability,
        axis=1
    )

    OUTPUT_DIR.mkdir(exist_ok=True)

    output_file = OUTPUT_DIR / "fraud_risk_scores.parquet"

    dataset[
        ["SERVICE_POINT_ID", "FRAUD_RISK_SCORE"]
    ].to_parquet(output_file, index=False)

    print("Pipeline completed.")
    print(f"Output saved to: {output_file}")


# ================================
# EXECUTION
# ================================

if __name__ == "__main__":

    run_pipeline() 
