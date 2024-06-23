
from flask import Flask, request, jsonify
import requests 

app = Flask(__name__)

# Members API Route

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


@app.route("/members")
def members():
    return {"members": ["Member1", "Member2"]}

@app.route("/cliente")

def cliente():
    return {"members": ["Arturo", "Se come a la prima del Jey"]}

if __name__ == "__main__":
  app.run(debug=True)


  


