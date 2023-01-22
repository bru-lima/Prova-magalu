from pymongo import MongoClient

def obter_colecao_mongodb(url_conexao: str, colecao: str):
    client = MongoClient(url_conexao)
    db = client.get_default_database()
    return db[colecao]

