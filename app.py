from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    api_url = 'https://pokeapi.co/api/v2/pokemon'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        pokemons = data.get('results', [])

        return render_template('index.html', pokemons = pokemons)
    return 'Erro na solicitação à API'
