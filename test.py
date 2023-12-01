import requests
import json

url = 'https://11ea-87-117-63-98.ngrok-free.app/get_text/'

data = {
    'test': 'sadad'
}

response = requests.post(url, data=json.dumps(data))

print(response.json())