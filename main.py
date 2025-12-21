import json
import requests
import csv
import sqlite3


def load_config():
    with open("config.json") as f:
        return json.load(f)

def fetch_rockets(base_url, endpoint, timeout_seconds):
    url = base_url.rstrip("/") + "/" + endpoint.lstrip("/")
    response = requests.get(url, timeout=timeout_seconds)
    
    response.raise_for_status()
    return response.json()

def transform_rockets(response):
    clean_data = []
    for data in response:
        items = {
            "id" : data.get("id"),
            "name": data.get("name"),
            "active": int(data.get("active",False)),
            "stages" : int(data.get("stages", 0))
        }
        clean_data.append(items)
    return clean_data

def save_json(data, path):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def save_csv(data, path):
    col_names = ["id", "name", "active", "stages"]
    with open(path, "w", newline='') as output:
        writer = csv.DictWriter(output, fieldnames=col_names)
        writer.writeheader()
        writer.writerows(data) 

def init_db(db_path):

    try: 
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS rockets( 
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    active INTEGER,
                    stages INTEGER); 
                    """)
        conn.commit()
    finally:
        conn.close()

def upsert_rockets(db_path, rockets):
    try: 
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        rows = ((d["id"], d["name"], int(d["active"]), int(d["stages"])) for d in rockets)
        insert_record = """INSERT OR REPLACE INTO rockets(id, name, active, stages) VALUES (?, ?, ?, ?);"""
        cursor.executemany(insert_record, rows)
        conn.commit()
    finally:
        conn.close()

def print_summary(db_path):
        conn = sqlite3.connect(db_path)
        try: 
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rockets;")
            data = cursor.fetchall()
            for d in data:
                print("Rows in the db: ", d)
        finally:
            conn.close()

def main():
    config = load_config()
    raw = fetch_rockets(
        config["api"]["base_url"]   , 
        config["api"]["endpoint"],
        config["api"]["timeout_seconds"],
)
    clean = transform_rockets(raw)
    print("clean count:", len(clean))
    print("clean sample:", clean[0])

    save_json(clean, "data/rockets.json")
    save_csv(clean, "data/rockets.csv")
    init_db("data/rockets.db")
    upsert_rockets("data/rockets.db", clean)
    print_summary("data/rockets.db")

if __name__ == "__main__":
    main()