import requests

url = "https://api.spacexdata.com/v4/rockets"

response = requests.get(url)

print(f"The response json code is: {response.status_code}")

print(f"The type of parsed json is: {type(response.json())}")

print(f"The json data is: {response.json()}")