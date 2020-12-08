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

