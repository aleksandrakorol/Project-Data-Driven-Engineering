import pandas as pd
import os

from pathlib import Path
from dotenv import load_dotenv
from .extract import ensure_dir
from sqlalchemy import create_engine, text, MetaData, Table, Column

load_dotenv()


def save_data_parquet(clean_data: pd.DataFrame, root: Path) -> Path:
    processed_dir = root / "processed"
    ensure_dir(processed_dir)
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

    connect_url = f"postgresql+psycopg2://{user}:{password}@{url}:{port}/homeworks"

    print("Подключение к homeworks прошло успешно")
    return create_engine(connect_url)


def load_dataset_in_database(engine, table_name: str, out_path: Path):

    df = pd.read_parquet(out_path).head(100)

    # Загружаем датасет в базу данных homework
    df.to_sql(
        table_name,
        con=engine,
        schema="public",
        if_exists="replace",
        index=False,
    )

    with engine.begin() as connection:
        connection.execute(
            text(
                f'ALTER TABLE public."{table_name}" DROP CONSTRAINT IF EXISTS {table_name}_pkey'
            )
        )
        connection.execute(
            text(f'ALTER TABLE public."{table_name}" ADD PRIMARY KEY (patient_id)')
        )

    print("Таблица public.korol создана и заполнена")
    return None


def check_table_in_database(engine):
    with engine.begin() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM public.korol"))
        print(f"Записано строк: {result.fetchone()[0]}")
    return result
