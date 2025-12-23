file_path = 'rockets.json'
import json
from scratch.phase3_extract import clean_rockets

with open(file_path, 'w') as output:
    json.dump(clean_rockets, output, indent=4)