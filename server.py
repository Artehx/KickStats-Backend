
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests 

app = Flask(__name__)
CORS(app)
# Members API Route

#Players
@app.route("/buscarJugador", methods=['GET'])
def buscar_jugador():
    try:
        player_name = request.args.get('player_name')
        if not player_name:
            return jsonify({'error': 'Player name parameter is required'}), 400

        api_url = f'https://transfermarkt-api.fly.dev/players/search/{player_name}'
        response = requests.get(api_url)

        if response.status_code == 200:
            results = response.json()
        else:
            results = {'error': 'Unable to fetch data from API'}

        return jsonify(results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/buscarJugadorProfile", methods=['GET'])
def busca_profile_jugador():
    try:
        id_player = request.args.get('id_player')
        if not id_player:
            return jsonify({'error': 'id player parameter is required'}), 400

        api_url = f'https://transfermarkt-api.fly.dev/players/{id_player}/profile'
        response = requests.get(api_url)

        if response.status_code == 200:
            results = response.json()
        else:
            results = {'error': 'Unable to fetch data from API'}

        return jsonify(results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

#Clubs
@app.route("/getClubs", methods=['GET'])
def getClubs():
    try:
        name_club = request.args.get('name_club')
        if not name_club:
            return jsonify({'error': 'name club is required'}), 400

        api_url = f'https://transfermarkt-api.fly.dev/clubs/search/{name_club}'
        response = requests.get(api_url)

        if response.status_code == 200:
            results = response.json()
        else:
            results = {'error': 'Unable to fetch data from API'}

        return jsonify(results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
        
if __name__ == "__main__":
  app.run(debug=True)


  


