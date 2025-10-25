import pandas as pd
import re
import sqlite3
from sqlalchemy import create_engine, text

#Подключаемся к базе данных creds для дальнейшего использования её содержимого
with sqlite3.connect("creds.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM access LIMIT 1;")
    row_values = cursor.fetchone()
    col_names = [desc[0] for desc in cursor.description]
    creds = dict(zip(col_names, row_values))

#Записываем учетные данные
url = creds.get("url")
port = creds.get("port")
user = creds.get("user")
password = creds.get("pass")

#Подключаемся к базе данных homework
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{url}:{port}/homeworks", echo=False, future=True)
print("Подключение к homeworks прошло успешно")

#Читаем первые 100 строк нашего датасета с приведенными заранее типами(coversation_data)
df = pd.read_parquet("conversion_data.parquet").head(100)

#Загружаем датасет в базу данных homework
df.to_sql(
    name="korol",
    con=engine,
    schema="public",
    if_exists="replace",
    index=False,
)
print("Таблица public.korol создана и заполнена")

# Проверяем, что таблица успешно загружена и имеет 100 строк
with engine.begin() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM public.korol"))
        print(f"Записано строк: {result.fetchone()[0]}")
