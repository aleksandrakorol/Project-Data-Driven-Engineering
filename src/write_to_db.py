import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

#Загружаем переменные из .env
load_dotenv()

url = os.getenv("url")
port = os.getenv("port")
user = os.getenv("user")
password = os.getenv("pass")

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
