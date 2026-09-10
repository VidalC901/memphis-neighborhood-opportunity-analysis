from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "shelby_county_acs_2024_raw.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "shelby_county_opportunity_data.csv"
)


NUMERIC_COLUMNS = [
    "total_population",
    "median_age",
    "median_household_income",
    "poverty_universe",
    "population_below_poverty",
    "civilian_labor_force",
    "unemployed_population",
    "occupied_housing_units",
    "owner_occupied_units",
    "renter_occupied_units",
    "median_gross_rent",
    "median_home_value",
]


def safe_percentage(
    numerator: pd.Series,
    denominator: pd.Series,
) -> pd.Series:
    return (
        numerator
        .div(denominator.where(denominator != 0))
        .mul(100)
        .round(2)
    )


def clean_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    cleaned = dataframe.copy()

    # Convert Census numeric fields from text to numbers
    for column in NUMERIC_COLUMNS:
        cleaned[column] = pd.to_numeric(
            cleaned[column],
            errors="coerce",
        )

        # Census uses large negative sentinel values
        # for unavailable estimates.
        cleaned.loc[
            cleaned[column] < 0,
            column
        ] = pd.NA

    # Calculate useful analytics metrics
    cleaned["poverty_rate"] = safe_percentage(
        cleaned["population_below_poverty"],
        cleaned["poverty_universe"],
    )

    cleaned["unemployment_rate"] = safe_percentage(
        cleaned["unemployed_population"],
        cleaned["civilian_labor_force"],
    )

    cleaned["homeownership_rate"] = safe_percentage(
        cleaned["owner_occupied_units"],
        cleaned["occupied_housing_units"],
    )

    cleaned["rent_to_income_ratio"] = (
        (cleaned["median_gross_rent"] * 12)
        .div(cleaned["median_household_income"])
        .round(3)
    )

    # Create unique Census tract identifier
    cleaned["tract_geoid"] = (
        cleaned["state"].astype(str).str.zfill(2)
        + cleaned["county"].astype(str).str.zfill(3)
        + cleaned["tract"].astype(str).str.zfill(6)
    )

    cleaned = cleaned.sort_values(
        "tract_geoid"
    ).reset_index(drop=True)

    return cleaned


def main() -> None:
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Raw Census file not found: {RAW_FILE}"
        )

    dataframe = pd.read_csv(
        RAW_FILE,
        dtype={
            "state": str,
            "county": str,
            "tract": str,
        },
    )

    cleaned = clean_data(dataframe)

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    cleaned.to_csv(
        OUTPUT_FILE,
        index=False,
    )

    print("SUCCESS!")
    print(f"Cleaned {len(cleaned):,} census tracts.")
    print(f"Saved cleaned data to: {OUTPUT_FILE}")

    print("\nMissing values after cleaning:")
    print(
        cleaned[NUMERIC_COLUMNS]
        .isna()
        .sum()
        .sort_values(ascending=False)
    )

    print("\nPreview:")
    preview_columns = [
        "tract_geoid",
        "geography_name",
        "median_household_income",
        "poverty_rate",
        "unemployment_rate",
        "homeownership_rate",
        "median_gross_rent",
        "rent_to_income_ratio",
    ]

    print(
        cleaned[preview_columns]
        .head(10)
        .to_string(index=False)
    )


if __name__ == "__main__":
    main()