#!/bin/bash

echo "criando venv"
sleep 2
python3 -m venv scrap-env
source scrap-env/bin/activate
clear

echo "baixando requirements"
sleep 2
pip install -r requirements.txt
clear

echo "rodando projeto"
sleep 2
python3 main.py
clear

echo "tudo pronto"

