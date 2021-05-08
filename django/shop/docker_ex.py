"""Docker about."""

### Uninstall old versions
sudo apt-get remove docker docker-engine docker.io containerd runc # 2

# Uninstall Docker Engine
sudo apt-get purge docker-ce docker-ce-cli containerd.io # 1
sudo rm -rf /var/lib/docker # 3
sudo rm -rf /var/lib/container # 4

# next 
docker --version 

# next 
sudo pip3 install docker-compose

# next
docker run -it ubuntu bash

# next
docker info

# new instructions # 1
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# next
Add GPG key or official repo Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# next
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

# next
sudo apt update

# next 
apt-cache policy docker-ce

# next
sudo apt install docker-ce

# next
sudo systemctl status docker

# All it that's with Docker

######
Add <docker> command without sudo

sudo usermod -aG docker ${USER}
su - ${USER}
id -nG  # check user in docker

# add user in docker group withot root
sudo usermod -aG docker username

######
Work with docker
docker # list commands
docker docker-subcommand --help
docker info
docker run hello-world
docker search ubuntu
docker login
docker pull ubuntu
docker run -it ubuntu  # run ubuntu image into container(run ->CREATE container with image ubuntu)
root@2ded33ab36c0:/# apt update #-is used in command
exit # go out from container

######
More work with docker
docker commit -m "What" -a "jack" container_id repository(dockershmat)/new_image_name # save current position of all programms into container

repository = dockershmat
docker commit -m "added Node.js" -a "jack" d9b1002f636 dockershmat/ubuntu-nodejs

docker login -u dockershmat
docker tag jack/ubuntu dockershmat/ubuntu # because jack not dockershmat
docker push dockershmat/docker-image-name # upload
docker push jack/ubuntu # upload into jack repo

######
Remove and clear
docker ps -a # all containers
docker images # all images
docker rm container_id(or name)
docker rmi name_image

###### new tutorial
Add Dockerfile
Add FROM python
    RUN python -m pip install DateTime
    RUN apt update && apt -y install vim


docker build -t jack/python-docker-tutorial:v1.0.0 .
docker run --name my_service jack/python-docker-tutorial:v1.0.0
docker start my_service
create hello.py
change Dockerfile
    COPY ./test/test.py /home
    CMD ["python", "/home/test.py"]
docker build -t jack/python-test:v2.0.0 .
docker create --name hello-test jack/python-test:v2.0.0
docker start hello -a
######
Add docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version # test

add docker-compose.yml to beside place where Dockerfile
for docker-compose.yml two spaces in different it is important

docker-compose build
docker-compose up -d  # -d run on the background
docker-compose ps
docker ps
###### new tutorial 02
make file app.py                       # 1. make a file
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! (from a Docker container)'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

cat requirements.txt                   # 2. make requirements
Flask==1.0.2

cat Dockerfile                         # 3. make Dockerfile
FROM python:3.7.3-alpine # set with pip
ENV APP_HOME/app
WORKDIR $APP_HOME
COPY requirements.tst .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ] # or default /bin/sh -c
CMD [ "app.py" ]

docker build -t hello-world-docker .    # 4. make image
docker run --rm -d -v 'pwd':/app -p 5000/:5000 hello-world-docker
# --rm (rm after stop), -d (in background), -v(in dir 'pwd'), -p (ports: firstport(5000) to the second port(5000) inside the container

docker logs <container ID>

curl http://127.0.0.1:5000
Hello,World! (from a Docker container)

docker stop <container ID>

###### Short instruction
mkdir myproject && cd myproject
echo "hello" > hello
echo -e "FROM busybox\nCOPY /hello/\nRUN cat /hello" > Dockerfile
docker build -t helloapp:v1

######
How rm images <none>?
$docker image prune
######
