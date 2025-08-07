#!/usr/bin/env python3
# generate_pokemon_extra.py - 全ポケモン分のextraデータを生成

import json
import os
import random
from typing import Dict, List, Any

def load_json_file(path: str) -> Any:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json_file(data: Any, path: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def generate_pokemon_extra():
    # パス設定
    base_dir = os.path.dirname(os.path.dirname(__file__))
    dataset_path = os.path.join(base_dir, 'data/pokemon_dataset.json')
    extra_path = os.path.join(base_dir, 'data/pokemon_extra.json')
    
    # データ読み込み
    pokemons = load_json_file(dataset_path)
    
    # 既存のエクストラデータがあれば読み込む
    extra_data = []
    if os.path.exists(extra_path):
        extra_data = load_json_file(extra_path)
        print(f"Loaded {len(extra_data)} existing extra data entries")
    
    # 既存データのマップを作成
    existing_pokemon_map = {entry['name']: entry for entry in extra_data if 'name' in entry}
    
    # パーソナリティ、好き、嫌いのリスト (preprocess.pyと一致させる)
    personalities = ['おだやか', 'せっかち', 'まじめ', 'おっとり', 'やんちゃ', 'ずるがしこい', 'がんばりや', 'おくびょう', 'のんびり']
    activities = ['運動', '読書', '音楽', '冒険', '料理', 'ゲーム', '自然歩き', '友達と遊ぶ']
    dislikes = ['虫', '暗い場所', '大きな音', '寒さ', '暑さ', '水', '運動', '勉強']
    
    # タイプごとのパーソナリティ傾向マッピング
    type_personality_map = {
        'normal': ['おだやか', 'のんびり'],
        'fire': ['せっかち', 'やんちゃ'],
        'water': ['のんびり', 'おだやか'],
        'grass': ['まじめ', 'おだやか'],
        'electric': ['せっかち', 'やんちゃ'],
        'ice': ['おくびょう', 'おっとり'],
        'fighting': ['がんばりや', 'せっかち'],
        'poison': ['ずるがしこい', 'やんちゃ'],
        'ground': ['のんびり', 'まじめ'],
        'flying': ['やんちゃ', 'せっかち'],
        'psychic': ['おっとり', 'まじめ'],
        'bug': ['おくびょう', 'せっかち'],
        'rock': ['がんばりや', 'まじめ'],
        'ghost': ['おくびょう', 'ずるがしこい'],
        'dragon': ['がんばりや', 'やんちゃ'],
        'dark': ['ずるがしこい', 'やんちゃ'],
        'steel': ['まじめ', 'がんばりや'],
        'fairy': ['おっとり', 'おだやか']
    }
    
    # タイプごとの好きなもの傾向マッピング
    type_like_map = {
        'normal': ['友達と遊ぶ', '自然歩き'],
        'fire': ['冒険', '運動'],
        'water': ['水遊び', '自然歩き'],
        'grass': ['自然歩き', '読書'],
        'electric': ['ゲーム', '冒険'],
        'ice': ['料理', '読書'],
        'fighting': ['運動', '冒険'],
        'poison': ['冒険', 'ゲーム'],
        'ground': ['自然歩き', '料理'],
        'flying': ['冒険', '音楽'],
        'psychic': ['読書', '音楽'],
        'bug': ['自然歩き', '友達と遊ぶ'],
        'rock': ['運動', '自然歩き'],
        'ghost': ['音楽', 'ゲーム'],
        'dragon': ['冒険', '運動'],
        'dark': ['ゲーム', '冒険'],
        'steel': ['運動', '読書'],
        'fairy': ['音楽', '友達と遊ぶ']
    }
    
    # タイプごとの嫌いなもの傾向マッピング
    type_dislike_map = {
        'normal': ['大きな音', '暗い場所'],
        'fire': ['水', '寒さ'],
        'water': ['暑さ', '虫'],
        'grass': ['虫', '暗い場所'],
        'electric': ['水', '勉強'],
        'ice': ['暑さ', '虫'],
        'fighting': ['勉強', '読書'],
        'poison': ['勉強', '暗い場所'],
        'ground': ['水', '運動'],
        'flying': ['勉強', '暗い場所'],
        'psychic': ['大きな音', '虫'],
        'bug': ['暗い場所', '寒さ'],
        'rock': ['水', '大きな音'],
        'ghost': ['運動', '勉強'],
        'dragon': ['勉強', '大きな音'],
        'dark': ['運動', '読書'],
        'steel': ['水', '暑さ'],
        'fairy': ['暗い場所', '虫']
    }
    
    # 年齢とジェンダーオプション
    age_range = (2, 15)
    genders = ['♂', '♀', '不明']
    gender_weights = [0.48, 0.48, 0.04]  # 通常の性別分布
    
    # 新しいエクストラデータを生成
    new_extra_data = []
    
    for pokemon in pokemons:
        if not isinstance(pokemon, dict) or 'name' not in pokemon:
            continue
            
        name = pokemon.get('name')
        
        # 既に存在するデータがあればそれを使用
        if name in existing_pokemon_map:
            new_extra_data.append(existing_pokemon_map[name])
            continue
        
        # ポケモンのタイプを取得
        types = pokemon.get('types', [])
        if not types:
            continue
            
        # メインタイプを使用
        main_type = types[0]
        
        # 性格を決定（タイプに基づく）
        personality_options = type_personality_map.get(main_type, personalities)
        personality = random.choice(personality_options)
        
        # 好きなものを決定（タイプに基づく）
        like_options = type_like_map.get(main_type, activities)
        like = random.choice(like_options)
        
        # 嫌いなものを決定（タイプに基づく）
        dislike_options = type_dislike_map.get(main_type, dislikes)
        dislike = random.choice(dislike_options)
        
        # 年齢とジェンダーを決定
        age = random.randint(*age_range)
        gender = random.choices(genders, weights=gender_weights)[0]
        
        # エクストラデータを生成
        extra_entry = {
            "name": name,
            "personality": personality,
            "like": like,
            "dislike": dislike,
            "age": age,
            "gender": gender
        }
        
        new_extra_data.append(extra_entry)
    
    # 新しいデータを保存
    save_json_file(new_extra_data, extra_path)
    print(f"Generated extra data for {len(new_extra_data)} Pokémon")

if __name__ == '__main__':
    generate_pokemon_extra()
