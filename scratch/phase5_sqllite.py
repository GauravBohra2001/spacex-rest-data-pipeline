import sqlite3
from scratch.phase3_extract import clean_rockets

conn = sqlite3.connect("rockets.db")
cursor = conn.cursor()

#create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS rockets(
               name TEXT (40),
               active INTEGER , 
               stages INTEGER
               );
""")

#creating rows to insert
rows = [(d["name"], int(d["active"]), int(d["stages"])) for d in clean_rockets]

#insert record
insert_record = """INSERT INTO rockets(name, active, stages) VALUES (?, ?, ?);"""

cursor.executemany(insert_record, rows)

conn.commit()

conn.close()