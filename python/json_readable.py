"""Make json data more readable."""

import json


filename = '/home/jack/django2/knowlege/python/apple.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = '/home/jack/django2/knowlege/python/apple_readable.json'
with open(readable_file, 'w') as f:
    
    json.dump(all_eq_data, f, indent=4)
