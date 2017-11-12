import uuid
from flask import session
from src.common.database import Database


class Produto2(object):
    def __init__(self, nome, preco, descricao, _id=None):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection="produtos", data=self.json())

    def json(self):
        return {
            "_id": self._id,
            "nome": self.nome,
            "preco": self.preco,
            "descricao": self.descricao
        }
