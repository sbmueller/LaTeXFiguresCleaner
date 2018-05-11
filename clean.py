# small script that deletes unused graphic files in a latex project.
# specify graphic directory and logfile. Unused files will be deleted in specified directory.

import os

directory = 'figures'
logfile = 'test.log'
enc = 'utf-8' # For Overleaf, try 'Latin-1' if issues encountered...

for filename in os.listdir(directory):
    if filename in open(logfile, encoding=enc).read():
        print(filename + ' in use.')
    else:
        if os.path.isfile(os.path.join(directory, filename)):
            print(filename + ' not in use - deleting.')
            os.remove(os.path.join(directory, filename))
        else:
            print(filename + ' is a directory.')
