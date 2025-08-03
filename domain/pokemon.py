# ポケモンのドメインモデル
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Pokemon:
    id: int
    name: str
    types: List[str]
    abilities: List[str]
    stats: Dict[str, int]
    nature: str = None  # 性格（オプション）
