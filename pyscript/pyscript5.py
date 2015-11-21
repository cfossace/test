import requests
import hashlib
import os
import json

USERNAME = 'christine'
API_KEY = 'd0e4164c2bd99f1f888477fc25cf8c5c104a5cd1'


#Read in the path with user input (or navigate to the directory in the GUI)
#path = '/home/wildcat/Lockheed/laikaboss/malware/' 

os.chdir("/home/wildcat/Lockheed/laikaboss")
print("Hint: /home/wildcat/Lockheed/laikaboss/malware/")
path = raw_input("Enter the path of your file: ")

for f in os.listdir(path):
	os.system("sudo python laika.py {} | jq '.scan_result[]' > /home/wildcat/Lockheed/crits/pyscript/mal3/{}.out".format(os.path.join(path,f), f))

os.chdir("/home/wildcat/Lockheed/crits/pyscript/mal3/")
path2 = "/home/wildcat/Lockheed/crits/pyscript/mal3/"

for k in os.listdir(path2):
	os.system("python single.py {}".format(k))
	

