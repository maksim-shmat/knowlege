""" About linux terminal."""

#1 Open new window

Shift+Ctrl + T  # open new tab
Shift+Ctrl + W  # close tab

Shift+Ctrl + N  # open window
Shift+Ctrl + Q  # close window



Open file in browser - $xdg-open index.html  # man xdg-open

passwd  # change password

rmdir   # remove directory

echo    # sends data

mv      # move a file (mv [source] [destination]

locate  # locate a file on the machine (locate [filename]

updatedb # update the directory database

grep    # search for the following words (can be used to check if a file
        # contains specific info)
$ grep -n about *  # show all files where is word 'about', -n - numbers or str

# =====================
    >       # overwrite

    >>      # appends, echo hui >> jill.py

# ====================

ifconfig # print network information

iwconfig # wireless network information

ping    # ping an ip address (-c flag lets you define how many times you wish
        # to ping the given ip address)

arp -a  # send out an arp request to check for machines on the network

netstat -a # shows all open ports and what is connected to these ports

route   # shows a routing table

# =====================
history 10 # last 10 command
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
