from flask import Flask, jsonify, request
from lista_pessoas import pessoas

app = Flask(__name__)


# Homepage
@app.route('/')
def homepage():
    return 'API está no ar!'


# Lista todas as pessoas
@app.route('/pessoas', methods=['GET'])
def pessoa():
    return jsonify(pessoas)


# Lista pessoa por id
@app.route('/pessoas/<int:Id>', methods=['GET'])
def busca_id(Id):
    for pessoa in pessoas:
        if pessoa.get('Id') == Id:
            return jsonify(pessoa)


# Edita pessoa por Id
@app.route('/pessoas/<int:Id>', methods=['PUT'])
def edita_nome_por_id(Id):
    edita_nome = request.get_json()
    for indice, pessoa in enumerate(pessoas):
        if pessoa.get('Id') == Id:
            pessoas[indice].update(edita_nome)
            return jsonify(pessoas[indice])


# Cadastrar pessoas
@app.route('/pessoas', methods=['POST'])
def criar_pessoas():
    nova_pessoa = request.get_json()
    pessoas.append(nova_pessoa)
    return pessoas


# Deletar pessoas por Id
@app.route('/pessoas/<int:Id>', methods=['DELETE'])
def deletar_pessoa(Id):
    for indice, pessoa in enumerate(pessoas):
        if pessoa.get('Id') == Id:
            del pessoas[indice]
    return pessoas


# Realizando teste antes de ir para PDR
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)

# Host principal: https://cryptic-bayou-73647-9b0666acf33b.herokuapp.com/
