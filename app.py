from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    api_url = 'https://pokeapi.co/api/v2/pokemon?limit=10'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        pokemons = data.get('results', [])

        for pokemon in pokemons:
            details = get_poke_details(pokemon['url'])
            if details:
                pokemon.update(details)


        return render_template('index.html', pokemons = pokemons)
    return 'Erro na solicitação à API'

def get_poke_details(pokemon_url):
    detail_response = requests.get(pokemon_url)

    if detail_response.status_code == 200:
        detail_data = detail_response.json()

        return {
            'type': detail_data.get('types', []),
            'moveset': detail_data.get('moves', []),
            'id': detail_data.get('id', 0),
        }
    return None