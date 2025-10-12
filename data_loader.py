import pandas as pd

File_ID = "1RtRInobd1gXIJ6yMKnNjgi3QjuUZo9kW"
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

# patient_id не требует приведения
# lesion_id не требует приведения
raw_data["smoke"] = raw_data["smoke"].astype("bool")
raw_data["drink"] = raw_data["drink"].astype("bool")
raw_data["background_father"] = raw_data["background_father"].astype("category")
raw_data["background_mother"] = raw_data["background_mother"].astype("category")
# age не требует приведения
raw_data["pesticide"] = raw_data["pesticide"].astype("bool")
raw_data["gender"] = raw_data["gender"].astype("category")
raw_data["skin_cancer_history"] = raw_data["skin_cancer_history"].astype("bool")
raw_data["cancer_history"] = raw_data["cancer_history"].astype("bool")
raw_data["has_piped_water"] = raw_data["has_piped_water"].astype("bool")
raw_data["has_sewage_system"] = raw_data["has_sewage_system"].astype("bool")
# fitspatrick не требует приведения
raw_data["region"] = raw_data["region"].astype("category")
# diameter_1 не требует приведения
# diameter_2 не требует приведения
raw_data["diagnostic"] = raw_data["diagnostic"].astype("category")
raw_data["itch"] = raw_data["itch"].astype("bool")
raw_data["grew"] = raw_data["grew"].astype("bool")
raw_data["hurt"] = raw_data["hurt"].astype("bool")
raw_data["changed"] = raw_data["changed"].astype("bool")
raw_data["bleed"] = raw_data["bleed"].astype("bool")
raw_data["elevation"] = raw_data["elevation"].astype("bool")
# img_id не требует приведения
# biopsed не требует приведения

print(raw_data.info())
# выводим информацию о данных датафрейма после приведения типов

raw_data.to_parquet("conversion_data.parquet", index=False)
# сохраняем обработанные данные в формате parquet



