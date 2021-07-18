"""NGINX abot."""

curl localhost # nginx werlcome default HTML site

nginx -v    # version

ps -ef | grep nginx   # running processes

nginx -h    # help

nginx -s reload    # reload without stopping the server

###### connection draining

curl -X POST -d '{"drain":true}'\
        'http://nginx.local/api/3/http/upstreams/backend/servers/0'

###### using the GeoIP module and databse

apt install nginx-module-geoip

mkdir /etc/nginx/geoip
cd /etc/nginx/geoip
wget "http://geolite.maxmind.com/\
        download/geoip/database/GeoLiteCountry/GeoIP.dat.gz"
gunzip GeoIP.dat.gz
wget "http://geolite.maxmind.com/\
        download/geoip/database/GeoLiteCity.dat.gz"
gunzip GeoLiteCity.dat.gz

######
