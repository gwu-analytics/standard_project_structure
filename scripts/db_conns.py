import pandas as pd
from sqlalchemy import create_engine

def query(db, query, params=0):
    if db in ['mdm', 'byod', 'eam', '2012', 'op10water', 'op10wastewater']:

        # Dialect and driver name variables
        dialect= "mssql+pyodbc:///?odbc_connect="
        driver= "DRIVER={ODBC Driver 17 for SQL Server};"

        # Variable for windows authentication
        windows_auth = "Trusted_Connection=yes;"
        
        if db == 'mdm':
            server = "SERVER=192.168.95.56\\UCENTRA;"
            database = "DATABASE=ODMReporting;"
            uid = "UID=odmreport;"
            pwd = "PWD=odmreport;"

            conn = dialect + driver + server + database + uid + pwd

        elif db == 'byod':
            server = "SERVER=cog-umax-sql-bi-int-prod-ugv-01.database.usgovcloudapi.net;"
            database = "DATABASE=cog-umax-sqldb-bi-int-prod-ugv-01;"
            encrypt = "Encrypt=yes;"
            trust_serv_cert = "TrustServerCertificate=no;"
            auth = "authentication=ActiveDirectoryInteractive;"

            conn = dialect + driver + server + database + encrypt + trust_serv_cert + auth
        
        elif db == '2012':
            server = "SERVER=srvvmumxproddb2;"
            database = "DATABASE=UMAX_BI_EXT_PROD;"

            conn = dialect + driver + server + database + windows_auth

        elif db == 'eam':
            server = "SERVER=srvvmeamproddb;"
            database = "DATABASE=EAMDB;"

            conn = dialect + driver + server + database + windows_auth

        elif db == 'op10water':
            server = "SERVER=srvvmop1022;"
            database = "DATABASE=COGWATER;"

            conn = dialect + driver + server + database + windows_auth

        elif db == 'op10wastewater':
            server = "SERVER=srvvmop1022;"
            database = "DATABASE=COGWASTEWATER;"
            
            conn = dialect + driver + server + database + windows_auth

    # Create engine, run query, return to df, dispose of engine
        engine = create_engine(conn)
        if params == 0:
            df = pd.read_sql(query, engine)
        else:
            df = pd.read_sql(query, engine, params=params)
        engine.dispose()

    # Handle invalid db selection    
    else:
        raise ValueError("db is invalid.")

    return df
