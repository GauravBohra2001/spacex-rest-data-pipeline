print(1+2)
import requests

base_url =  "https://api.spacexdata.com"
endpoint =  "/v4/rockets"

url = base_url.rstrip("/") + "/" + endpoint.lstrip("/")
print(url)
response = requests.get(url)
print(response.json())