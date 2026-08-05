# clean.py

import pandas as pd

def clean_data(results: list[dict]) -> pd.DataFrame:
    df = pd.DataFrame(results)
    df["date_heure"] = pd.to_datetime(df["date_heure"])
    df = df.drop(["date", "heure"], axis=1)
    # NaN
    print(df.isna().sum())
    # anomalies flaguées
    return df