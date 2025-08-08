# APIテストスクリプト
import requests

url = 'http://127.0.0.1:5000/diagnose'

payload = {
    "types": ["fire", "flying"],
    "abilities": ["blaze"],
    "important_stats": ["speed", "attack"],
    "personality": "おだやか",
    "activities": ["スポーツ", "読書"],
    "dislikes": ["高所", "虫"],
    "k": 3 # 近傍数
}

response = requests.post(url, json=payload)
print('Status:', response.status_code)
print('Result:', response.json())
