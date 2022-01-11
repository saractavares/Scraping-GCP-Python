import pandas as pd
import time
import os


def insert_data():

    
    print('____________________ Inserting Data on Database')

    path = os.getcwd()
    positiva = pd.read_csv(f'{path}/df_positiva.csv', sep='|')
    positiva.to_gbq(destination_table='Tables.positivas',
                    project_id='scrap-sauter',
                    if_exists='replace')

    neutra = pd.read_csv(f'{path}/df_neutra.csv', sep='|')
    neutra.to_gbq(destination_table='Tables.neutras',
                  project_id='scrap-sauter',
                  if_exists='replace')

    negativa = pd.read_csv(f'{path}/df_negativa.csv', sep='|')
    negativa.to_gbq(destination_table='Tables.negativas',
                    project_id='scrap-sauter',
                    if_exists='replace')

    completa = pd.read_csv(f'{path}/df_final.csv', sep='|')
    completa.to_gbq(destination_table='Tables.completa',
                    project_id='scrap-sauter',
                    if_exists='replace')


insert_data()
time.sleep(5)
