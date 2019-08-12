from models import db


class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(250), nullable=False)
    preco_unitario = db.Column(db.DECIMAL(18, 2), nullable=False)
    multiplo = db.Column(db.Integer, nullable=True, server_default=db.text('1'))

    def __init__(self, nome, preco_unitario, multiplo):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.multiplo = multiplo
