#!/usr/bin/env python

import sys

filename = sys.argv[1]
print filename

with open (filename, "r") as myfile:
    data=myfile.read()

position = data.find("PAR 2.0\x00Creator")
if position >= 0:
        mylist = data[position:].split('\x00')
        creator = mylist[2]
        print "creator:", creator
