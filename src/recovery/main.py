import json
from pathlib import Path

from src.clean_storage.storage import write_sql
from src.cleaning.clean import clean_data
from src.raw_storage.storage import write_raw
from src.recovery.explore import fetch_by_year


def main(year: int, url: str):
    path_raw = Path("data") / "raw" / f"{year}.json"
    path_clean = Path("data") / "clean" / "measures.db"
    excluded_columns = {"perimetre", "nature", "date_heure", "prevision_j1", "prevision_j"}
    if path_raw.exists():
        with open(path_raw) as f:
            data = json.load(f)
    else:
        data = fetch_by_year(url, year)
        write_raw(data, path_raw)
    df = clean_data(data, excluded_columns)
    print(write_sql(df, path_clean))
    return df


if __name__ == "__main__":
    url = "https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/eco2mix-national-cons-def/records"
    df = main(2022, url)
    # print(df.duplicated(subset=["date_heure"]))
    # print(df.duplicated(subset=["date_heure"]).sum())
    # print(df.head())
    # print(df["date_heure"].dt.minute.value_counts())
    # print(df.groupby(df["date_heure"].dt.minute)["consommation"].apply(lambda x: x.isna().sum()))
