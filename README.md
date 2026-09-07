# ポケモン診断アプリケーション

## 概要
ポケモン診断アプリケーションは、ユーザーの特徴や好みをもとに、ぴったりのポケモンを診断する DDD 構成のツールです。機械学習（K近傍法・KNN）を利用し、外部のポケモン API と連携することで、シンプルかつ拡張しやすいユーザー体験を提供します。プロジェクトはドメイン層・アプリケーション層・インフラストラクチャ層・インターフェース層に分割されており、保守性と拡張性を確保しています。

## 補足
表示は主に日本語で、レーダーチャートによってユーザーとポケモンの特徴の一致度を可視化します。日本語のポケモン名や説明文にも対応しています。

## プロジェクト構成

```
application/
    knn_model.py              # 予測用の KNN モデル
    preprocess.py             # データの前処理ユーティリティ
    user_input_vectorizer.py  # ユーザー入力のベクトル化
    add_pokemon_usecase.py    # API からポケモンデータを追加するユースケース

data/
    pokemon_dataset.json      # ポケモンの基本データセット（ID1〜1000 に対応）
    pokemon_extra.json        # 追加データ（性格・好みなど）
    pokemon_vectors.npy       # 前処理済みのポケモンベクトル

domain/
    pokemon.py                # ポケモンのドメインモデル（エンティティ）
    pokemon_repository.py     # ポケモンリポジトリのインターフェース（抽象）
    user_profile.py           # ユーザープロファイルのドメインモデル

infrastructure/
    pokeapi_client.py         # ポケモン API のクライアント
    pokemon_json_repository.py# JSON によるポケモンリポジトリ実装

interface/
    api_test.py               # API のテスト
    api.py                    # API の実装
    app.py                    # アプリケーションのエントリポイント（Flask）
    static/                   # 静的ファイル（JSON、画像など）
    templates/                # Web 画面用の HTML テンプレート

tools/
    add_pokemon_1_1000.py     # API から ID1〜1000 のポケモンを一括追加するスクリプト
    fetch_flavor_text.py      # ポケモンの説明文を取得するスクリプト
    fetch_japanese_names.py   # ポケモンの日本語名を取得するスクリプト
    generate_pokemon_extra.py # 追加データを生成するスクリプト
```

## 主な機能
- **ポケモン診断**: ユーザーの入力からポケモンを予測します。
- **機械学習**: KNN による精度の高い予測を行います。
- **API 連携**: 外部のポケモン API（PokeAPI）からデータを取得・拡張します。
- **DDD 構成**: ドメイン駆動設計により関心事を明確に分離しています。
- **データの自動拡張**: 付属スクリプトで ID1000 までデータセットを簡単に拡張できます。
- **Web インターフェース**: 使いやすい Web 画面から操作できます。
- **レーダーチャート表示**: 一致する特徴を視覚的に確認できます。
- **日本語対応**: 日本語のポケモン名・説明文を収録しています。

## インストール

1. リポジトリをクローンします:
   ```bash
   git clone https://github.com/your-repo/pokemon_diagnosis.git
   cd pokemon_diagnosis
   ```

2. Python の仮想環境を作成し、依存パッケージをインストールします:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   # または
   .venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

3. （任意）ポケモンデータを ID1000 まで自動拡張します:
   ```bash
   .venv/bin/python tools/add_pokemon_1_1000.py
   .venv/bin/python tools/fetch_flavor_text.py      # 説明文を取得
   .venv/bin/python tools/fetch_japanese_names.py   # 日本語名を取得
   .venv/bin/python tools/generate_pokemon_extra.py # 追加データを生成
   .venv/bin/python application/preprocess.py       # ベクトルデータを再生成
   ```

4. アプリケーションを起動します:
   ```bash
   .venv/bin/python interface/app.py
   ```

## 使い方
- ブラウザで `http://localhost:5001` を開きます。
- Web 画面の案内に従って好みを入力すると、診断結果が表示されます。

## 開発環境

1. **初回のみ**: 仮想環境の作成とパッケージのインストール
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   # または
   .venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

2. **2回目以降**: 仮想環境を有効化するだけです
   ```bash
   source .venv/bin/activate  # macOS / Linux
   # または
   .venv\Scripts\activate     # Windows
   ```

3. **アプリケーションの起動**:
   ```bash
   .venv/bin/python interface/app.py
   ```

4. **API の利用**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"types":["fire"], "personality":"おだやか"}' http://localhost:5001/diagnose
   ```

## 仮想環境に関する注意
- 仮想環境のパッケージは `.venv` フォルダに保存され、PC を再起動しても保持されます
- パッケージの再インストールが必要になるのは、仮想環境を削除して作り直した場合や `requirements.txt` を更新した場合のみです
- 新しいターミナルを開くたびに、仮想環境の有効化が必要です

## コントリビュート
コントリビュートを歓迎します。リポジトリをフォークして、プルリクエストを送ってください。

## ライセンス
本プロジェクトは MIT ライセンスで公開されています。詳細は LICENSE ファイルを参照してください。
