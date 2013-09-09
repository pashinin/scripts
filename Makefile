# -*- Makefile -*-

DIR = /usr/src/scripts

menu:
	echo "Creating Nautilus menu items..."
# How to use gconftool to create Nautilus menu items???

update:
	test -d "${DIR}" || cp . "${DIR}"
	git pull

links:
	sudo ln -sf ${DIR}/dir2djvu.py /usr/local/bin/dir2djvu
	sudo ln -sf ${DIR}/zip27z.py /usr/local/bin/zip27z
	sudo ln -sf ${DIR}/ogg/oggart.py /usr/local/bin/oggart

install: update links
#install: menu
