# API
# Used API
http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json

Description:

Weather forecasts for astronomy.
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

- Result:

<img width="1046" height="392" alt="Снимок экрана (536)" src="https://github.com/user-attachments/assets/5cd3e93a-dc4f-4cce-84f1-6323ef1e17f9" />


