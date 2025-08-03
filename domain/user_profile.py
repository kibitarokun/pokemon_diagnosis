
# ユーザープロファイルのドメインモデル
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class UserProfile:
    types: List[str] = None           # 自分を表すタイプ（例: ['fire', 'flying']）
    abilities: List[str] = None       # 自分の特徴・特性（例: ['blaze']）
    important_stats: List[str] = None # 自分が重視する能力（例: ['speed', 'attack']）
    personality: Optional[str] = None # 性格
    activities: List[str] = None      # 好きな活動・趣味
    dislikes: List[str] = None        # 苦手なこと
    memo: Optional[str] = None        # その他メモ
