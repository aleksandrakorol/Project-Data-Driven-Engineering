# Project-Skin-Cancer
В ходе данного проекта будет рассмотен датасет по кожным поражениям. 

В частности, выделяется две основные группы: 
- болезни рака кожи (базальноклеточная карцинома BCC, плоскоклеточная карцинома MEL, болезнь Боуэна SCC);
- кожные заболевания (актинический кератоз ACK, невус NEV, себорейный кератоз SEK).

<img width="700" height="525" alt="image" src="https://github.com/user-attachments/assets/480e1f75-c9ea-4afe-9319-a437fec3b31c" />

# Dataset
https://www.kaggle.com/datasets/mahdavi1202/skin-cancer

https://drive.google.com/drive/folders/1HBtpv8kD75_lFkkOiwhrYzz9TcDml_OP?usp=sharing

# Project Structure
 ```
├── README.md          <- The top-level README for developers using this project.
├── pyproject.toml     <- Project configuration file with package metadata
├── ETL                <- ETL project.
|   │
|   ├── __init__.py             
|   ├── extract.py
|   ├── load.py 
|   ├── transform.py
|   └── main.py
├── notebooks          <- Jupyter notebooks.
|   └── EDA.ipynb
└── Experiments
    ├── data_load.py
    ├── api_example                
    │   ├── README.md
    │   ├── api_reader.py     
    │   └── pyproject.toml
    └── src                  
        └── write_to_db.py
 ```
# Project activation guide 
# Preparation
Installation Miniconda from official website for your system: 
https://www.anaconda.com/docs/getting-started/miniconda/install
# Creation enviromental variables (conda + poetry)
 ```
1. conda create -n my_env python=3.13
2. conda activate my_env
3. pip install poetry
4. poetry new project_scin_cancer
5. cd project_scin_cancer
6. poetry add jupyter pandas matplotlib numpy wget
7. poetry install --no-root
 ```
# Activation
- Write activate code:
 ```
python data_loader.py
 ```
- Result comand print(raw_data.head(10)):

<img width="1453" height="1007" alt="Снимок экрана" src="https://github.com/user-attachments/assets/3c14ba9b-4880-4e3a-b9df-c57601684768" />

# DTypes
Watch what all the data types are in a dataframe, use 
print(raw_data.info())

Result:
<img width="729" height="934" alt="Снимок экрана (549)" src="https://github.com/user-attachments/assets/579c2309-dd2a-4685-bd6c-8ec600762c4c" />

Change types in a dataframe

Watch what all the data types are in a dataframe after conversation, use 
print(raw_data.info())

Result:
<img width="775" height="857" alt="Снимок экрана (550)" src="https://github.com/user-attachments/assets/6c059b44-3568-46b2-970b-a940b3c82a2c" />

Save conversation data on parquet
 ```
raw_data.to_parquet("conversion_data.parquet", index=False)
 ```
# EDA
Visualisation EDA:

https://nbviewer.org/github/aleksandrakorol/Project-Data-Driven-Engineering/blob/main/notebooks/EDA.ipynb

# ETL

# ETL Structure
 ```
ETL
│
├── __init__.py
├── extract.py
├── transform.py
├── load.py 
└── main.py                
```
- DB connection uses environment variables: host, port, name, user, password.

# Runing
If you want to work with dataset in GoogleDrive: 
 ```
python -m etl.main --place https://drive.google.com/uc?id=18Jp35qlgM0XFDRkD2_xrt630cbXQr_qv --table-name korol
 ```
or

If you want to work with uploading dataset:
 ```
python -m etl.main --place data_engineering/data/raw/Skin_cancer.csv --table-name korol
 ```

- EXTRACT: upload and save dataset
- TRANSFORM: convert dtypes and clean from NaN
- LOAD: write to parquet and load to database
