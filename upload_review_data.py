#!/bin/bash python

import os
import psycopg2
import json
import typing
import logging

from typing import Generator, List
from psycopg2.extras import execute_values

from etc.get_db_connection import get_db_connection
from etc.logging import initialize_logging
from etc.types import PsycopgCursor

def lazyload_json_file(fpath: str=None)->Generator[str, dict, str]:
    """
    Accept fpath to json file. Return a lazy generator that yields one json element at a time.

    """
    f = open(fpath)
    for jsonline in f:
        yield json.loads(jsonline)

    return 'JSON file exhausted.'

def insert_json_into_psql(table: str, columns: List[str], json_elements: List[dict],
                          cursor: PsycopgCursor)->None:
    """
    Accept list of json elements. Save to external psql db.

    """
    sorted_cols = sorted(columns)
    insert_query = f'INSERT INTO {table} ({",".join(sorted_cols)}) VALUES %s'

    values = []
    for el in json_elements:
        values.append(tuple(el[k] if (k in el) else None for k in sorted_cols))

    execute_values(cursor, insert_query, values)


if __name__ == '__main__':
    initialize_logging()

    # setup vars
    json_fpath = '/Users/robertdalton/web-projects/subjective-objective/data/reviews_Office_Products_5.json'
    columns = ['reviewerID', 'asin', 'reviewerName',
               'helpful', 'reviewText', 'overall',
               'summary', 'unixReviewTime', 'reviewTime']

    # setup psql cursor
    conn = get_db_connection()
    cur = conn.cursor()

    # save elements in batches of batch_size
    batch_size = 100
    batch_num = 0
    i, elements = 0, []
    for el in lazyload_json_file(json_fpath):
        if i < batch_size:
            elements.append(el)
            i += 1
        else:
            insert_json_into_psql('reviews', columns, elements, cur)
            batch_num += 1
            logging.info(f'Batch {batch_num} successfully saved to DB.')
            i, elements = 0, []

    # save last chunk if remainders
    if len(elements) > 0:
        insert_json_into_psql('reviews', columns, elements, cur)

    logging.info(f'{batch_num * batch_size + len(elements)} elements succesfully saved to DB.')
