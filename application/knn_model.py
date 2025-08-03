
# k-NNによるポケモン診断モデル
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import numpy as np
import json
from typing import List, Dict
from domain.user_profile import UserProfile
from application.user_input_vectorizer import load_metadata, vectorize_user_profile

def load_pokemon_vectors() -> np.ndarray:
    vec_path = os.path.join(os.path.dirname(__file__), '../data/pokemon_vectors.npy')
    return np.load(vec_path)

def load_pokemon_dataset() -> List[Dict]:
    dataset_path = os.path.join(os.path.dirname(__file__), '../data/pokemon_dataset.json')
    with open(dataset_path, encoding='utf-8') as f:
        return json.load(f)

def knn_predict(user: UserProfile, k=1):
    all_types, all_abilities, personalities, activities, dislikes, genders = load_metadata()
    user_vec = vectorize_user_profile(user, all_types, all_abilities, personalities, activities, dislikes, genders)
    pokemon_vecs = load_pokemon_vectors()
    pokemons = load_pokemon_dataset()
    # 距離計算（ユーザー入力と各ポケモンのベクトル）
    dists = np.linalg.norm(pokemon_vecs - user_vec, axis=1)
    sorted_idxs = np.argsort(dists)
    # 仲良し: 2番目に近い, 天敵: 一番遠い
    best_idx = sorted_idxs[0]
    friend_idx = sorted_idxs[1] if len(sorted_idxs) > 1 else sorted_idxs[0]
    enemy_idx = sorted_idxs[-1]
    max_dist = np.max(dists) if np.max(dists) > 0 else 1
    min_dist = np.min(dists)
    def make_result(i):
        score = 1 - (dists[i] - min_dist) / (max_dist - min_dist) if max_dist != min_dist else 1.0
        match_percent = int(score * 100)
        p = pokemons[i].copy() if isinstance(pokemons[i], dict) else pokemons[i].__dict__.copy()
        p['match_percent'] = match_percent
        return p
    return {
        'best': make_result(best_idx),
        'friend': make_result(friend_idx),
        'enemy': make_result(enemy_idx)
    }

# サンプル利用例
def main():
    user = UserProfile(
        types=['fire', 'flying'],
        abilities=['blaze'],
        important_stats=['speed', 'attack'],
        personality=None,
        memo=None
    )
    result = knn_predict(user, k=3)
    print('診断結果:')
    for p in result:
        print(f"{p['id']}: {p['name']} (types: {p['types']}, abilities: {p['abilities']})")

if __name__ == '__main__':
    main()
