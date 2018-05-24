import os
import psycopg2
import json
import typing

from typing import Generator
from psycopg2.extras import execute_values

from etc.get_psql_cursor import get_psql_cursor
from etc.types import PsycopgCursor

def lazyload_json_file(fpath: str=None)->Generator[dict]:
    """
    Accept fpath to json file. Return a lazy generator that yields one json element at a time.

    """
    f = open(fpath)
    for jsonline in f:
        yield json.loads(jsonline)

def insert_json_into_psql(table: str,
                          columns: list[str],
                          json_elements: list[dict],
                          cursor: PsycopgCursor)->None:
    """
    Accept list of json elements. Save to external psql db.

    """
    sorted_cols = sorted(columns)
    insert_query = f'INSERT INTO {table} ({",".join(sorted_cols)}) VALUES %s'

    values = []
    for el in json_elements:
        values.append(tuple(el.values()))

    execute_values(cursor, insert_query, values)


if __name__ == '__main__':

    # setup vars
    json_fpath = '/Users/robertdalton/web-projects/subjective-objective/data/reviews_Office_Products_5.json'
    columns = ['reviewerID', 'asin', 'reviewerName',
               'helpful', 'reviewText', 'overall',
               'summary', 'unixReviewTime', 'reviewTime']

    # setup psql cursor
    cur = get_psql_cursor('reviews')

    # save elements
    for el in lazyload_json_file(json_fpath):
        pass

