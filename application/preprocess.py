# データ前処理（ベクトル化・数値化）
import json
import numpy as np
from typing import List, Dict
import os

def load_pokemon_dataset(path: str) -> List[Dict]:
    with open(path, encoding='utf-8') as f:
        return json.load(f)

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

def vectorize_pokemon(pokemon: Dict, all_types: List[str], all_abilities: List[str], personalities: list, activities: list, dislikes: list) -> np.ndarray:
    # タイプと特性はOne-Hotエンコーディング
    type_vec = [1 if t in pokemon['types'] else 0 for t in all_types]
    ability_vec = [1 if a in pokemon['abilities'] else 0 for a in all_abilities]
    # 種族値を正規化（0-1の範囲にスケール）
    stats_vec = [pokemon['stats'][k] / 255.0 for k in ['hp','attack','defense','special-attack','special-defense','speed']]
    # 性格: one-hot（nature, extra, flavor_text等から推定。なければ全0）
    personality_vec = [1 if ('nature' in pokemon and pokemon['nature'] == p) else 0 for p in personalities]
    # 趣味・苦手はデータがないので全0
    activities_vec = [0 for _ in activities]
    dislikes_vec = [0 for _ in dislikes]
    return np.array(type_vec + ability_vec + stats_vec + personality_vec + activities_vec + dislikes_vec)

def main():
    dataset_path = os.path.join(os.path.dirname(__file__), '../data/pokemon_dataset.json')
    pokemons = load_pokemon_dataset(dataset_path)
    all_types = get_all_types(pokemons)
    all_abilities = get_all_abilities(pokemons)
    personalities = ['おだやか','せっかち','真面目','おっとり','やんちゃ','ずる賢い','がんばり屋','おく病','のんびり']
    activities = ['運動','読書','音楽','冒険','料理','ゲーム','自然歩き','友達と遊ぶ']
    dislikes = ['虫','暗い場所','大きな音','寒さ','暑さ','水','運動','勉強']
    vectors = [vectorize_pokemon(p, all_types, all_abilities, personalities, activities, dislikes) for p in pokemons]
    # ベクトル化したデータを保存
    np.save(os.path.join(os.path.dirname(__file__), '../data/pokemon_vectors.npy'), np.array(vectors))
    print('ベクトル化完了: data/pokemon_vectors.npy')

if __name__ == '__main__':
    main()
