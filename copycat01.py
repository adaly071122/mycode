#!/usr/bin/env python3


"""Pushing files around using shutil and os from the standard library"""

import shutil

# import additional code to complete our task

import os

def main():

# move into the working directory
    os.chdir("/home/student/mycode/")


# copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")


# copy the entire directoryA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")


if __name__ == "__main__":
    main()


