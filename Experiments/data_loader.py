import pandas as pd

File_ID = "18Jp35qlgM0XFDRkD2_xrt630cbXQr_qv"
# File_ID - ID файла (наш dataset) на Google Drive

File_url = f"https://drive.google.com/uc?id={File_ID}"
# File_url - расположение файла

raw_data = pd.read_csv(File_url)
# читаем файл

print(raw_data.head(10))
# выводим на экран первые 10 строк для проверки

print(raw_data.info())
# выводим информацию о данных датафрейма

# приступаем к приведению типов

conversation_data = pd.read_csv(File_url,
                         dtype={'gender': 'category',
                                'diagnostic': 'category',
                                'itch': 'category',
                                'grew': 'category',
                                'hurt': 'category',
                                'changed': 'category',
                                'bleed': 'category',
                                'elevation': 'category'
                                })

print("Типы данных после приведения\n")
print(conversation_data.dtypes)

# выводим информацию о данных датафрейма после приведения типов

raw_data.to_parquet("conversion_data.parquet", index=False)
# сохраняем обработанные данные в формате parquet







