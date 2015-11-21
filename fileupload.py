import requests
import os

USERNAME = 'christine'
API_KEY = 'd0e4164c2bd99f1f888477fc25cf8c5c104a5cd1 		'

file_data = open('0.exe', 'rb').read()

data = {'upload_type': 'file',
        'filedata': file_data,
	'password': 'infected',
	'file_format': 'zip',
        'source': 'Christine'
         }

files = {'filedata': open('0.exe', 'rb')}

url = 'http://localhost:8080/api/v1/samples/?username={0}&api_key={1}'.format(USERNAME, API_KEY)

r = requests.post(url, data=data, files=files)
print r.text
