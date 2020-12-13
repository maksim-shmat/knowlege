import requests
response = requests.get("http://www.metoffice.gov.uk/pub/data/weather\
        /uk/climate/stationdata/heathrowdata.txt")

data = response.text
data_rows = []
rainfall =[]
for row in data.split("\r\n")[7:]:
    fields = [x for x in row.split(" ") if x]
    data_rows.append(fields)
    rainfall.append(float(fields[5]))

print("Average rainfall = {} mm".format(sum(rainfall)/len(rainfall)))
