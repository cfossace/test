#!/usr/bin/python
import os


path = '/home/wildcat/Lockheed/laikaboss/malware/'  


for f in os.listdir(path):
	os.system("./laika.py {}".format(os.path.join(path,f)))
