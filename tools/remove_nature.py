#!/usr/bin/env python3
# remove_nature.py - ポケモンデータから nature フィールドを削除するスクリプト

import json
import os

def remove_nature_field():
    # データセットのパスを取得
    dataset_path = os.path.join(os.path.dirname(__file__), '../data/pokemon_dataset.json')
    
    # ファイルを読み込む
    with open(dataset_path, 'r', encoding='utf-8') as f:
        pokemons = json.load(f)
    
    # 各ポケモンの nature フィールドを削除
    for pokemon in pokemons:
        if isinstance(pokemon, dict) and 'nature' in pokemon:
            del pokemon['nature']
    
    # 変更を保存
    with open(dataset_path, 'w', encoding='utf-8') as f:
        json.dump(pokemons, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully removed 'nature' field from {len(pokemons)} Pokémon entries")

if __name__ == '__main__':
    remove_nature_field()
