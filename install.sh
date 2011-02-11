#!/bin/bash
src=$(dirname $0)
install_dir="$HOME/.gnome2/rhythmbox/plugins"

if [ -e "$src/skip.rb-plugin" ]; then
    echo  -n "installing: ";
    sed 's/^Description=//;t;d' "$src/skip.rb-plugin";
    echo "To $install_dir";
else
   echo "bah couldn't find plugin"
fi

mkdir -p $install_dir;
if ! mv $src $install_dir; then
    echo "REMOVE the plugin if you want to install it again"
else
    echo "RESTART Rhythmbox, installation done I think"
    echo -------------------
    echo "you need to  enable the plugin in 'Edit->Plugin modules->skip'"
fi


