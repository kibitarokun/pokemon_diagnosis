#!/usr/bin/env python3
# remove_age_gender.py - pokemon_extra.jsonからageとgenderフィールドを削除

import json
import os

def remove_age_gender_fields():
    # エクストラデータのパスを取得
    extra_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/pokemon_extra.json')
    
    # ファイルを読み込む
    with open(extra_path, 'r', encoding='utf-8') as f:
        pokemon_extra = json.load(f)
    
    # 各ポケモンのage, genderフィールドを削除
    count = 0
    for pokemon in pokemon_extra:
        if isinstance(pokemon, dict):
            if 'age' in pokemon:
                del pokemon['age']
                count += 1
            if 'gender' in pokemon:
                del pokemon['gender']
                count += 1
    
    # 変更を保存
    with open(extra_path, 'w', encoding='utf-8') as f:
        json.dump(pokemon_extra, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully removed 'age' and 'gender' fields from pokemon_extra.json")
    print(f"Total fields removed: {count}")

if __name__ == '__main__':
    remove_age_gender_fields()
