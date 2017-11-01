# -*- Makefile -*-

# DIR = /usr/src/scripts
DIR = `pwd`
host = `hostname`

ubuntu-desktop:
	(cd ubuntu-setup; sh setup.sh)

menu:
	echo "Creating Nautilus menu items..."
# How to use gconftool to create Nautilus menu items???

update:
	test -d "${DIR}" || sudo cp -r . "${DIR}"
	git pull

links:
	sudo ln -sf ${DIR}/dir2djvu.py /usr/local/bin/dir2djvu
	sudo ln -sf ${DIR}/zip27z.py /usr/local/bin/zip27z
	sudo ln -sf ${DIR}/ogg/oggart.sh /usr/local/bin/oggart
	sudo ln -sf ${DIR}/ogg/oggcover64.py /usr/local/bin/oggcover64

install: links
#install: menu


cluster:
	(cd ubuntu-setup; sh setup.sh)
