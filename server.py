
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import requests 
import bcrypt


app = Flask(__name__)

client = MongoClient('localhost', 27017)


db = client.KickStatsDB
todos = db.todos

print(f'Se ha conectado mongo en: {client}')
CORS(app)
# Members API Route

#Register
@app.route('/registerClient' , methods=['POST'])
def register():

    try:
     data = request.json #Get the info of the body
     print(f'datos del cliente -> {email, password}')
     email = data.get('email')
     password = data.get('password')
     

     hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
     password = hashed_password.decode('utf-8')

     #Insercción de datos (registro)
     
     result = db.usuarios.insert_one(email, password)
     print(f'se ha insertado correctamente {email, password}')


     # Convertir ObjectId a cadena
     result['_id'] = str(result.inserted_id)

     return jsonify({'message': 'register ok', 'data': result}) 

    except Exception as e:
      print(f'An exception occurred: {e}')
      return jsonify({'error': 'something went wrong'})


@app.route('/loginClient', methods=['POST'])
def login():
    
    try:
        datos = request.json;    
        email = datos.get('email')
        password = datos.get('password')

        return jsonify({'message': 'login ok', 'email': email, 'password': password}) 

    except Exception as e:
        print(f'An exception occurred:{e}');
        return jsonify({'error':'something went wrong'});
    
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


  


