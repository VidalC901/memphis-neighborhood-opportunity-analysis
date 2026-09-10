from pathlib import Path
import sqlite3

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

CSV_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "shelby_county_opportunity_data.csv"
)

DB_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "memphis_opportunity.db"
)


def main() -> None:
    df = pd.read_csv(CSV_FILE)

    connection = sqlite3.connect(DB_FILE)

    df.to_sql(
        "census_tract_metrics",
        connection,
        if_exists="replace",
        index=False,
    )

    connection.close()

    print("SUCCESS!")
    print("Created SQLite database:")
    print(DB_FILE)
    print(f"Loaded {len(df):,} rows into census_tract_metrics.")


if __name__ == "__main__":
    main()