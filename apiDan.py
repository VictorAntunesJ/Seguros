from flask import Flask, jsonify, request
import requests

api_url = (
    "https://api.sheety.co/20e6e67423392ddd3f7dc9eaf5caed47/servicos360Seguros/servicos"
)

zapier_url = (
    "https://hooks.zapier.com/hooks/catch/11165692/3hdyjo8/"
)

api_cotacao_url = (
    "https://economia.awedddsomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
)

ultima_cotacao = {}

app = Flask(__name__)


def junta_texto(texto1, texto2, texto3):
    return f"{texto1} {texto2} {texto3}"


@app.route("/")
def inicial():
    response = requests.get(api_url)

    return jsonify(response.json())

@app.route("/meu-texto")
def meu_texto():
    turma = request.args.get("turma")
    periodo = request.args.get("periodo")
    meu_texto = request.args.get("meu_texto")

    return jsonify({
        "texto": meu_texto,
        "turma": turma, 
        "periodo": periodo
    })

@app.route("/juntar")
def juntar():
    texto1 = request.args.get("texto1")
    texto2 = request.args.get("texto2")
    texto3 = request.args.get("texto3")

    return junta_texto(texto1, texto2, texto3)


@app.route("/salvar-dados", methods=["POST"])
def salvar_dados():
    dados = request.get_json()

    texto = dados["texto"]
    email = dados["email"]
    HTTP_CREATED = 201

    requests.post(zapier_url, json=dados)

    return jsonify({
        "mensagem": "Cadastro realizado com sucesso!", 
        "dados": {
            "texto": texto,
            "email": email
        }
    }), HTTP_CREATED

@app.route("/", methods=["PUT"])
def enviar():
    dados = request.get_json()

    print(dados["nome"])
    print(dados["email"])

    return jsonify({"mensagem": "Cadastro realizado com sucesso!"}), 201


@app.route("/minha-aula")
def minha_aula():
    return "", 500

@app.route("/minha-aula2")
def minha_aula2():
    return "", 500

@app.route("/cotacao")
def cotacao():
    # cotacao é atualizada a cada 30 segundos
    global ultima_cotacao

    try:
        response = requests.get(api_cotacao_url)
        ultima_cotacao = response.json()
    except:
        if not ultima_cotacao:
            ultima_cotacao = {
                "USDBRL": {
                    "bid": "5.00"
                },
                "EURBRL": {
                    "bid": "6.00"
                },
                "BTCBRL": {
                    "bid": "100000.00"
                }
            }

    return jsonify(ultima_cotacao)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=80)