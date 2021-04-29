https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru

sudo atp update

sudo apt install apt-transport-https ca-certificates curl software-properties-common # apt use https

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# result - OK
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
# result - done
sudo apt update
# check that download from docker without ubuntu repo
Hit:5 https://download.docker.com/linux/ubuntu focal InRelease

apt-cache policy docker-ce
# check candidates for install
sudo apt install docker-ce
# 410mb
sudo systemctl status docker
sudo usermod -aG docker ${USER}
su - ${USER}
Password:
jack@Cesar:~$ id -nG
jack adm cdrom sudo dip plugdev lpadmin sambashare docker
# docker group check
docker  -list of commands
docker docker-subcommands --help
docker info

docker run hello-world

docker run -it ubuntu bash
Status: Downloaded newer image for ubuntu:latest
root@6d2f4cf5c77b:/#
# nowb, you rootman in container, cool. Remember 6d2f4cf5c77b, that's name of your container and del it later.
docker run -it ubuntu
root@0c3e307ae07e:/#
# What new container? oh scheet.
root@0c3e307ae07e:/# apt update
root@0c3e307ae07e:/# apt install nodejs
root@0c3e307ae07e:/# node -v
root@0c3e307ae07e:/# exit

docker ps -a  - view all containers
docker ps -l  - last one container
docker start <nuber of container>
# docker add funny name for you container
docker stop blissful_keller
docker rm blissful_keller

jack@Cesar:~$ docker commit -m "added hihuia" -a "Shmat" frosty_varahamihira dockershmat/hui
# commit , author, container_id, repository in DockerHub, new_image_name.

docker images  # sees your docker images

docker login -u dockershmat
password:
    WARNING! Your password will be stored unencrypted in /home/jack/.docker/config.json.

if your local docker username diff with docker name from Docker Hub  - tag it:
    $ docker tag pupkin/ubuntu-nodejs dockershmat/ubuntu-nodejs

docker push dockershmat/hui  (your docker image name)
# push it

Install Compose 
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

Even if you want to run a single Docker container, it is still a good idea to include it in a docker-compose.yaml file and launch it with the docker-compose up -d command. It will make your life easier when you want to add a second container into the mix, and it will also serve as a mini Infrastructure as Code example, with the docker-compose.yaml file reflecting the state of your local Docker setup for your application.

######
porting the docker-compose services to a new host and os

sudo apt-get update
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get installl \
        apt transport-https \
        ca-sertificates \
        curl \
        gnupg-agent \
        software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
        "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable"

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo usermod -a -G docker ubuntu

# download docker-compose
$ sudo curl -L \
        "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-\

$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose

###
copy docker-compose.yaml to the remote EC2 instance and start the db service

docker-compose up -d db
docker-compose exec db psql -U postgres
docker exec -it 49fe88efdb46 psql -U postgres wordcount

###
docker login
export DOCKER_PASS=MYPASS

docker-compose up -d

