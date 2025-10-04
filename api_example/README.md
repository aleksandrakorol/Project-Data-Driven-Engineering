# API
# Used API
https://www.hko.gov.hk/en/abouthko/opendata_intro.htm
Description:
This API offers a comprehensive suite of weather information, earthquake details, and climate data.
# API Reading 
# Preparation
Installation Miniconda from official website for your system: 
https://www.anaconda.com/docs/getting-started/miniconda/install
# Creation enviromental variables (conda + poetry)
1. conda create -n api_env python=3.13
2. conda activate api_env
3. pip install poetry
4. poetry new api_project
5. cd api_project
6. poetry add pandas numpy requests tqdm
7. poetry install --no-root
# 
# Activation
- Write activate code:

python api_reader.py

- Result comand print(raw_data.head(10)):

<img width="1453" height="1007" alt="Снимок экрана" src="https://github.com/user-attachments/assets/3c14ba9b-4880-4e3a-b9df-c57601684768" />

