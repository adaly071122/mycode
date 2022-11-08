#!/usr/bin/env python3


"""A simple script to move two files into ceph_storage/"""

# standard library imports

import shutil
import os


def main():




    os.chdir('/home/student/mycode/')      # move into this working directory

    shutil.move('raynor.obj', 'ceph_storage/') # try moving the file raynor.obj into ceph_storage/ dir

    # program will pause while we accept input
    xname = input('What is the new name for kerrigan.obj? ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # moving kerrigan.obj into ceph_storagewith new name

main() # this calls our main function

