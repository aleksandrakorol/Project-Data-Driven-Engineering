import pandas as pd


def convert_types(raw_data: pd.DataFrame) -> pd.DataFrame:
    data = raw_data.copy()

    conversation_data = pd.read_csv(
        data,
        dtype={
            "gender": "category",
            "diagnostic": "category",
            "itch": "category",
            "grew": "category",
            "hurt": "category",
            "changed": "category",
            "bleed": "category",
            "elevation": "category",
        },
    )
    conversation_data.dtypes
    return conversation_data


def clean_convert_data_from_NaN(conversation_data: pd.DataFrame) -> pd.DataFrame:

    change_column = [
        "background_mother",
        "background_father",
        "gender",
        "fitsfitspatrick",
    ]

    for col in change_column:
        conversation_data[change_column] = (
            conversation_data[change_column].cat.add_categories("UNK").fillna("UNK")
        )

    delete_column = ["diametric_1", "diametric_2"]

    for col in delete_column:
        clean_data = conversation_data.drop([delete_column], axis=1)

    return clean_data
