# spacex-rest-data-pipeline
Python pipeline that ingests data from the SpaceX REST API, transforms it, and stores it in JSON, CSV, and SQLite with idempotent upserts.
=======
# SpaceX Rockets Data Pipeline (REST API → JSON/CSV → SQLite)

A small Python project that fetches rocket data from the public SpaceX REST API, transforms it into a clean schema, saves it to JSON/CSV, and upserts it into a SQLite database.

## Data Source
SpaceX API: `https://api.spacexdata.com/v4/rockets`

## What it does
- Calls the SpaceX rockets endpoint
- Extracts fields: `id`, `name`, `active`, `stages`
- Saves data to:
  - `data/rockets.json`
  - `data/rockets.csv`
- Loads into SQLite:
  - `data/rockets.db`
- Uses `id` as PRIMARY KEY to prevent duplicates (idempotent runs)

## How to run

1) Create and activate venv (optional)
```bash
python -m venv .venv
source .venv/bin/activate
```

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) Run the pipeline
```bash
python main.py
```

## SQLite schema
Table: `rockets`
* `id` TEXT PRIMARY KEY
* `name` TEXT
* `active` INTEGER
* `stages` INTEGER

