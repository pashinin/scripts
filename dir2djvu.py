#!/usr/bin/env python

# HOW TO USE IT?
#
# 1. Enter a dir with images
# 2. run "dir2djvu"
# 3. You have a file "dirname.djvu" with all images in it ordered by name
#

import os, sys
import fnmatch
import tempfile
import subprocess
from subprocess import call
from subprocess import Popen, PIPE
import ntpath
import shutil
import argparse


files_regex = '*.png'
tmpdir = tempfile.mkdtemp()         # /tmp/.......
curdir = os.getcwd()

# PARSE ARGS
parser = argparse.ArgumentParser(description='Convert a directory with images to a DjVu-file.')
parser.add_argument('-t', '--temp-dir', default='/tmp', help="Directory to store temp pages files.")
parser.add_argument('-i', action='store_true')
parser.add_argument('--png', action='store_true', default=True)
args = parser.parse_args()

def img2djvu(src, dst):
    """
    Convert SRC image file to DST djvu file.
    Arguments:
    - `src`: filename of input image
    - `dst`: filename of output djvu file
    """

    # -crcbnone
    #   Disable the encoding of the chrominance.  Only the luminance
    #   information will be encoded. The resulting image will show in
    #   shades of gray.
    #call(["c44", '-dpi', '100', '-crcbnone', src, dst])
    call(["c44", '-dpi', '100', src, dst])
    return


# DO WORK
try:
    # get files
    files_to_convert = []
    for filename in os.listdir('.'):
        p, f = ntpath.split(filename)   # "path", "fname.ext"
        f, ext = os.path.splitext(f)    # "fname", ".ext"
        ext = ext.lower()
        if ext==".png" or ext==".jpg" or ext==".jpeg" or ext==".bmp":
            files_to_convert.append(os.path.abspath(filename))
    files_to_convert.sort()  # sort files

    # convert images to .djvu pages
    for fname in files_to_convert:
        p, f = ntpath.split(fname)      # "path", "fname.ext"
        f, ext = os.path.splitext(f)    # "fname", ".ext"
        # ppm - all  colors, very big size
        # pnm - gray colors
        # pbm - black & white ONLY
        fname_ppm  = os.path.join(tmpdir, f)+'.pnm'
        fname_djvu = os.path.join(tmpdir, f)+'.djvu'

        # convert images to 1 format
        call(["convert", fname, '-compress', 'lzw', fname_ppm])      # fast
        img2djvu(fname_ppm, fname_djvu)
        os.remove(fname_ppm)

    # create final file
    # djvm book.djvu page1.djvu page2.djvu page3.djvu pageN.djvu
    os.chdir( tmpdir )
    try:
        cmd = 'djvm -c book.djvu *.djvu'
        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
        p.wait()
        out, err = p.communicate()
    except Exception, e:
        print "Error creating a final file."
        print e

    # move final file
    p, f = ntpath.split(curdir)
    if f: dst = os.path.join(curdir, f)+".djvu"
    else: dst = curdir
    try:
        shutil.copy2('book.djvu', dst)
    except Exception, e:
        print "Error moving final file."
        print e
    os.chdir( curdir )

except Exception as e:
    print e
    pass

shutil.rmtree(tmpdir)   # delete tmp dir
