import json
import requests
import time
import os

dataset_path = os.path.join(os.path.dirname(__file__), '../data/pokemon_dataset.json')
with open(dataset_path, encoding='utf-8') as f:
    pokemons = json.load(f)

for p in pokemons:
    if 'flavor_text' not in p or not p['flavor_text']:
        pid = p['id']
        url = f'https://pokeapi.co/api/v2/pokemon-species/{pid}/'
        try:
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                species = res.json()
                flavor = ''
                for entry in species.get('flavor_text_entries', []):
                    if entry['language']['name'] == 'ja-Hrkt':
                        flavor = entry['flavor_text'].replace('\n', '').replace('\u3000', '')
                        break
                p['flavor_text'] = flavor
                print(f"Added flavor_text for {pid}: {p['name']}")
            else:
                p['flavor_text'] = ''
        except Exception as e:
            print(f"Error {pid}: {e}")
        time.sleep(1)

with open(dataset_path, 'w', encoding='utf-8') as f:
    json.dump(pokemons, f, ensure_ascii=False, indent=2)
