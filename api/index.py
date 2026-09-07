# Vercel用エントリポイント
# interface/app.py の Flask アプリをそのまま公開する
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from interface.app import app  # noqa: E402,F401 (Vercelがこの`app`をWSGIアプリとして利用する)
