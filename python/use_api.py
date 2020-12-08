import requests
response = requests.get("http://data.cityofchicago.org/resource/\
        6zsd-86xi.json?$where=date between '2015-01-10T12:00:00' and\
         '2015-01-10T13:00:00'&arrest=true")
print(response.text)
