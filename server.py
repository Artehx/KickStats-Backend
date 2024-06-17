
from flask import Flask

app = Flask(__name__)

# Members API Route

@app.route("/members")

def members():
    return {"members": ["Member1", "Member2"]}

@app.route("/cliente")

def cliente():
    print("hola mundo");
    return {"members": ["Arturo", "Se come a la prima del Jey"]}

if __name__ == "__main__":
  app.run(debug=True)


  


