# APIテストスクリプト
import requests

url = 'http://127.0.0.1:5000/diagnose'

payload = {
    "types": ["fire", "flying"],
    "abilities": ["blaze"],
    "important_stats": ["speed", "attack"],
    "k": 3
}

response = requests.post(url, json=payload)
print('Status:', response.status_code)
print('Result:', response.json())
