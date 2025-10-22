import re
import pandas as pd
import sqlite3
from sqlalchemy import create_engine, text

with sqlite3.connect("creds.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM access LIMIT 1;")
    row_values = cursor.fetchone()
    col_names = [desc[0] for desc in cursor.description]
    creds = dict(zip(col_names, row_values))

url = creds.get("url")
port = creds.get("port")
user = creds.get("user")
password = creds.get("pass")

conn_homeworks = (
    f"postgresql+psycopg2://{user}:{password}@{url}:{port}/homeworks"
)
engine = create_engine(conn_homeworks, echo=False, future=True)
print("Подключились к homeworks")

df = pd.read_parquet("conversion_data.parquet").head(100)

df.to_sql(
    name="korol",
    con=engine,
    schema="public",
    if_exists="replace",
    index=False,
)
print("Таблица public.korol создана и заполнена")
