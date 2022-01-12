from google.oauth2 import service_account
import pandas_gbq
import os
import time


def drop_tables():


    print('____________________ Conecting to Big Query')

    path = os.getcwd()

    credentials = service_account.Credentials.from_service_account_file(
        f'{path}/dbcredential.json',
    )


    try:
        sql = """
        DROP TABLE scrap-sauter.Tables.positivas ;

        DROP TABLE scrap-sauter.Tables.neutras ;

        DROP TABLE scrap-sauter.Tables.negativas ;

        DROP TABLE scrap-sauter.Tables.completa
        
        """

        df = pandas_gbq.read_gbq(sql, project_id="scrap-sauter", credentials=credentials)

    except:
        print('_____________ Requiring Insert Module')
        time.sleep(3)


drop_tables()
