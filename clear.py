import os
import time


def limpar_raiz():
    print('____________________ Cleaning Files From Root')
    path = os.getcwd()
    diretorios = os.listdir(path)
    print()
    time.sleep(3)
    try:
        for arquivo in diretorios:
            if arquivo == "df_neutra.csv" or arquivo == "df_positiva.csv" or arquivo == "df_negativa.csv" or arquivo == "df_final.csv":
                os.remove(arquivo)
                print(f'Arquivo = {arquivo} apagado')
    except:
        print('Cleaning stopped. Make sure the address of the files in the directory to be cleaned. ')

    print('____________________ Clear Done \n')
    print(
        '##################  Programa executado com êxito ###################\n# Ações Executadas:                                                #\n# 1- App Scraping de Reviews do app Alexa na Google Play Store     #\n# 2- Limpeza e Filtragem de Dados                                  #\n# 3- Geração de 3 arquivos csv filtradas pela avaliação            #\n#    dos usuários                                                  #\n# 4- Geração de Reports de análise dos dados coletados             #\n# 5- Gravação de informações no banco de dados                     #\n# 6- Limpeza do diretório de origem dos arquivos CSV               #\n#                                                                  #\n####################################################################\n')


limpar_raiz()