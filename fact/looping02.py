#!/usr/bin/env python3

"""For - Using a file's lines as a source for the for-loop"""


dnsfile = open("dnsservers.txt", "r")
# open file in read mode


# create list of lines
dnslist = dnsfile.readlines()

# loop over lines
for svr in dnslist:
    print(svr, end="")

# close the file (we created the list of lines)
dnsfile.close()

