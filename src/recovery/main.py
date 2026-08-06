from pathlib import Path
import json

from src.cleaning.clean import clean_data
from src.raw_storage.storage import write_raw
from src.recovery.explore import fetch_by_year

def main(year: int, url: str):
    path = Path("src") / "raw_storage" / f"{year}.json"
    excluded_columns = {"perimetre", "nature", "date_heure", "prevision_j1", "prevision_j"}
    if path.exists():
        with open(path, 'r') as f:
            data = json.load(f)
    else:
        data = fetch_by_year(url, year)
        write_raw(data, path)
    df = clean_data(data, excluded_columns)
    return df

if __name__== "__main__":
    url = "https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/eco2mix-national-cons-def/records"
    df = main(2022, url)
    print(df.head())
    print(df["date_heure"].dt.minute.value_counts())
    print(df.groupby(df["date_heure"].dt.minute)["consommation"].apply(lambda x: x.isna().sum()))