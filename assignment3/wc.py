#!/usr/bin/env python3
# A simple wc-like script.
# prints: # of lines, # of words, # of characters and the filename of corresponding file.
#
# NB: This script differs from wc in at least one important matter:
# wc outputs number of newlines, while this script prints total number of lines.
#
# "wc *" and "wc *.py" - is expanded before they are fed into script, so they work by default.

import sys

def wc(filename):
    lines=0
    words=0
    characters=0
    f = open(filename, 'r')

    for line in f:
        lines += 1
        words += len(line.strip().split())
        characters += len(list(line))
        
    print(str(lines)+" "+str(words)+" "+str(characters)+" "+filename)

del sys.argv[0] #remove first arg (command used to execute script)
for arg in sys.argv: #process all files
    wc(arg)
