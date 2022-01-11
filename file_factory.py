import os
from treatment import df_positiva, df_neutra, df_negativa, df_final
from pandas_profiling import ProfileReport as pr


def files_builder():


    print('____________________ Building Reports and CSVs')    
    path = os.getcwd()

    #Report Positivas
    profile_positivo = pr(df_positiva, title='Report Geral Reviews Alexa - Avaliações Positivas',
                        html={'style': {'full_width': True}})
    profile_positivo.to_notebook_iframe()
    # profile_positivo.to_file(output_file=f"{path}/Report_Positivas.html")
    profile_positivo.to_file(output_file=f"{path}/Report_Positivas.html")

    # Report Neutras
    profile_neutra = pr(df_neutra, title='Report Geral Reviews Alexa - Avaliações Neutras',
                        html={'style': {'full_width': True}})
    profile_neutra.to_notebook_iframe()
    # profile_neutra.to_file(output_file=f"{path}/Report_Neutras.html")
    profile_neutra.to_file(output_file=f"{path}/Report_Neutras.html")

    # Report Negativas
    profile_negativa = pr(df_negativa, title='Report Geral Reviews Alexa - Avaliações Negativas',
                        html={'style': {'full_width': True}})
    profile_negativa.to_notebook_iframe()
    # profile_negativa.to_file(output_file=f"{path}/Report_Negativas.html")
    profile_negativa.to_file(output_file=f"{path}/Report_Negativas.html")

    # Salvando localmente as tabelas que serão inseridas no banco
    df_positiva.to_csv(f"{path}/df_positiva.csv", sep="|", index=False)
    df_neutra.to_csv(f"{path}/df_neutra.csv", sep="|", index=False)
    df_negativa.to_csv(f"{path}/df_negativa.csv", sep="|", index=False)
    df_final.to_csv(f"{path}/df_final.csv", sep="|", index=False)

    # Backup de tabelas já consumidas, para histórico
    df_positiva.to_csv(f"{path}/df_positiva_bkp.csv", sep=";", index=False)
    df_neutra.to_csv(f"{path}/df_neutra_bkp.csv", sep=";", index=False)
    df_negativa.to_csv(f"{path}/df_negativa_bkp.csv", sep=";", index=False)


files_builder()
