#!/usr/bin/python
#Written by Christine Fossaceca
#This code writes the MalStor Banner
#This code changes to the laikaboss directory (git tree)
#This code prints the working directory
#This code invokes laika.py on the executable 0.exe
import os

os.chdir("/home/wildcat/Lockheed/laikaboss")
os.system("pwd")

malware = '0.exe'

os.system("./laika.py {}".format(malware))
