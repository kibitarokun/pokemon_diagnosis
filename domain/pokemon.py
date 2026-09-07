# ポケモンのドメインモデル
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class Pokemon:
    id: int
    name: str
    types: List[str]
    abilities: List[str]
    stats: Dict[str, int]
    nature: Optional[str] = None  # 性格（オプション）
