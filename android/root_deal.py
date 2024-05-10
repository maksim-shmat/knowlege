"""How get the root."""

#1 install adb and fastboot

sudo apt install adb fastboot

adb version

#2 on the phone

Build number push-push-push
get developers options

USB debugging - on

#3 start daemon

sudo adb start-server

#4 check connection after connect phone by cable

adb devices

#5 see android bowels

adb shell

ls


