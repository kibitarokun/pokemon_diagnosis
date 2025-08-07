import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from infrastructure.pokeapi_client import PokeApiClient
from domain.pokemon import Pokemon
from domain.pokemon_repository import PokemonRepository
from typing import List
import json
import requests

def pokemon_from_api_data(poke_data, species_data):
    # 日本語フレーバーテキスト取得
    flavor_text = ""
    for entry in species_data.get("flavor_text_entries", []):
        if entry["language"]["name"] == "ja-Hrkt":
            flavor_text = entry["flavor_text"].replace('\n', '').replace('\u3000', '')
            break
    return Pokemon(
        id=poke_data["id"],
        name=poke_data["name"],
        types=[t["type"]["name"] for t in poke_data["types"]],
        abilities=[a["ability"]["name"] for a in poke_data["abilities"]],
        stats={s["stat"]["name"]: s["base_stat"] for s in poke_data["stats"]},
        nature=None
    )

class AddPokemonUsecase:
    def __init__(self, repository: PokemonRepository):
        self.repository = repository
        self.api_client = PokeApiClient()

    def add_pokemon_by_id(self, pokemon_id: int):
        poke_data = self.api_client.get_pokemon(pokemon_id)
        species_data = self.api_client.get_pokemon_species(pokemon_id)
        pokemon = pokemon_from_api_data(poke_data, species_data)
        self.repository.save(pokemon)

    def add_pokemon_by_id_range(self, start_id: int, end_id: int):
        pokemons: List[Pokemon] = []
        for pid in range(start_id, end_id + 1):
            poke_data = self.api_client.get_pokemon(pid)
            species_data = self.api_client.get_pokemon_species(pid)
            pokemon = pokemon_from_api_data(poke_data, species_data)
            pokemons.append(pokemon)
        self.repository.save_many(pokemons)

with open("data/pokemon_dataset.json", encoding="utf-8") as f:
    pokemons = json.load(f)

for p in pokemons:
    if "image_url" not in p or not p["image_url"]:
        poke_id = p["id"]
        url = f"https://pokeapi.co/api/v2/pokemon/{poke_id}/"
        res = requests.get(url)
        if res.status_code == 200:
            poke = res.json()
            p["image_url"] = poke["sprites"]["other"]["official-artwork"]["front_default"]
        else:
            p["image_url"] = ""

with open("data/pokemon_dataset.json", "w", encoding="utf-8") as f:
    json.dump(pokemons, f, ensure_ascii=False, indent=2)