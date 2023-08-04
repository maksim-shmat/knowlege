"""HTTP requests about."""

#1 GET

import requests


urls = {
        'get': 'https://httpbin.org/get?title=learn+python+programming',
        'headers': 'https://httpbin.org/headers',
        'ip': 'https://httpbin.org/ip',
        'now': 'https://now.httpbin.org/',
        'user-agent': 'https://httpbin.org/user-agent',
        'UUID': 'https://httpbin.org/uuid',
}

def get_content(title, url):
    resp = requests.get(url)
    print(f'Response for {title}')
    print(resp.json())

for title, url in urls.items():
    get_content(title, url)
    pritn('-' * 40)

RESULTS:
Response for GET
{
        "args": {
            "title": "learn python programming"
        },
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "close",
            "Host": "httpbin.org",
            "User-Agent": "python-requests/2.19.0"
        },
        "origin": "82.47.175.158",
        "url": "https://httpbin.org/get?title=learn+python+programming"
}
... rest of the output omitted ...

#2 POST

import requests

url = 'https://httpbin.org/post'
data = dict(title='Learn Python Programming')

resp = requests.post(url, data=data)
print('Response for POST')
print(resp.json())

RESULTS:
Response for POST
{'args': {},
 'data': '',
 'files': {},
 'form': {'title': 'Learn Python Programming'},
 'headers': {'Accept': '*/*',
             'Accept-Encoding': 'gzip, deflate',
             'Connection': 'close',
             'Content-Length': '30',
             'Content-Type': 'application/x-www-form-urlencoded',
             'Host': 'httpbin.org',
             'User-Agent': 'python-requests/2.7.0 CPython/3.7.0b2'
                           'Darwin/17.4.0'},
 'json': None,
 'oringin': '82.45.123.178',
 'url': 'https://httpbin.org/post'}
