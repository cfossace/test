import requests
import hashlib
import os
import json

USERNAME = 'christine'
API_KEY = 'd0e4164c2bd99f1f888477fc25cf8c5c104a5cd1'


os.chdir("/home/wildcat/Lockheed/crits/pyscript/mal3/")
path2 = "/home/wildcat/Lockheed/crits/pyscript/mal3/"

for k in os.listdir(path2):
	os.system("python single.py {}".format(k))
	

