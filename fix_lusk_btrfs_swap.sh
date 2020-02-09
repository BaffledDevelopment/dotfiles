 #!/bin/bash
 
OLD_LINE="#keyfile_device_mount_options=\"--options=subvol=__active/__\""
NEW_LINE="keyfile_device_mount_options=\"-t btrfs -o subvol=@,defaults\""
SED_PATT=s:$OLD_LINE:$NEW_LINE:g

if grep -q $OLD_LINE /etc/openswap.conf
then
    sudo sed -i "$SED_PATT" /etc/openswap.conf
    sudo mkinitcpio -p linux54
else
    echo "Swap is aready fixed!"
fi
