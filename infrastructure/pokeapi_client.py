# PokéAPIクライアント
import requests
from typing import Dict, Any

class PokeApiClient:
    BASE_URL = "https://pokeapi.co/api/v2/"

    def get_pokemon(self, pokemon_id: int) -> Dict[str, Any]:
        url = f"{self.BASE_URL}pokemon/{pokemon_id}/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_pokemon_species(self, pokemon_id: int) -> Dict[str, Any]:
        url = f"{self.BASE_URL}pokemon-species/{pokemon_id}/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
