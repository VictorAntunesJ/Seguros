from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route("/")
def inicial():
    response = requests.get(
        "https://api.sheety.co/20e6e67423392ddd3f7dc9eaf5caed47/servicos360Seguros/servicos")
    return jsonify(response.json())


@app.route("/", methods=["POST"])
def enviar():
    dados = request.get_json()

    print(dados['nome'])
    print(dados['email'])

    return jsonify({"mensagem": "Cadastro realizado com sucesso!"}), 200


@app.route("/minha-aula")
def minha_aula():
    return "", 404


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=80)
