import pandas as pd
from tqdm import tqdm
import requests
import json

api_url = (
    "http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json"
)
filename_out = "weather.csv"


def load_data_from_api(url: str) -> list[dict]:
    # Загружаем данные о температуре воздуха в Сингапуре из API
    try:
        response = requests.get(url, headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            weather = response.json()
            return weather
    except json.JSONDecodeError as e:
        print(f"JSON Decode Eror: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error:{e}")


def convert_to_dataset_and_save_csv(
    weather: list[dict], fname: str
) -> pd.DataFrame | None:
    # Конвертируем данные в Dataframe и сохраняем в формате csv
    if weather:
        dataset = pd.DataFrame(weather)
        dataset.to_csv(fname, index=False)
        print("Данные о погоде сохранены")
        return dataset
    else:
        print("Ошибка! Нет данных о погоде для сохранения!")
    return None


if __name__ == "__main__":
    # Выводим данные о погоде
    print("Данные о погоде")
    weather_df = load_data_from_api(api_url)
    print(f"Получено данных: {len(weather_df)}")
    dataset = convert_to_dataset_and_save_csv(weather_df, filename_out)
    print(dataset.head(10))
