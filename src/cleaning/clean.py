# clean.py

import pandas as pd
from src.recovery.explore import paginate

def clean_data(results: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(results)
    # datetime
    df["date_heure"] = pd.to_datetime(df["date_heure"])
    df = df.drop(["date", "heure"], axis=1)
    # NaN
    print(df.isna().sum())
    # anomalies flaguées

    return df

if __name__ == "__main__":
    #url = 'https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/eco2mix-national-tr/records'
    url = "https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/eco2mix-national-cons-def/records"
    refine = {"date_heure":"2022"}
    result_list = paginate(url, refine=refine)
    df = clean_data(result_list)
    print(df.head())