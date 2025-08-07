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
    all_types, all_abilities, personalities, activities, dislikes = load_metadata()
    user_vec = vectorize_user_profile(user, all_types, all_abilities, personalities, activities, dislikes)
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
    user_types = user_vec[:len_types]
    user_abilities = user_vec[len_types:len_types+len_abilities]
    user_stats = user_vec[len_types+len_abilities:len_types+len_abilities+len_stats]
    user_personality = user_vec[len_types+len_abilities+len_stats:len_types+len_abilities+len_stats+len_personality]
    user_activities = user_vec[len_types+len_abilities+len_stats+len_personality:len_types+len_abilities+len_stats+len_personality+len_activities]
    user_dislikes = user_vec[len_types+len_abilities+len_stats+len_personality+len_activities:]
    
    pokemon_types = pokemon_vec[:len_types]
    pokemon_abilities = pokemon_vec[len_types:len_types+len_abilities]
    pokemon_stats = pokemon_vec[len_types+len_abilities:len_types+len_abilities+len_stats]
    pokemon_personality = pokemon_vec[len_types+len_abilities+len_stats:len_types+len_abilities+len_stats+len_personality]
    pokemon_activities = pokemon_vec[len_types+len_abilities+len_stats+len_personality:len_types+len_abilities+len_stats+len_personality+len_activities]
    pokemon_dislikes = pokemon_vec[len_types+len_abilities+len_stats+len_personality+len_activities:]
    
    # カテゴリごとのマッチ度を計算（ユークリッド距離の類似度）
    # ※値が0のカテゴリは計算から除外
    def calc_match_score(user_cat, poke_cat):
        if np.sum(user_cat) == 0 or np.sum(poke_cat) == 0:
            return 0  # 選択なしの場合は0を返す
        sim = 1 - (np.linalg.norm(user_cat - poke_cat) / np.sqrt(len(user_cat)))
        return max(0, sim)  # 負の値は0にする
    
    # カテゴリごとのマッチスコアを計算
    type_match = calc_match_score(user_types, pokemon_types) * 100
    ability_match = calc_match_score(user_abilities, pokemon_abilities) * 100
    stat_match = calc_match_score(user_stats, pokemon_stats) * 100
    personality_match = calc_match_score(user_personality, pokemon_personality) * 100
    activity_match = calc_match_score(user_activities, pokemon_activities) * 100
    dislike_match = calc_match_score(user_dislikes, pokemon_dislikes) * 100
    
    # チャート用のデータを作成
    chart_data = {
        'labels': ['タイプ', '特性', '能力値', '性格', '好きなこと', '苦手なこと'],
        'user_data': [
            int(np.sum(user_types) > 0) * 100,  # 選択あり:100, なし:0
            int(np.sum(user_abilities) > 0) * 100,
            int(np.sum(user_stats) > 0) * 100,
            int(np.sum(user_personality) > 0) * 100,
            int(np.sum(user_activities) > 0) * 100,
            int(np.sum(user_dislikes) > 0) * 100
        ],
        'pokemon_data': [
            type_match,
            ability_match,
            stat_match,
            personality_match,
            activity_match,
            dislike_match
        ]
    }
    return chart_data

def knn_predict(user: UserProfile, k=1):
    all_types, all_abilities, personalities, activities, dislikes = load_metadata()
    user_vec = vectorize_user_profile(user, all_types, all_abilities, personalities, activities, dislikes)
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
