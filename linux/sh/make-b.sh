echo "__________________________________________________________________________"
lsblk
echo "__________________________________________________________________________"
echo "select the disk from above(sdb, sdc): "
read disk
echo "select the path to the iso: "
read path

echo "preparing..."
umount /dev/$disk
echo "press any key to start the process: "
read any

dd if=$path of=/dev/$disk bs=2M conv=fdatasync status=progress

echo ""
echo "bootable drive created."
