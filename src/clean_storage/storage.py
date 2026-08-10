import sqlite3
from pathlib import Path

from pandas import DataFrame


def write_sql(df: DataFrame, path: Path):
    ignored_rows = []
    df_timestamp = df.copy()
    df_timestamp["date_heure"] = df_timestamp["date_heure"].dt.strftime("%Y-%m-%d %H:%M:%S")
    measure_columns = [c for c in df.columns if c != "date_heure"]
    measure_str = ", ".join(measure_columns)
    replace_columns = ["?" for c in df.columns]
    replace_str = ", ".join(replace_columns)

    conn = sqlite3.connect(path)
    conn.execute(f"CREATE TABLE IF NOT EXISTS measures (date_heure TEXT unique, {measure_str})")

    ordered_columns = ["date_heure", *measure_columns]
    df_reordered = df_timestamp[ordered_columns]

    for row in df_reordered.itertuples(index=False):
        try:
            conn.execute(f"INSERT INTO measures VALUES ({replace_str})", tuple(row))
        except sqlite3.IntegrityError:
            ignored_rows.append(row.date_heure)
    conn.commit()
    conn.close()
    return ignored_rows
