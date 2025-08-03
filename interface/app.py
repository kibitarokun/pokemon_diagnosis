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
        result = knn_predict(user, k=3)
    # 選択肢用データ
    all_types = [
        ('normal', 'ノーマル'), ('fire', 'ほのお'), ('water', 'みず'), ('electric', 'でんき'), ('grass', 'くさ'),
        ('ice', 'こおり'), ('fighting', 'かくとう'), ('poison', 'どく'), ('ground', 'じめん'), ('flying', 'ひこう'),
        ('psychic', 'エスパー'), ('bug', 'むし'), ('rock', 'いわ'), ('ghost', 'ゴースト'), ('dragon', 'ドラゴン'),
        ('dark', 'あく'), ('steel', 'はがね'), ('fairy', 'フェアリー')
    ]
    all_abilities = [
        ('overgrow', 'しんりょく'), ('chlorophyll', 'ようりょくそ'), ('blaze', 'もうか'), ('solar-power', 'サンパワー'),
        ('torrent', 'げきりゅう'), ('rain-dish', 'あめうけざら'), ('shield-dust', 'りんぷん'), ('run-away', 'にげあし'),
        ('shed-skin', 'だっぴ'), ('compound-eyes', 'ふくがん'), ('swarm', 'むしのしらせ'), ('keen-eye', 'するどいめ'),
        ('tangled-feet', 'ちどりあし'), ('big-pecks', 'はとむね'), ('guts', 'こんじょう')
    ]
    all_stats = [
        ('hp', 'HP'), ('attack', 'こうげき'), ('defense', 'ぼうぎょ'),
        ('special-attack', 'とくこう'), ('special-defense', 'とくぼう'), ('speed', 'すばやさ')
    ]
    personalities = ['おだやか','せっかち','まじめ','おっとり','やんちゃ','ずるがしこい','がんばりや','おくびょう','のんびり']
    activities = ['スポーツ','読書','音楽','冒険','料理','ゲーム','自然散策','友達と遊ぶ']
    dislikes = ['虫','暗い場所','大きな音','寒さ','暑さ','水','運動','勉強']
    genders = ['男性','女性','その他']
    return render_template('index.html', result=result, all_types=all_types, all_abilities=all_abilities, all_stats=all_stats,
        personalities=personalities, activities=activities, dislikes=dislikes, genders=genders)

if __name__ == '__main__':
    app.run(debug=True)
