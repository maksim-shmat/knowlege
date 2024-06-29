"""How check microSD about."""

#0 Format standard means from ubuntu discks

#1 Format flash to FAT32

mkfs.vfat /dev/sda  # mkfs.ext4 persistence -L /dev/sda (check it)

# mkfs variants
fs(5), badblocks(8), fsck(8), mkdosfs(8), mke2fs(8), mkfs.bfs(8),
       mkfs.ext2(8), mkfs.ext3(8), mkfs.ext4(8), mkfs.minix(8),
       mkfs.msdos(8), mkfs.vfat(8), mkfs.xfs(8)

#1.1 Init with copy to

Copy file fo mount disc

#2 f3 write

f3write /media/jack/7964-494A  # write with 1Gb blocks (16 hours for 128Gb, then it 900mb instead)

#3 f3 preserve easy check

sudo f3probe --destructive --time-ops /dev/sda  # check lightly

#4

f3read /media/jack/7964-794A  # read corrupted blocks (13 hours)
