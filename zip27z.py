#!/usr/bin/env python3

from __future__ import print_function
import os
import sys
import fnmatch
import tempfile
import subprocess
from subprocess import call
from subprocess import Popen, PIPE
import ntpath
import shutil
import argparse

if __name__ == "__main__":
    # PARSE ARGS
    parser = argparse.ArgumentParser(description='Convert zip files to 7z.')
    parser.add_argument('-t', '--tempdir', default='/tmp', help="Directory to store temp files.")
    parser.add_argument('-d', '--dir', default='.', help="Directory to store temp files.")
    parser.add_argument('filename', help="Zip file to convert")
    args = parser.parse_args()

    filename = args.filename
    if not os.path.isfile(filename):
        print("Error: No such file -", filename)
        sys.exit(1)

    if not os.path.isdir(args.dir):
        print("Error: No destination dir -", args.dir)
        sys.exit(1)

    if not os.path.isdir(args.tempdir):
        print("Error: No temporary dir -", args.tempdir)
        sys.exit(1)

    tmpdir = tempfile.mkdtemp()
    try:
        call(["unzip", '-qq', '-d', tmpdir, filename])      # extract
        dirbase = os.path.basename(os.path.abspath(filename))
        f, ext = os.path.splitext(dirbase)    # "fname", ".ext"
        call(["7za", 'a', f+".7z", tmpdir+'/*'])    # make 7z
    except Exception as e:
        print("Error:", e)
    shutil.rmtree(tmpdir)   # delete tmp dir
