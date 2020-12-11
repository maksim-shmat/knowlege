import json
import requests

response = requests.get("https://data.cityofchicago.org/resource/\
        6zsd-86xi.json?$where=date between '2015-01-10T12:00:00' and \
        '2015-01-10T13:00:00'&arrest=true")

crime_data = json.loads(response.text)

with open("crime_series.json") as infile:
    for line in infile:
        crime_data_3 = json.loads(line)
