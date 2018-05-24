#!/bin/bash python
import os

from etc.get_db_connection import get_db_connection

if __name__ == '__main__':

    conn = get_db_connection()
    cur = conn.cursor()

    # setup table column dtypes
    columns = {'id': 'serial PRIMARY KEY',
               'asin': 'text',
               'helpful': 'int[]',
               'overall': 'numeric',
               'reviewText': 'text',
               'reviewTime': 'text',
               'reviewerID': 'text',
               'reviewerName': 'text',
               'summary': 'text',
               'unixReviewTime': 'int'}

    # create table
    query = f'CREATE TABLE IF NOT EXISTS reviews ({",".join(f"{k} {v}" for k,v in columns.items())});'
    cur.execute(query)
