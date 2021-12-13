"""gpg apbout."""

#1 Generate keys

gpg --full-generate-key

#2 Whereis gpg keys

/home/jack/.gnupg/openpgp-revocs.d

#3 Check fingerprint

gpg --fingerprint m.sh@gmail

#4 Write key into file

gpg --output ~/jill.key --armor --export m.sh@gmail
gpg --export-secret-key -a "Alesha Popovj" > private.key
gpg --export-secret-key -a -o private.key "Alesha Popovj"

###
gpg --import public.key
gpg --import private.key

#5 List of keys

gpg --list-keys
gpg --list-secret-keys

#6 Remove keys

gpg --delete-key "Andrus Petuhoff"
gpg --delete-secret-key "Andrus Petuhoff"

#7 
