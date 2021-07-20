""" Push ask with proxy from lib Requests."""

>>> import requests
>>> p = {'htttp': '200.255.122.174:8080'}  # Free proxy IP
>>> r = requests.get("http://httpbin.org/ip")  # push ask withot proxy
>>> r.json()['origin']  # my IP
>>> r = requests.get("http://httpbin.org/ip",proxies = p) #push ask with proxyIP
>>> r.json()['origin'} # he have change IP, but in my case it freeze from Beralusian kingdom
