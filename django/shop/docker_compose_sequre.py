"""About save confidence in docker-compose."""

# with PGP ecryption
$ gpg --generate-key
pub rsa2048...
uid  pydevops <my.email@gmail.com>
sub rsa2048 2019-07-12 [E] [expires: 2021-07-11]

# next
download "sops" from his site
create file environment.secrets
$ sops --pgp BBDE.... environment.secrets

# next
add note in file
export DBPASS=MYPASS

# next
inspect how encrypted
cat environment.secrets

# next
to decrypt
$ sops -d environment.secrets
export DBPASS=MYPASS

# next
run migration service for example
$ source <(sops -d environment.secrets); docker-compose up -d migrations

# next
verify that the migrations
$ docker-compose exec db psql -U postgres wordcount

######
Note that if your secret key includes a dollar sign, $, then you need to add an additional
dollar sign, $$. This is due to how docker-compose handles variable substitution a .
Otherwise you will see an error!

######
