#!/usr/bin/python
#This code writes the MalStor Banner
#This code changes to the laikaboss directory (git tree)
#This code invokes laika.py on the contents of the folder named "malware"
import os

os.chdir("/home/wildcat/Lockheed/laikaboss")
os.system("pwd")

path = '/home/wildcat/Lockheed/laikaboss/malware/'  


for f in os.listdir(path):
	os.system("./laika.py {}| jq '.scan_result[]' > out.txt".format(os.path.join(path,f)))
