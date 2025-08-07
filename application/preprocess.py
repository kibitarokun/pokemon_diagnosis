# データ前処理（ベクトル化・数値化）
import json
import numpy as np
from typing import List, Dict
import os

def load_pokemon_dataset(path: str) -> List[Dict]:
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def load_pokemon_extra(path: str) -> Dict[str, Dict]:
    """ポケモンのエクストラデータをロードし、名前をキーとする辞書として返す"""
    with open(path, encoding='utf-8') as f:
        extra_list = json.load(f)
        return {item['name']: item for item in extra_list if 'name' in item}

def get_all_types(pokemons: List[Dict]) -> List[str]:
    types = set()
    for p in pokemons:
        types.update(p['types'])
    return sorted(list(types))

def get_all_abilities(pokemons: List[Dict]) -> List[str]:
    abilities = set()
    for p in pokemons:
        abilities.update(p['abilities'])
    return sorted(list(abilities))

def vectorize_pokemon(pokemon: Dict, all_types: List[str], all_abilities: List[str], 
                    personalities: list, activities: list, dislikes: list, 
                    extra_data: Dict[str, Dict]) -> np.ndarray:
    # タイプと特性はOne-Hotエンコーディング
    type_vec = [1 if t in pokemon['types'] else 0 for t in all_types]
    ability_vec = [1 if a in pokemon['abilities'] else 0 for a in all_abilities]
    # 種族値を正規化（0-1の範囲にスケール）
    stats_vec = [pokemon['stats'][k] / 255.0 for k in ['hp','attack','defense','special-attack','special-defense','speed']]
    
    # extra_dataから性格と好き嫌いの情報を取得
    pokemon_name = pokemon.get('name', '')
    extra = extra_data.get(pokemon_name, {})
    
    # 性格: one-hot
    personality_vec = [1 if ('personality' in extra and extra['personality'] == p) else 0 for p in personalities]
    
    # 好きなこと・嫌いなこと
    activities_vec = [1 if ('like' in extra and extra['like'] == a) else 0 for a in activities]
    dislikes_vec = [1 if ('dislike' in extra and extra['dislike'] == d) else 0 for d in dislikes]
    
    return np.array(type_vec + ability_vec + stats_vec + personality_vec + activities_vec + dislikes_vec)

def main():
    dataset_path = os.path.join(os.path.dirname(__file__), '../data/pokemon_dataset.json')
    extra_path = os.path.join(os.path.dirname(__file__), '../data/pokemon_extra.json')
    
    pokemons = load_pokemon_dataset(dataset_path)
    extra_data = load_pokemon_extra(extra_path)
    
    all_types = get_all_types(pokemons)
    all_abilities = get_all_abilities(pokemons)
    personalities = ['おだやか','せっかち','まじめ','おっとり','やんちゃ','ずるがしこい','がんばりや','おくびょう','のんびり']
    activities = ['運動','読書','音楽','冒険','料理','ゲーム','自然歩き','友達と遊ぶ']
    dislikes = ['虫','暗い場所','大きな音','寒さ','暑さ','水','運動','勉強']
    
    vectors = [vectorize_pokemon(p, all_types, all_abilities, personalities, activities, dislikes, extra_data) for p in pokemons]
    # ベクトル化したデータを保存
    np.save(os.path.join(os.path.dirname(__file__), '../data/pokemon_vectors.npy'), np.array(vectors))
    print('ベクトル化完了: data/pokemon_vectors.npy')
    print(f'処理したポケモン数: {len(vectors)}')
    print(f'エクストラデータ適用ポケモン数: {sum(1 for p in pokemons if p.get("name") in extra_data)}')

if __name__ == '__main__':
    main()
