# JSON to PSQL Converter
Script to save a json file to a PSQL table using `psycopg2` and Python 3.

## Usage
Run as command `python json_to_psql.py <ARGS>` with args:
  - `-f`, `--fpath`: path to json file to save to PSQL (required)
  - `-n`, `--name`: name of table to save JSON to (required)
  - `-s`, `--schema`: path to JSON file of table schema (required)
  - `-c`, `--connection`: path to JSON file of PSQL connection params (optional)

## Requirements
The script requires 2 JSON files to run. You are required to pass the first one as an argument, and may optionally pass the second one:
  - A JSON file of column names and dtypes corresponding to the data in your JSON file
  - A JSON file of PSQL connection parameters for the DB you will be saving to. Will use the file `psql_default_params.json` by default, if it exists.

Example schema file:
```
{
    "id": "serial PRIMARY KEY",
    "user": "text",
    "review_text": "text",
    "date": "date"
}
```

Example connection parameters file:
```
{
    "host": "localhost",
    "dbname": "reviews",
    "user": "postgres",
    "password": "abc123",
}
```
