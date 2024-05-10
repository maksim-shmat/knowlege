"""How check microSD about."""

#0 Format standard means from ubuntu discks

#1 Format flash to FAT32

mkfs.vfat /dev/sda

#1.1 Init with copy to

Copy file fo mount disc

#2 f3 write

f3write /media/jack/7964-494A  # write with 1Gb blocks (16 hours for 128Gb, then it 900mb instead)

#3 f3 preserve easy check

sudo f3probe --destructive --time-ops /dev/sda  # check lightly

#4

f3read /media/jack/7964-794A  # read corrupted blocks (13 hours)
