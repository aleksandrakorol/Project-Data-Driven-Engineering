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
