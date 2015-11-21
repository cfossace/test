#!/usr/bin/python
#Written by Christine Fossaceca

import os

#Read in the path with user input (or navigate to the directory in the GUI)
#path = '/home/wildcat/Lockheed/laikaboss/malware/' 

os.chdir("/home/wildcat/Lockheed/laikaboss")
print("Hint: /home/wildcat/Lockheed/laikaboss/malware/")
path = raw_input("Enter the path of your file: ")

#if the path doesn't work, throw an error
assert os.path.exists(path), "I did not find the file at, "+str(path)
i = 0;
#For every file in the directory, run the laika.py script
for f in os.listdir(path):
	os.system("./laika.py {} | jq '.scan_result[]' > {}out.txt".format(os.path.join(path,f), i))
        i+= 1
