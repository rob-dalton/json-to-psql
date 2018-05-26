# JSON to PSQL Converter
Script to save a json file to a PSQL table.

## Setup
The script requires 2 JSON files to run:
  - A JSON file of column names and dtypes corresponding to the data in your JSON file
  - A JSON file of PSQL connection parameters for the DB you will be saving to. Will use the file 'psql_default_params.json' by default, if it exists.

## Usage
Run as command `python json_to_psql.py <ARGS>' with args:
  - '-f', '--fpath': path to json file to save to PSQL (required)
  - '-n', '--name': name of table to save JSON to (required)
  - '-s-, '--schema': path to JSON file of table schema (required)
  - '-c', '--connection': path to JSON file of PSQL connection params (optional)
