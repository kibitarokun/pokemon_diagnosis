#!/usr/bin/env python3
# remove_nature_json.py - JSONデータを直接操作してnatureフィールドを削除

import json
import os

def remove_nature_field():
    # データセットのパスを取得
    dataset_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/pokemon_dataset.json')
    
    # ファイルを読み込む
    with open(dataset_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    try:
        # JSONをパース
        data = json.loads(content)
        
        # 各ポケモンからnatureフィールドを削除
        count = 0
        for pokemon in data:
            if isinstance(pokemon, dict) and 'nature' in pokemon:
                del pokemon['nature']
                count += 1
                
        # 変更されたJSONを保存
        with open(dataset_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        print(f"Successfully removed 'nature' field from {count} Pokémon entries")
        
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {str(e)}")
        # JSONパースエラーの場合、正規表現で置換を試みる
        import re
        modified_content = re.sub(r',\s*"nature":\s*null', '', content)
        
        # 修正したコンテンツを保存
        with open(dataset_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
            
        print("Used regex to remove 'nature' field")

if __name__ == '__main__':
    remove_nature_field()
