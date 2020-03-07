#!/bin/sh

echo_green ()
{
    local TEXT=$1
    echo -e "\e[4;32m$TEXT\e[0m"
}

echo_red ()
{
	local TEXT=$1
	echo -e "\e[4;31m$TEXT\e[0m"
}

link ()
{
    local SOURCE=$1
    local DEST=$2

    if [ -f "$SOURCE" ] || [ -d "$SOURCE" ]
    then
    	echo_green "Linking $SOURCE -> $DEST"
    	mkdir -p $(dirname $DEST) # Make parent dir for destination
    	rm -r $DEST               # Remove existing destination
    	ln -s $SOURCE $DEST       # Link
    else
    	echo_red "$SOURCE does not exist"
	fi
} 

confirm_path ()
{
    if [[ $PWD == *dotfiles ]]
    then
        :
    else
        echo_red "You must be inside dotfiles directory!"
        exit
    fi
}
