# シンプルでかわいらしいUIのFlaskアプリ
from flask import Flask, render_template, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from domain.user_profile import UserProfile
from application.knn_model import knn_predict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    user_profile = None
    if request.method == 'POST':
        types = request.form.getlist('types')
        abilities = request.form.getlist('abilities')
        important_stats = request.form.getlist('important_stats')
        personality = request.form.get('personality') or None
        activities = request.form.getlist('activities')
        dislikes = request.form.getlist('dislikes')
        user = UserProfile(
            types=types,
            abilities=abilities,
            important_stats=important_stats,
            personality=personality,
            activities=activities,
            dislikes=dislikes,
            memo=None
        )
        # ユーザープロファイルを辞書形式で保存
        user_profile = {
            'types': types,
            'abilities': abilities,
            'important_stats': important_stats,
            'personality': personality,
            'activities': activities,
            'dislikes': dislikes
        }
        result = knn_predict(user, k=3)
    # 選択肢用データ
    all_types = [
        ('normal', 'ノーマル'), ('fire', '火'), ('water', '水'), ('electric', '電気'), ('grass', '草'),
        ('ice', '氷'), ('fighting', '格闘'), ('poison', '毒'), ('ground', '地面'), ('flying', '空'),
        ('psychic', '超能力'), ('bug', '虫'), ('rock', '岩'), ('ghost', 'ゴースト'), ('dragon', 'ドラゴン'),
        ('dark', '悪'), ('steel', '鋼'), ('fairy', '妖精')
    ]
    all_abilities = [
        ('overgrow', '植物パワー'), ('chlorophyll', '太陽好き'), ('blaze', '火の力'), ('solar-power', '太陽パワー'),
        ('torrent', '水の力'), ('rain-dish', '雨で回復'), ('shield-dust', '粉で防御'), ('run-away', '逃げ足'),
        ('shed-skin', '皮がぬける'), ('compound-eyes', '大きな目'), ('swarm', '虫の仲間'), ('keen-eye', '良い目'),
        ('tangled-feet', 'ふらつく'), ('big-pecks', 'がんじょう'), ('guts', '負けない心')
    ]
    all_stats = {
        'hp': 'HP',
        'attack': '攻撃',
        'defense': '防御', 
        'special-attack': '特殊攻撃',
        'special-defense': '特殊防御',
        'speed': 'すばやさ'
    }
    personalities = ['おだやか','せっかち','まじめ','おっとり','やんちゃ','ずるがしこい','がんばりや','おくびょう','のんびり']
    activities = ['運動','読書','音楽','冒険','料理','ゲーム','自然歩き','友達と遊ぶ']
    dislikes = ['虫','暗い場所','大きな音','寒さ','暑さ','水','運動','勉強']
    genders = ['男性','女性','その他']
    return render_template('index.html', result=result, all_types=all_types, all_abilities=all_abilities, all_stats=all_stats,
        personalities=personalities, activities=activities, dislikes=dislikes, genders=genders, user_profile=user_profile)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
