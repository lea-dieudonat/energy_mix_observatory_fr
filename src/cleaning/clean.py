# clean.py

import pandas as pd

def clean_data(results: list[dict], excluded_columns) -> pd.DataFrame:
    df = pd.DataFrame(results)
    df["date_heure"] = pd.to_datetime(df["date_heure"])
    df = df.drop(["date", "heure"], axis=1)
    measure_columns = list(set(df.columns) - excluded_columns)
    df = df.dropna(how="all", subset=measure_columns)
    print(df.isna().sum())
    return df