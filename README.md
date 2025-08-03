# Pokémon Diagnosis Application

## Overview
The Pokémon Diagnosis Application is a tool designed to help users identify Pokémon based on their characteristics and preferences. It leverages machine learning techniques, including K-Nearest Neighbors (KNN), to provide accurate predictions. The application also integrates with external Pokémon APIs to enhance its dataset and provide a seamless user experience.

## Project Structure

```
application/
    data_collector.py       # Collects and processes Pokémon data
    knn_model.py            # Implements the KNN model for predictions
    preprocess.py           # Preprocessing utilities for data
    user_input_vectorizer.py # Converts user input into vector format

data/
    pokemon_dataset.json    # Core dataset of Pokémon
    pokemon_extra.json      # Additional Pokémon data
    pokemon_vectors.npy     # Preprocessed Pokémon vectors

domain/
    pokemon.py              # Pokémon domain model
    user_profile.py         # User profile domain model

infrastructure/
    pokeapi_client.py       # Client for interacting with the Pokémon API

interface/
    api_test.py             # Tests for the API
    api.py                  # API implementation
    app.py                  # Main application entry point
    static/                 # Static files (e.g., JSON, images)
    templates/              # HTML templates for the web interface
```

## Features
- **Pokémon Identification**: Predicts Pokémon based on user input.
- **Machine Learning**: Uses KNN for accurate predictions.
- **API Integration**: Fetches additional data from external Pokémon APIs.
- **Web Interface**: User-friendly web interface for interaction.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/pokemon_diagnosis.git
   cd pokemon_diagnosis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python interface/app.py
   ```

## Usage
- Open your browser and navigate to `http://localhost:5000`.
- Follow the instructions on the web interface to input your preferences and get Pokémon predictions.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
