# Pokémon Diagnosis Application

## Overview
The Pokémon Diagnosis Application is a DDD-structured tool that helps users identify Pokémon based on their characteristics and preferences. It leverages machine learning (K-Nearest Neighbors, KNN) and integrates with external Pokémon APIs to provide a seamless and extensible user experience. The project is organized by domain, application, infrastructure, and interface layers for maintainability and scalability.

## Note
The display is primarily in Japanese with radar chart visualization to show matching characteristics between users and Pokémon. The application includes Japanese Pokémon names and descriptions for an authentic experience.

## Project Structure

```
application/
    data_collector.py         # Collects and processes Pokémon data
    knn_model.py              # Implements the KNN model for predictions
    preprocess.py             # Preprocessing utilities for data
    user_input_vectorizer.py  # Converts user input into vector format
    add_pokemon_usecase.py    # Use case for adding Pokémon data from API

data/
    pokemon_dataset.json      # Core dataset of Pokémon (ID1-1000 supported)
    pokemon_extra.json        # Additional Pokémon data (personality, likes, etc.)
    pokemon_vectors.npy       # Preprocessed Pokémon vectors

domain/
    pokemon.py                # Pokémon domain model (entity)
    pokemon_repository.py     # Pokémon repository interface (abstract)
    user_profile.py           # User profile domain model

infrastructure/
    pokeapi_client.py         # Client for interacting with the Pokémon API
    pokemon_json_repository.py# JSON repository implementation for Pokémon

interface/
    api_test.py               # Tests for the API
    api.py                    # API implementation
    app.py                    # Main application entry point (Flask)
    static/                   # Static files (e.g., JSON, images)
    templates/                # HTML templates for the web interface

tools/
    add_pokemon_1_1000.py     # Script to auto-add Pokémon ID1-1000 from API
    fetch_flavor_text.py      # Script to fetch Pokémon descriptions
    fetch_japanese_names.py   # Script to fetch Japanese Pokémon names
    generate_pokemon_extra.py # Script to generate additional Pokémon data
```

## Features
- **Pokémon Identification**: Predicts Pokémon based on user input.
- **Machine Learning**: Uses KNN for accurate predictions.
- **API Integration**: Fetches and extends data from external Pokémon APIs (pokeAPI).
- **DDD Structure**: Domain-driven design for clear separation of concerns.
- **Data Auto-Expansion**: Easily expand dataset up to ID1000 with provided scripts.
- **Web Interface**: User-friendly web interface for interaction.
- **Radar Chart Visualization**: Visual representation of matching characteristics.
- **Japanese Localization**: Includes Japanese Pokémon names and descriptions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/pokemon_diagnosis.git
   cd pokemon_diagnosis
   ```

2. Set up a Python virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

3. (Optional) Auto-expand Pokémon data to ID1000:
   ```bash
   .venv/bin/python tools/add_pokemon_1_1000.py
   .venv/bin/python tools/fetch_flavor_text.py      # Fetch Pokémon descriptions
   .venv/bin/python tools/fetch_japanese_names.py   # Fetch Japanese names
   .venv/bin/python tools/generate_pokemon_extra.py # Generate extra data
   .venv/bin/python application/preprocess.py       # Regenerate vector data
   ```

4. Run the application:
   ```bash
   .venv/bin/python interface/app.py
   ```

## Usage
- Open your browser and navigate to `http://localhost:5001`.
- Follow the instructions on the web interface to input your preferences and get Pokémon predictions.

## Development Environment

1. **First time only**: Create virtual environment and install packages
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

2. **Subsequent use**: Only activate the virtual environment
   ```bash
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate     # Windows
   ```

3. **Start the application**:
   ```bash
   .venv/bin/python interface/app.py
   ```

4. **Using the API**:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"types":["fire"], "personality":"おだやか"}' http://localhost:5001/diagnose
   ```

## Virtual Environment Notes
- Packages in the virtual environment are stored in the `.venv` folder and persisted between computer restarts
- Reinstalling packages is only necessary if you delete and recreate the virtual environment or update `requirements.txt`
- Activating the virtual environment is required each time you open a new terminal session

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
