
# データ収集ユースケース
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from infrastructure.pokeapi_client import PokeApiClient
from domain.pokemon import Pokemon
import json

class DataCollector:
    def __init__(self):
        self.client = PokeApiClient()

    def collect_pokemon_data(self, start_id=1, end_id=100):
        pokemons = []
        for pid in range(start_id, end_id+1):
            data = self.client.get_pokemon(pid)
            species = self.client.get_pokemon_species(pid)
            # 日本語の説明文（flavor_text）を抽出
            flavor_text = None
            import re
            for entry in species.get('flavor_text_entries', []):
                if entry['language']['name'] == 'ja':
                    flavor_text = entry['flavor_text']
                    # 改行・タブ・全角/半角スペースをすべて削除
                    flavor_text = re.sub(r'[\s　]+', '', flavor_text)
                    break
            name = data['name']
            types = [t['type']['name'] for t in data['types']]
            abilities = [a['ability']['name'] for a in data['abilities']]
            stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}
            nature = None  # 性格は後で拡張
            # 公式イラストURLを取得
            image_url = data['sprites']['other']['official-artwork']['front_default']
            p = Pokemon(id=pid, name=name, types=types, abilities=abilities, stats=stats, nature=nature)
            p.image_url = image_url
            p.flavor_text = flavor_text
            pokemons.append(p)
        return pokemons

    def save_to_json(self, pokemons, path):
        # image_urlも含めて保存
        def to_dict(p):
            d = p.__dict__.copy()
            if hasattr(p, 'image_url'):
                d['image_url'] = p.image_url
            if hasattr(p, 'flavor_text'):
                d['flavor_text'] = p.flavor_text
            return d
        with open(path, 'w', encoding='utf-8') as f:
            json.dump([to_dict(p) for p in pokemons], f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    collector = DataCollector()
    pokemons = collector.collect_pokemon_data(1, 100)  # 100体取得
    collector.save_to_json(pokemons, "data/pokemon_dataset.json")
