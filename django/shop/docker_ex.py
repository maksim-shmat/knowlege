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
sudo pip install docker-compose

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
docker images
docker run -it ubuntu  # run ubuntu image into container(run ->CREATE container with image ubuntu)
root@2ded33ab36c0:/# apt update #-is used in command
exit # go out from container

######
Work with docker farther
docker ps # check active containers
docker ps -a # check all containers
docker ps -l # check last container
docker start 9fb60763329a
docker stop quizzical_mcnulty # use name or ID
docker rm youthful_curie

######
More work with docker
docker commit -m "What" -a "jack" container_id repository(dockershmat)/new_image_name # save current position of all programms into container

repository = dockershmat
docker commit -m "added Node.js" -a "jack" d9b1002f636 dockershmat/ubuntu-nodejs
docker image # check new repo with ubuntu

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

######
Work with containers
docker run --help # inf about indexes
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
docker run --rm sos_ka # Autoremove container after exit
docker run --name string # Assign a name to the container

###### new tutorial
make a mkdir software and file into dir Dockerfile

write into Dockerfile:
    FROM python:3.9
    RUN python -m pip install DateTime
    RUN apt update && apt -y install vim

next 1
docker build -t your-user-name/python-docker-totorial:v1.0.0. .
-t # name and tag your image
. # is a full stop? and path in this place

