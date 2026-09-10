import os
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv


# Load environment variables from the .env file in the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(dotenv_path=ENV_FILE)


YEAR = 2024
DATASET = "acs/acs5"

STATE_FIPS = "47"
COUNTY_FIPS = "157"

CENSUS_API_KEY = os.getenv("CENSUS_API_KEY")

if not CENSUS_API_KEY:
    raise RuntimeError(
        "CENSUS_API_KEY was not found.\n"
        "Make sure your .env file contains:\n"
        "CENSUS_API_KEY=your_actual_key"
    )


VARIABLES = {
    "NAME": "geography_name",
    "B01003_001E": "total_population",
    "B01002_001E": "median_age",
    "B19013_001E": "median_household_income",
    "B17001_001E": "poverty_universe",
    "B17001_002E": "population_below_poverty",
    "B23025_003E": "civilian_labor_force",
    "B23025_005E": "unemployed_population",
    "B25003_001E": "occupied_housing_units",
    "B25003_002E": "owner_occupied_units",
    "B25003_003E": "renter_occupied_units",
    "B25064_001E": "median_gross_rent",
    "B25077_001E": "median_home_value",
}


def download_acs_data() -> pd.DataFrame:
    """Download ACS 5-year tract data for Shelby County, Tennessee."""

    variable_codes = ",".join(VARIABLES.keys())

    url = f"https://api.census.gov/data/{YEAR}/{DATASET}"

    params = {
        "get": variable_codes,
        "for": "tract:*",
        "in": f"state:{STATE_FIPS} county:{COUNTY_FIPS}",
        "key": CENSUS_API_KEY,
    }

    print("Requesting Census data...")

    response = requests.get(
        url,
        params=params,
        timeout=60,
    )

    print(f"HTTP status: {response.status_code}")

    if not response.ok:
        print("\nCensus API returned an error:")
        print(response.text[:1000])
        response.raise_for_status()

    try:
        records = response.json()
    except requests.exceptions.JSONDecodeError as error:
        print("\nThe response was not valid JSON.")
        print("Response beginning:")
        print(repr(response.text[:1000]))

        raise RuntimeError(
            "Could not decode Census API response."
        ) from error

    if len(records) < 2:
        raise ValueError(
            "The Census API returned no tract records."
        )

    dataframe = pd.DataFrame(
        records[1:],
        columns=records[0],
    )

    dataframe = dataframe.rename(
        columns=VARIABLES
    )

    return dataframe


def save_raw_data(dataframe: pd.DataFrame) -> Path:
    """Save the downloaded records as a raw CSV file."""

    output_directory = PROJECT_ROOT / "data" / "raw"

    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path = (
        output_directory
        / "shelby_county_acs_2024_raw.csv"
    )

    dataframe.to_csv(
        output_path,
        index=False,
    )

    return output_path


def main() -> None:
    try:
        dataframe = download_acs_data()

        output_path = save_raw_data(
            dataframe
        )

        print("\nSUCCESS!")
        print(
            f"Downloaded {len(dataframe):,} census tracts."
        )
        print(
            f"Saved raw data to: {output_path}"
        )

        print("\nFirst 3 rows:")
        print(
            dataframe.head(3).to_string(
                index=False
            )
        )

    except requests.RequestException as error:
        print(
            f"\nCensus API request failed: {error}"
        )
        raise SystemExit(1) from error

    except (
        RuntimeError,
        ValueError,
        KeyError,
    ) as error:
        print(
            f"\nCould not process Census data: {error}"
        )
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()