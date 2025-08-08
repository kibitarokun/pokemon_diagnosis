import json
from domain.pokemon import Pokemon
from domain.pokemon_repository import PokemonRepository
from typing import List

class PokemonJsonRepository(PokemonRepository):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save(self, pokemon: Pokemon) -> None:
        self.save_many([pokemon])

    def save_many(self, pokemons: List[Pokemon]) -> None:
        try:
            with open(self.filepath, encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        # 既存IDを除外し新しいものを追加
        existing_ids = {p.get("id") for p in data}
        for poke in pokemons:
            data = [p for p in data if p.get("id") != poke.id]
            data.append({
                "id": poke.id,
                "name": poke.name,
                "types": poke.types,
                "abilities": poke.abilities,
                "stats": poke.stats,
            })
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
