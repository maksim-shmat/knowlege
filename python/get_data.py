import json
import csv
import requests

for sol in range(1830,1863):
    response = requests.get("http://marsweather.ingenology.com/v1/\
            archive/?sol={}&format=json".format(sol))
    result = json.loads(response.text)
    if not result['count']:
        continue
    weather = result['results'][0]
    print(weather)
    csv.DictWriter(open("mars_weather.csv", 'a'), \
            list(weather.keys())).writerow(weather)
