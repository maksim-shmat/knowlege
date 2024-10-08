"""Install distributive from flash."""

#1 check name flashdrive

lsblk

#2 unmount flash for write mode

sudo umount /dev/sda

#3 write .iso

cd to path_of_.iso
sudo dd if=path_where.iso of=/dev/sda bs=4M

and in "Discs" > options > edit partition and <check> Legacy BIOS Bootable

#4 For Bootable Flashdrive with partition

After previous steps, create partition with <+> in "Discs"
I`m crate 32Gb, ext4

usb=/dev/sda

# Create ext4

# Create filesystem
# or sudo parted /dev/sda mklabel gpt    # for GPT
# or sudo parted /dev/sda mklabel msdos  # for MBR

# Next
sudo parted -a opt /dev/sda mkpart primary ext4 0% 100% (0% 100% mean from start to the finish flashdrive)

# Next
sudo mkfs.ext4 -L persistence ${usb}2
or
sudo mkfs.ext4 -L datapartition /dev/sda2

#! Show Edit Partition in "Discs" > options, and then: Type = Linux Filesistem, Flags = System Partition (check it)
#RESULTS:
size 32Gb
Contents Ext4
Device /dev/sda2
Partition Type Linux Filesystem (System)  # for no clean/rewrite this data

# Next
usb=/dev/sda2  # sda1 Kali, sda is free

sudo mkdir -p /mnt/my_usb

sudo mount /dev/sda2/mnt/my_usb

echo "/ union" | sudo tee /mnt/my_usb/persistence.conf

sudo umount ${usb}  # or umount /mnt/my_usb

#5 $ reboot and press F12

# Ok on Kali, persistence not working

mkdir -p /mnt/USB
mount /dev/sda2 /mnt/USB
echo "/ union" >> /mnt/USB/persistence.conf
umount /dev/sda2
reboot

#6 Trubles and resolves
By default from "Disks" mountet in /media/

sudo mkdir -p /mnt/Kali
sudo mkdir -p /mnt/persistence

sudo mount /dev/sda1 /mnt/Kali/
sudo mount /dev/sda2 /mnt/persistence
sudo echo "/mnt/persistence/" | sudo tee /mnt/persistence.conf

#7 Fail, permission denied for persistence
ok chmod

sudo chmod u=rwx,g=r,p=r file #? file or dir?
sudo 744 file  # analog: for user write/read/execute(7) for othe read(4)
... for dir no results
maybe for .conf need acces?
