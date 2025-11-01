import pandas as pd
import os

from pathlib import Path

from dotenv import load_dotenv

from sqlalchemy import create_engine, text

load_dotenv()


def save_data_parquet(clean_data: pd.DataFrame, root: Path) -> Path:
    processed_dir = root / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)
    out_path = processed_dir / "clean_data.parquet"
    clean_data.to_parquet(out_path, index=False)
    return out_path


def validate_output(clean_data: pd.DataFrame) -> None:
    if clean_data.empty:
        raise ValueError("Внимание! Выходные данные пусты!!!")

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
        "diametric_1",
        "diametric_2",
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

    miss_columns = [col for col in needed_columns if col not in clean_data.columns]

    if miss_columns:
        raise ValueError(f"Внимание! В датасете не хватает колонок: {miss_columns}")

    clean_data.dtypes

    return None


def get_connect_database():
    url = os.getenv("url")
    port = os.getenv("port")
    user = os.getenv("user")
    password = os.getenv("pass")

    # Подключаемся к базе данных homework
    engine = create_engine(
        f"postgresql+psycopg2://{user}:{password}@{url}:{port}/homeworks",
        echo=False,
        future=True,
    )
    print("Подключение к homeworks прошло успешно")
    return engine


def load_dataset_in_database():
    df = pd.read_parquet("conversion_data.parquet").head(100)
    # Загружаем датасет в базу данных homework
    df.to_sql(
        name="korol",
        con=get_connect_database,
        schema="public",
        if_exists="replace",
        index=False,
    )
    print("Таблица public.korol создана и заполнена")
    return None


def check_table_in_database():
    with get_connect_database.begin() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM public.korol"))
        print(f"Записано строк: {result.fetchone()[0]}")
    return result
