import requests
import hashlib
import os
import json

USERNAME = 'christine'
API_KEY = 'd0e4164c2bd99f1f888477fc25cf8c5c104a5cd1'


os.chdir("/home/wildcat/Lockheed/crits/pyscript/mal3/")
path2 = "/home/wildcat/Lockheed/crits/pyscript/mal3/"

for k in os.listdir(path2):
	read_data = open(k,'r')
        md5_data = json.load(read_data)
        file_data = open(k, 'r').read()
        #my_data =json.dumps(read_data)

	md5 = md5_data['moduleMetadata']['META_HASH']['HASHES']['md5']

	data = {'upload_type': 'metadata',
        'filename': k,
        'md5': md5,
        'source': 'Christine'}
	files = {'filedata': open(k, 'rb')}

	url = 'http://localhost:8080/api/v1/samples/?username={0}&api_key={1}'.format(USERNAME, API_KEY)

	r = requests.post(url, data=data, files=files)
	print r.text
