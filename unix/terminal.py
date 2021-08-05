""" About linux terminal."""

Open file in browser - $xdg-open index.html  # man xdg-open

passwd  # change password

rmdir   # remove directory

echo    # sends data

cp      # copy a file (cp [source] [destination]

mv      # move a file (mv [source] [destination]

locate  # locate a file on the machine (locate [filename]

updatedb # update the directory database

man     # manualy page of any command

grep    # search for the following words (can be used to check if a file
        # contains specific info)

# =====================
./      # your directory right now

../     # previous folder

~       # the users root folder

|       # pipe the output of one command into another

>       # use command on the following file (overwrite)

>>      # use command on following file (appends)

# =====================

cat     # reads a file to the terminal

chmod   # change permission for a file

adduser # make a new user

su      # switch user

# ====================

ifconfig # print network information

iwconfig # wireless network information

ping    # ping an ip address (-c flag lets you define how many times you wish
        # to ping the given ip address)

arp -a  # send out an arp request to check for machines on the network

netstat -a # shows all open ports and what is connected to these ports

route   # shows a routing table

# =====================

history # lists the 15 commands you entered (history | grep [command] shows
        # all the times you run a command on the machine (including spec syntax))
apt purge # program name - (You have to use the **)

# ==================== webserver commands

service apache2 start  # start a webserver

service ssh start  # start a ssh server

service postgresql start  # a service that starts with metasploit

sevice apache2 stop

systemctl enable [program name]  # start the service when the machine turns on

# =============== important file/directories

/etc/password  # a file stores all of the users in the system

/etc/shadow    # stores all of the passwords in the system

/var/log/auth.log  # authentication reports

# =================
