"""Work with API."""

import requests


# Make a call API and save answer.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")  # 200 is a good answer

# Save answer from API into variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Analize of information about repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Analize a first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

# Handling of results
print(response_dict.keys())

print("\nSelectec information about first repository:")
#for repo_dict in repo_dicts:
#    print(f"Name: {repo_dict['name']}")
#    print(f"Owner: {repo_dict['owner']['login']}")
#    print(f"Stars: {repo_dict['stargazers_count']}")
#    print(f"Repository: {repo_dict['html_url']}")
#    print(f"Created: {repo_dict['created_at']}")
#    print(f"Updated: {repo_dict['updated_at']}")
#    print(f"Description: {repo_dict['description']}")

# Results:
#Repository: https://github.com/shadowsocks/shadowsocks
#Created: 2012-04-20T13:10:49Z
#Updated: 2022-05-19T01:03:22Z
#Description: None
#Name: DeepFaceLab
#Owner: iperov
#Stars: 32616
#Repository: https://github.com/iperov/DeepFaceLab
#Created: 2018-06-04T13:10:00Z
#Updated: 2022-05-19T00:59:40Z
#Description: DeepFaceLab is the leading software for creating deepfakes.
