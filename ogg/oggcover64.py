#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script's output is a correct base64(header+img) of image to use
# as a cover art for OGG file
#
# Format description:
# https://xiph.org/flac/format.html#metadata_block_picture

import os, sys
import argparse
import base64, struct

if __name__ == "__main__":
    # PARSE ARGS
    parser = argparse.ArgumentParser(description='Make a correct base64(header+img) of cover art for ogg.')
    parser.add_argument('filename', help="Cover image (JPG)")
    args = parser.parse_args()

    filename = args.filename
    size = os.path.getsize(filename)

    data = b"\x00\x00\x00\x03"         # front cover (3)
    data += b"\x00\x00\x00\x0A"        # 10 - length of "image/jpeg"
    data += "image/jpeg"
    data += b"\x00\x00\x00\x00"        # The length of the description string in bytes
    data += b"\x00"*16                 # ...
    data += struct.pack("!L4", size)   # size of file
    data += open(filename, "rb").read()

    print base64.b64encode(data)
