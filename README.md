# Project-Skin-Cancer
# Dataset
https://www.kaggle.com/datasets/mahdavi1202/skin-cancer

https://drive.google.com/drive/folders/1HBtpv8kD75_lFkkOiwhrYzz9TcDml_OP?usp=sharing
# Project activation guide 
# Preparation
Installation Miniconda from official website for your system: 
https://www.anaconda.com/docs/getting-started/miniconda/install
# Creation enviromental variables (conda + poetry)
1. conda create -n my_env python=3.13
2. conda activate my_env
3. pip install poetry
4. poetry new project_scin_cancer
5. cd project_scin_cancer
6. poetry add jupyter pandas matplotlib numpy wget
7. poetry install --no-root
# Activation
- Write activate code:

python data_loader.py

- Result comand print(raw_data.head(10)):

<img width="1453" height="1007" alt="Снимок экрана" src="https://github.com/user-attachments/assets/3c14ba9b-4880-4e3a-b9df-c57601684768" />

# DTypes
Watch what all the data types are in a dataframe, use 
print(raw_data.info())

Result:
<img width="1920" height="940" alt="Снимок экрана (532)" src="https://github.com/user-attachments/assets/d5ba9339-cea5-4a1c-b3e5-92dc286568be" />

Change types in a dataframe

Watch what all the data types are in a dataframe after conversation, use 
print(raw_data.info())

Result:
<img width="1342" height="837" alt="2025-10-19_22-24-01" src="https://github.com/user-attachments/assets/7ca81e2c-beda-4c43-a8a6-ed3b11305313" />

Save conversation data on parquet
raw_data.to_parquet("conversion_data.parquet", index=False)

# EDA
Visualisation EDA:

https://nbviewer.org/github/aleksandrakorol/Project-Data-Driven-Engineering/blob/main/notebooks/EDA.ipynb
