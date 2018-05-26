import os
import psycopg2

from etc.types import PsycopgConnection

def get_db_connection(psql_vars: dict)->PsycopgConnection:

    conn = psycopg2.connect( ' '.join(f'{k}={v}' for k,v in psql_vars.items()))
    conn.set_session(autocommit=True)

    return conn
