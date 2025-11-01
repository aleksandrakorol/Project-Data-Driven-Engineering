import pandas as pd

from pathlib import Path

def validate_load_data(raw_data: pd.DataFrame) -> None:

    if raw_data.empty:
        raise ValueError("Внимание! Датасет пуст!!!")

    needed_columns = [
        "patient_id",
        "lesion_id",
        "smoke",
        "drink",
        "background_father",
        "background_mother",
        "age",
        "pesticide",
        "gender",
        "skin_cancer_history",
        "cancer_history",
        "has_piped_water",
        "has_sewage_system",
        "fitspatrick",
        "region",
        "diagnostic",
        "itch",
        "grew",
        "hurt",
        "changed",
        "bleed",
        "elevation",
        "img_id",
        "biopsed",
    ]

    miss_columns = [col for col in needed_columns if col not in raw_data.columns]

    if miss_columns:
        raise ValueError(f"Внимание! В датасете не хватает колонок: {miss_columns}")

    return None

def load_scin_cancer_raw_data(place: str | Path) -> pd.DataFrame:
    raw_data = pd.read_csv(place)
    validate_load_data(raw_data)
    return raw_data

def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)

def raw_data_save_csv(raw_data: pd.DataFrame, root: Path) -> Path:
    raw_dir = root / "raw"
    ensure_dir(raw_dir)
    out_path = raw_dir / "Skin_cancer.csv"
    raw_data.to_csv(out_path, index=False)
    return out_path
