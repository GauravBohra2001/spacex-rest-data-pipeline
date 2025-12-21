import csv
from scratch.phase3_extract import clean_rockets

col_names = ["name", "active", "stages"]

file_path = "rockets.csv"
with open(file_path, 'w', newline='') as output:
    writer = csv.DictWriter(output, fieldnames=col_names)
    writer.writeheader()
    writer.writerows(clean_rockets)