#!/usr/bin/python
import os

#Read in the path with user input (or navigate to the directory in the GUI)
#path = '/home/wildcat/Lockheed/laikaboss/malware/' 

path = raw_input("Enter the path of your file: ")

#if the path doesn't work, throw an error
assert os.path.exists(path), "I did not find the file at, "+str(path)

#For every file in the directory, run the laika.py script
for f in os.listdir(path):
	os.system("./laika.py {}".format(os.path.join(path,f)))
