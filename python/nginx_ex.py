"""Nginx about."""

# check
sudo systemctl status nginx

# stop
sudo systemctl stop nginx

###### How to use nginx

1. Update your system
sudo apt update

2. Install Nginx
sudo apt install nginx

3. Create new folder in /var/www
cd /var/www
sudo mkdir linuxseb
cd linuxseb

4. Create index.html file

sudo vim index.html

<!doctype html>
<html>
  <head>
    <title> Linux with Seb </title>
  </head>
  <body>
    <h1> hello welcome to my tutorial </h1>
    <p> to be honest i was bored and was like ok lemme make a tutorial </p>
</html>

5. Create the virtual host

cd /etc/nginx/sites-enabled
sudo vim linuxspompom

server {
listen 81;
listen [::]:81;

server_name linuxwithseb.com;

root /var/www/linuxseb;
index index.html;

location / {
try_files $uri $uri/ =404;

}
}

6. Restart Nginx

sudo service nginx restart

7. Test it

Go to your browser and type localhost:81

######2
