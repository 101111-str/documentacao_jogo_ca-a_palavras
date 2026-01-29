# app.py
from flask import Flask, jsonify, request, render_template
from game import get_dados_nivel, verificar_palavra

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dados", methods=["GET"])
def dados_jogo():
    # Pega o nível da URL (ex: /dados?nivel=2), padrão é 1
    nivel = request.args.get("nivel", default=1, type=int)
    dados = get_dados_nivel(nivel)
    
    return jsonify({
        "palavras": dados["palavras"],
        "grade": dados["grade"],
        "colunas": 20
    })

@app.route("/verificar", methods=["POST"])
def verificar():
    data = request.json
    palavra = data.get("palavra", "")
    nivel = data.get("nivel", 1) # Recebe o nível atual do frontend
    
    return jsonify({
        "valida": verificar_palavra(nivel, palavra)
    })

if __name__ == "__main__":
    app.run(debug=True)