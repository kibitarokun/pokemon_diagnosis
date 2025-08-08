# ポケモン診断API（Flask）
from flask import Flask, request, jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from domain.user_profile import UserProfile
from application.knn_model import knn_predict

app = Flask(__name__)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.json
    user = UserProfile(
        types=data.get('types', []),
        abilities=data.get('abilities', []),
        important_stats=data.get('important_stats', []),
        personality=data.get('personality'),
        activities=data.get('activities', []),
        dislikes=data.get('dislikes', [])
    )
    result = knn_predict(user, k=data.get('k', 3))
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
