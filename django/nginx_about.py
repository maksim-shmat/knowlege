"""NGINX abot."""

curl localhost # nginx werlcome default HTML site

nginx -v    # version

ps -ef | grep nginx   # running processes

nginx -h    # help

nginx -s reload    # reload without stopping the server

###### connection draining

curl -X POST -d '{"drain":true}'\
        'http://nginx.local/api/3/http/upstreams/backend/servers/0'

######
