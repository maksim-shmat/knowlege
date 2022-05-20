"""Get info from hacker-news for next step analyze and visualisation."""

import requests
import json


# API call and save answer.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Handling of information about every topic.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make special API call for every topic.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Make a dict for every topic.
    submission_dict = {
            'title': response_dict['title'],
            'hh_link': f"http://news.ycombinator.com/item?=id={submission_id}",
    #        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

#submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hh_link']}")
#    print(f"Comments: {submission_dict['comments']}")
    
# Analize structure of data
response_dict = r.json()
readable_file = '/home/jack/django2/knowlege/python/jill.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
