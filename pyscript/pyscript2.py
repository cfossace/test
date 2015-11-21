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

for f in os.listdir(path2):
	read_data = open(f,'r')

	md5_data = json.load(read_data)

	file_data = open(f, 'r').read()

	md5 = md5_data['moduleMetadata']['META_HASH']['HASHES']['md5']

	data = {'upload_type': 'metadata',
        'filename': f,
        'md5': md5,
        'source': 'Christine'}
	files = {'filedata': open(f, 'rb')}

	url = 'http://localhost:8080/api/v1/samples/?username={0}&api_key={1}'.format(USERNAME, API_KEY)

	r = requests.post(url, data=data, files=files)

