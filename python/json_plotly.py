"""Analize data from .json for plotly."""

import json

from plotly.graph_objs import Scattergeo, Layout  # Scattergeo it's global map
from plotly import offline


filename = '/home/jack/django2/knowlege/python/apple.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['High']  # 'High' I read this tag from apple_readable.json
#mags, lons, lats = [], [], []
#for eq_dict in all_eq_dicts:
#    mag = eq_dict['properties']['mag']  # if the dict make more dicts
#    lon = eq_dict['geometry']['coordinates'][0]
#    lat = eq_dict['geometry']['coordinates'][1]
#    mags.append(mag)
#    lons.append(lon)
#    lats.append(lat)
#
#print(len(all_eq_dicts))
#print(mags[:10])
#print(lons[:5])
#print(lats[:5])

# Put data on the map
#data = [Scattergeo(lon=lons, lat=lats)]  # it's simply, dict better
#or
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],  # bigger marker
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,  # dark-blue for high, light-yellow for low
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
ofline.plot(fig, filename='global_earthquakes.html')

