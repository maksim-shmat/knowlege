sudo vim /etc/hosts
127.0.0.1    localhost
127.0.0.1    mysite.com


download ngrok 

python3.8 -m pip install sorl-thumbnail
templates/images/image/list_ajax.html
list.html
account/templates/base.html


sudo apt install redis-server
sudo systemctl status redis-server
sudo systemctl status redis-server
automatic start
redis-cli
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> SET name "Peter"
OK
127.0.0.1:6379> GET name 
"Peter"
127.0.0.1:6379> EXISTS name
(integer) 1
127.0.0.1:6379> EXPIRE name 2  # life this key 2 seconds
127.0.0.1:6379> GET name
(nil)
127.0.0.1:6379> SET total 1
OK
127.0.0.1:6379> DES total
(integer) 1
127.0.0.1:6379> GET total
(nil)

python3.8 -m pip install redis
