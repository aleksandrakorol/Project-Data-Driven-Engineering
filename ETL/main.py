import argparse
import sys
from pathlib import Path

from .extract import load_scin_cancer_raw_data, raw_data_save_csv, ensure_dir
from .transform import convert_types
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
    ensure_dir(root())

    print("#### Запуск ETL процесса ####")

    print("\n1. Загрузка данных\n")
    try:
        raw_data = load_scin_cancer_raw_data(place)
        save_raw = raw_data_save_csv(raw_data, root())
        print("\nЗагузка прошла успешно!\n")
    except Exception as e:
        print(f"\nОшибка при загрузке данных: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)

    print("\n2. Преобразование данных\n")
    try:
        conversation_data = convert_types(raw_data)
        print("\nПреобразование прошло успешно!\n")
    except Exception as e:
        print(f"\nОшибка при преобразовании данных: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)

    print("\n3. Выгрузка датасета в базу данных\n")
    try:
        save_parquet = save_data_parquet(conversation_data, root())
        validate_parquet = validate_output(conversation_data)
        engine = get_connect_database()
        load_to_db = load_dataset_in_database(engine)
        checking = check_table_in_database(engine)
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
