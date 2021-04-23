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


