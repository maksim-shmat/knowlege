"""gpg apbout."""

#1 Generate keys

gpg --full-generate-key

#2 Whereis gpg keys

/home/jack/.gnupg/openpgp-revocs.d

#3 Check fingerprint

gpg --fingerprint m.sh@gmail  # or "Antuan Pestrunoff"

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

gpg --delete-key "Andrus Petuhoff"  # or fingerprint, or email
gpg --delete-secret-key "Andrus Petuhoff"

#7 Encryption

gpg -e -a -r "Petr Bzdunoff" petrushka.py  ## -a (ASCII, .asc) for mailing key

# Encrypt message for copy from terminal, for mailing

echo 'Hello, World' | gpg -e -a -r 'Anri Kars'

# Scenarios1: not simple
#--------------
#- encrypt message and output into terminal
#- copy into buffer
#- move primary buffer to file.gpg with xsel
#- ...
#- decrypt it with gpg

<1> gpg -e -a -r "Hello, World!" | gpg -e -a -r "Unt Serensen"  # -e encrypt
                                                            # -a ASCII
                                                            # -r Recipient
<2> ...
<3> xsel -p > message_Unt.py.gpg  # -p primary buffer
<4> send it file, for example
<5> gpg --decrypt -o decrypted_Unt.py message_Unt.py.gpg  
                # -o output into newfile

# Scenarious2:  better and simple
#1 encrypt and output into file
echo "Hello, John!" | gpg -e -a -r "John Mclain" > message_for_john.py.gpg

#2 decrypt into file

gpg -d -o decrypted_John.py message_for_john.py.gpg  # output into file
# gpg -d encrypted.py.gpg > decrypted.py
gpg -d message_for_john.py.gpg  # output into terminal

#8 Check for how message without keys (ID, time, name, comment, email, type key)

gpg -- list-only -d encrypted_mess.py.gpg

#9 Signs
# not readable before decryption
gpg --local-user 'Jeffrey Stokman' -s test.py  # -u = --local-user
gpg -d test.py.gpg

# readable, decript for view sign
gpg -u 'Joui Smargl'--clear-sign test.py
gpg -d test.py.asc

# Sign in different file .sig with link to original file, send both files.
gpg -u 'Farhad Simbaef' -b test.py  # -b = --detach-sign

#9
