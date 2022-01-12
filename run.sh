#!/bin/bash

echo "Building Venv"
sleep 2
python3 -m venv scrap-env
source scrap-env/bin/activate
clear

echo "Runing Requirements and Installing Packages"
sleep 2
pip install -r requirements.txt
clear

echo "Runing Work Pipeline"
sleep 2
python3 main.py
clear

echo "Finish"

