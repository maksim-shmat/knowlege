"""Visual python repositories with Plotly, continue work from find_py_repos_on_git.py."""

import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and save ansver.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Handling of results.
response_dict = r.json()
repo_dicts = response_dict['items']
#repo_names, stars, labels = [], [], []
# or
repo_links, stars = [], []
for repo_dict in repo_dicts:
    #repo_names.append(repo_dict['name'])
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}''>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

#    owner = repo_dict['owner']['login']
#    discription = repo_dict['description']
#    label = f"{owner}<br />{description}"
#    labels.append(label)

# Build a visualization.
data = [{
    'type': 'bar',
   # 'x' : repo_names,
    'x' : repo_links,
    'y' : stars,
#    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
