import argparse
import sys
from pathlib import Path

from .extract import load_scin_cancer_raw_data, validate_load_data, raw_data_save_csv
from .transform import convert_types, clean_convert_data_from_NaN
from .load import (
    save_data_parquet,
    validate_output,
    get_connect_database,
    load_dataset_in_database,
    check_table_in_database,
)


def root() -> Path:
    return Path(__file__).resolve().parents[1] / "data"


def etl_run(place: str, table_name: str) -> None:
    root()

    print("#### Запуск ETL процесса ####")

    print("\nЗагрузка данных\n")
    try:
        raw_data = load_scin_cancer_raw_data(place)
        validate_raw = validate_load_data(raw_data)
        save_raw_csv = raw_data_save_csv(raw_data, root)
    except Exception as e:
        print(f"\nОшибка при загрузке данных: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    print("\nПреобразование данных\n")
    try:
        conversation_data = convert_types(raw_data)
        clean_data = clean_convert_data_from_NaN(conversation_data)
    except Exception as e:
        print(f"\nОшибка при преобразовании данных: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    print("\n Выгрузка датасета в базу данных\n")
    try:
        save_parquet = save_data_parquet(clean_data, root)
        validate_parquet = validate_output(clean_data)
        engine = get_connect_database()
        load_to_db = load_dataset_in_database()
        checking = check_table_in_database()
    except Exception as e:
        print(f"\nОшибка при выгузке датасета: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


def parse_args() -> argparse.Namespace:
    pars = argparse.ArgumentParser(
        description="Запуск ETL для обработки данных поражений кожи"
    )
    pars.add_argument(
        "--place",
        required=True,
        help="Место откуда берется датасет его Path или URL",
    )
    pars.add_argument(
        "--table-name",
        help="Имя таблицы в базе данных",
    )
    return pars.parse_args()


def main() -> None:
    args = parse_args()
    etl_run(place=args.place, table_name=args.table_name)


if __name__ == "__main__":
    main()
