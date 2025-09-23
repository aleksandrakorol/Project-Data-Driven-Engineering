import pandas as pd

File_ID = "1HBtpv8kD75_lFkkOiwhrYzz9TcDml_OP"
# File_ID - ID файла (наш dataset) на Google Drive

File_url = f"https://drive.google.com/uc?id={File_ID}"
# File_url - расположение файла

raw_data = pd.read_csv(File_url)
# читаем файл

print(raw_data.head(10))
# выводим на экран первые 10 строк для проверки
