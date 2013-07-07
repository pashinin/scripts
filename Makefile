# -*- Makefile -*-

EMACS = emacs
TEST_DIR = src
TRAVIS_FILE = .travis.yml

# Compile with noninteractive and relatively clean environment.
BATCHFLAGS = -batch -q --no-site-file

install:
#${EMACS} -L src $(BATCHFLAGS) -f batch-byte-compile $(TEST_DIR)/*.el
# copy current dir to /usr/src
	sudo cp -r . /usr/src/imgdir
	sudo ln -sf /usr/src/imgdir/dir2djvu.py /usr/local/bin/dir2djvu
#ln -s dir2djvu.py
