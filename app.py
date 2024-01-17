from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    api_url = 'https://pokeapi.co/api/v2/pokemon?limit=365/'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        pokemons = data.get('results', [])
        return render_template('index.html', pokemons = pokemons)
    return 'Erro na solicitação à API'

def get_poke_details(pokemon_url):
    response = requests.get(pokemon_url)

    if response.status_code == 200:
        data = response.json()
        # image_url = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{data.get("id","")}.svg'

        return {
            'type': data.get('types', []),
            'moveset': data.get('moves', []),
            'id': data.get('id', []),
            # 'image_url': image_url,
        }
    return None