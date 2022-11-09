#!/usr/bin/python3

loginfail = 0   # counter for fails


keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")
# open the file for reading


 
keystone_file_lines=keystone_file.readlines()
# turn the file into a list of lines in memory

# loop over the list of lines
for line in keystone_file_lines: 
    if "- - - - -] Authorization failed" in line: # if this 'fail pattern' appears in the line... 
        loginfail += 1 # this is the same as loginfail = loginfail + 1

print("The number of failed log in attempts is", loginfail)
keystone_file.close()


    
