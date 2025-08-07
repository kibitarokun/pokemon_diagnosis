import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from application.add_pokemon_usecase import AddPokemonUsecase
from infrastructure.pokemon_json_repository import PokemonJsonRepository

def main():
    repo = PokemonJsonRepository("data/pokemon_dataset.json")
    usecase = AddPokemonUsecase(repo)
    usecase.add_pokemon_by_id_range(1, 1000)

if __name__ == "__main__":
    main()
