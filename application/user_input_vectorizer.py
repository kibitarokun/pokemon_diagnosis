# ユーザー入力をベクトル化するユースケース
import numpy as np
from domain.user_profile import UserProfile
import json
import os

def load_metadata():
    dataset_path = os.path.join(os.path.dirname(__file__), '../data/pokemon_dataset.json')
    with open(dataset_path, encoding='utf-8') as f:
        pokemons = json.load(f)
    all_types = sorted({t for p in pokemons for t in p['types']})
    all_abilities = sorted({a for p in pokemons for a in p['abilities']})
    personalities = ['おだやか','せっかち','まじめ','おっとり','やんちゃ','ずるがしこい','がんばりや','おくびょう','のんびり']
    activities = ['運動','読書','音楽','冒険','料理','ゲーム','自然歩き','友達と遊ぶ']
    dislikes = ['虫','暗い場所','大きな音','寒さ','暑さ','水','運動','勉強']
    return all_types, all_abilities, personalities, activities, dislikes

def vectorize_user_profile(user: UserProfile, all_types, all_abilities, personalities, activities, dislikes) -> np.ndarray:
    # types, abilities, important_statsをポケモンと同じ形式でベクトル化
    type_vec = [1 if user.types and t in user.types else 0 for t in all_types]
    ability_vec = [1 if user.abilities and a in user.abilities else 0 for a in all_abilities]
    stats_keys = ['hp','attack','defense','special-attack','special-defense','speed']
    stats_vec = [1 if user.important_stats and k in user.important_stats else 0 for k in stats_keys]
    # personality: one-hot
    personality_vec = [1 if user.personality == p else 0 for p in personalities]
    # activities: multi-hot
    activities_vec = [1 if user.activities and a in user.activities else 0 for a in activities]
    # dislikes: multi-hot
    dislikes_vec = [1 if user.dislikes and d in user.dislikes else 0 for d in dislikes]
    return np.array(type_vec + ability_vec + stats_vec + personality_vec + activities_vec + dislikes_vec)

# サンプル利用例
def main():
    all_types, all_abilities, personalities, activities, dislikes = load_metadata()
    user = UserProfile(
        types=['fire', 'flying'],
        abilities=['blaze'],
        important_stats=['speed', 'attack'],
        memo=None
    )
    vec = vectorize_user_profile(user, all_types, all_abilities, personalities, activities, dislikes)
    print('ユーザーベクトル:', vec)

if __name__ == '__main__':
    main()
