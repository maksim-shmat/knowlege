"""Simple instruction about Django."""

#1 Create a simple Django server.

#2 Host your server on the Digital Ocean for example

#2a Create connection to your DigOcean droplet through ssh

#3 Install python dependencies

pip install django gunicorn

#4 Create Django project

django-admin startproject lifecycle .

#5 Start

python manage.py runserver  # but django server not safe

#6 Need Gunicorn and WSGI

#7 Create a simple script named hello_world.py

def process_http_request(environ, start_response):
    status = '200 OK'
    response_headers = [
            ('Content-type', 'text/plain; charset=utf-8'),
    ]
    start_response(status, response_headers)
    text = 'Hello World'.encode('utf-8')
    return [text]

#8 Start Gunicorn

$ gunicorn hello_world:process_http_request --bind 0.0.0.0:8000

#8a Open the pabe and we should see "Hello World" text

#9 Run Gunicorn wsgi server for our Django application

$ gunicorn lifecycle.wsgi:application --bind 0.0.0.0:8000

#10 Need Nginx

sudo apt install nginx

#10a Need configure firewall, allow incoming traffic on port 80
# and port 443 for HTTPS

$ sudo ufw allow 'Nginx HTTP'  # 80 port

#10b Create a configuration file

# vim /etc/nginx/sites-available/lifecycle

upstream_django {
        server 0.0.0.0:8000;
}

server {
        listen 80;

        location / {
            proxy_pass http://sever_django;
            proxy_set_header X-Forward-For
$proxy_add_x_forwarded_for;
            proxy_set_header Host $host;
            proxy_redirect off;
        }

        location /statuc/ {
            alias /app/static/;
        }
}

#10c Remove default configuration file from Nginx and add our conf to /sites-enabled/

$ rm -rf /etc/nginx/sites-available/default
$ rm -rf /etc/nginx/sites-enabled/default
$ sudo ln -s /etc/nginx/sites-available/lifecycle/ 
/etc/nginx/sites-enabled/

#10d Restart Nginx

sudo systemctl restart nginx


