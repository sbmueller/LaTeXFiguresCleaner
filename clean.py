# small script that deletes unused graphic files in a latex project.
# specify graphic directory and logfile. Unused files will be deleted in specified directory.

import os

directory = 'figures'
logfile = 'rus.log'

for filename in os.listdir(directory):
    if filename in open(logfile).read():
        print filename + " in use."
    else:
        if os.path.isfile(filename):
            print filename + " not in use - deleting."
            os.remove(directory + "/" + filename)
        else:
            print filename + " is a directory."
