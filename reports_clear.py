"""
Optional module.
"""

import os
import time


def clear_reports():
    print('____________________ Cleaning Reports From Root')
    path = os.getcwd()
    diretorios = os.listdir(path)
    print()
    time.sleep(3)
    try:
        for arquivo in diretorios:
            if arquivo == "Report_Negativas.html" or arquivo == "Report_Neutras.html" or arquivo == "Report_Positivas.html":
                os.remove(arquivo)
                print(f'Arquivo = {arquivo} apagado')
    except:
        print('Cleaning stopped. Make sure the address of the files in the directory to be cleaned. ')

    print('____________________ Clear Done \n')
    

clear_reports()