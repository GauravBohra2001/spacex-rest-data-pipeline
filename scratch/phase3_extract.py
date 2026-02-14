import requests

url = "https://api.spacexdata.com/v4/rockets"

response = requests.get(url)


clean_rockets = []

if response.status_code == 200:
    print("Response code is:", response.status_code)
    for data in response.json():
        items = {
            "name" : data.get("name"),
            "active" : data.get("active"),
            "stages" : data.get("stages")
        }
        clean_rockets.append(items)
else:
    print("Connection is not made properly")

for i in clean_rockets:
    print(f"name = {i['name']} | active = {i['active']} | stages = {i['stages']}")