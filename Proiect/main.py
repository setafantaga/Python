# Linux FIND command
import sys
import os, fnmatch, re, glob, datetime, time
from stat import *
from datetime import datetime

# find a file by name
def findbyName(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

# find a file by extension
def findByExtension(path, pattern):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(pattern):
                result.append(os.path.join(root, file))
    return result

# find by size
def findBySize(size, path):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            if os.path.getsize(path) == size:
                result.append(path)
    return result

# find by last date time modified
def findByModifiedTime(path, data_entry):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            if time.ctime(os.path.getmtime(path)) == data_entry:
                result.append(path)
    return result


# find by last date time accessed
def findByCreatedTime(path, data_entry):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            if time.ctime(os.path.getmtime(path)) == data_entry:
                result.append(path)
    return result

# find by permission
def findByPermission(path, mode):
    result = []
    for root, dirs, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            perm = oct(os.stat(path).st_mode)[-3:]
            if (perm == mode):
                result.append(path)
    return result

# define the arguments
sys.argv[0] = "python"
command = sys.argv[1]
arguments = sys.argv[2]
path = sys.argv[3]
value = sys.argv[4]

# if first argument is find than continue, else exit
if(command == "find"):
    # if the second argument is type, find by extension of file
    if(arguments == "-type"):
        # give the input specify that function you have called
        print(findByExtension(path, value))
    # if the second argument is name, find by name of file
    elif (arguments == "-name"):
        # give the name of file
        print(findbyName(value, path))
    # if the second argument is size, find by size of file
    elif (arguments == "-size"):
        # give the size of file
        print(findBySize(int(value), path))
    # if the second argument is mtime, find the file by the last date modified
    elif (arguments == "-mtime"):
        # give the date of file
        print(findByModifiedTime(path, value))
    # if the second argument is ctime, fine the file by the created date of file
    elif (arguments == "-ctime"):
        # give the date of file
        print(findByCreatedTime(path, value))
    # if the second argument is perm, find by kind of permission of file
    elif (arguments == "-perm"):
        # give the permission
        print(findByPermission(path, value))
    else:
        print("We don't know that arguments.")
else:
    exit("We don't know that command")


# import os
# import datetime
# import os.path, time
# print("Last modified: %s" % time.ctime(os.path.getmtime("directory/files/a.txt")))
# print("Created: %s" % time.ctime(os.path.getctime("directory/files/a.txt")))
