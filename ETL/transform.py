import pandas as pd


def convert_types(raw_data: pd.DataFrame) -> pd.DataFrame:
    data = raw_data.copy()

    category_columns = [
        "gender",
        "diagnostic",
        "itch",
        "grew",
        "hurt",
        "changed",
        "bleed",
        "elevation",
    ]
    for col in category_columns:
        if col in data.columns:
            data[col] = data[col].astype("category")
    return data
