from flask import Flask, request


app = Flask(__name__)

entrada= {'entrada': 0}

@app.route('/contador', methods=['POST']) 
def novo_entrada():
    dado= request.json
    entrada['entrada'] = dado['entrada']
    return {'entrada': entrada['entrada']}, 201

@app.route('/contador', methods=['GET']) 
def leitura_entrada():
    return {'entrada': entrada['entrada']}, 200


@app.route('/contador/incrementa', methods=['PUT']) 
def incrementa_entrada():
    entrada['entrada'] += 1
    return {'entrada': entrada['entrada']}, 202


@app.route('/contador', methods=['DELETE']) 
def deleta_entrada():
    entrada['entrada'] = 0
    return {'entrada': entrada['entrada']}, 202

if __name__ == '__main__':
    app.run(debug=True)










