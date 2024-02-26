#!/usr/bin/env python
""" tail - efficiently display the last lines of a file.
License: 3-clause BSD (see https://opensource.org/licenses/BSD-3-Clause)
Author: Tom Lang
"""

import argparse
import os
import io

# Instantiate the parser
parser = argparse.ArgumentParser(description='Efficiently display the last lines of a file')

parser.add_argument('-f', action='store_true',
                    help='Watch the file continuously for changes')
parser.add_argument('-n', action='store_true',
                    help='Show the last N lines')
parser.add_argument('lines', type=int, nargs='?',
                    help='Number of lines to show')
parser.add_argument('file', nargs='?',
                    help='File to read')

args = parser.parse_args()

if args.n and args.lines == None:
    parser.error("Need to specify the number of lines to show")
if args.file == None:
    parser.error("Need to specify the file to read")

lines = 0
offset = -1
f = open(args.file, 'rb')
offset = f.seek(0, os.SEEK_END) - 1
while lines < args.lines:
    f.seek(offset)
    char = f.read(1)
    if char == '\n':
        lines += 1
    offset -= 1
for line in f:
    print(line)

