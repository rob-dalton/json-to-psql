import os
import psycopg2

from etc.types import PsycopgConnection

def get_db_connection()->PsycopgConnection:

    # setup psql connection
    psql_vars = {
        'host': os.environ['PSQL_HOST'],
        'dbname': os.environ['PSQL_DBNAME'],
        'user': os.environ['PSQL_USER'],
        'password': os.environ['PSQL_PASS']
    }

    conn = psycopg2.connect( ' '.join(f'{k}={v}' for k,v in psql_vars.items()))
    conn.set_session(autocommit=True)

    return conn
