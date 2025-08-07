#!/usr/bin/env python3
# fetch_japanese_names.py - PokeAPIからポケモンの日本語名を取得

import json
import os
import time
import requests
from typing import Dict, List, Any

def load_json_file(path: str) -> Any:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(data: Any, path: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def fetch_japanese_name(pokemon_id: int) -> str:
    """PokeAPIからポケモンの日本語名を取得"""
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # 日本語名を探す
            for name_entry in data["names"]:
                if name_entry["language"]["name"] == "ja":
                    return name_entry["name"]
            # 日本語名が見つからない場合
            return ""
        else:
            print(f"Error: API request failed for Pokemon ID {pokemon_id} - Status code: {response.status_code}")
            return ""
    except Exception as e:
        print(f"Error fetching data for Pokemon ID {pokemon_id}: {str(e)}")
        return ""

def add_japanese_names():
    # データセットのパスを取得
    base_dir = os.path.dirname(os.path.dirname(__file__))
    dataset_path = os.path.join(base_dir, 'data/pokemon_dataset.json')
    
    # データ読み込み
    pokemons = load_json_file(dataset_path)
    
    # 各ポケモンに日本語名を追加
    updated_count = 0
    total_count = 0
    
    for i, pokemon in enumerate(pokemons):
        if not isinstance(pokemon, dict) or 'id' not in pokemon:
            continue
        
        total_count += 1
        # すでに日本語名がある場合はスキップ
        if 'name_ja' in pokemon and pokemon['name_ja']:
            continue
            
        # 日本語名を取得
        pokemon_id = pokemon['id']
        japanese_name = fetch_japanese_name(pokemon_id)
        
        if japanese_name:
            pokemon['name_ja'] = japanese_name
            updated_count += 1
            print(f"Added Japanese name for {pokemon['name']}: {japanese_name}")
        
        # API制限を避けるため少し待機（20件ごとに3秒）
        if (i + 1) % 20 == 0:
            print(f"Processed {i + 1} Pokemon, sleeping for 3 seconds...")
            time.sleep(3)
    
    # 変更を保存
    save_json_file(pokemons, dataset_path)
    print(f"Successfully added Japanese names to {updated_count} out of {total_count} Pokemon")

if __name__ == '__main__':
    add_japanese_names()
