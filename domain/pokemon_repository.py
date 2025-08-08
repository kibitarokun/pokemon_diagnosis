from abc import ABC, abstractmethod
from .pokemon import Pokemon
from typing import List

# ポケモンリポジトリの抽象基底クラス
class PokemonRepository(ABC):
    @abstractmethod
    def save(self, pokemon: Pokemon) -> None:
        pass

    @abstractmethod
    def save_many(self, pokemons: List[Pokemon]) -> None:
        pass
