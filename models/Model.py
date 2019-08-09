from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


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


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)

    def __init__(self, nome):
        self.nome = nome


class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id', ondelete='CASCADE'), nullable=False)
    cliente = db.relationship('Cliente', backref=db.backref('clientes', lazy='dynamic'))
    itens_pedido = db.relationship('ItensPedido', lazy='select', backref=db.backref('itens_pedidos', lazy='joined'))

    def __init__(self, cliente_id):
        self.cliente_id = cliente_id


class ItensPedido(db.Model):
    __tablename__ = 'itens_pedido'
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id', ondelete='CASCADE'), nullable=False)
    produto = db.relationship('Produto', backref=db.backref('produtos', lazy='dynamic'))
    preco_unitario = db.Column(db.DECIMAL(18, 2), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    rentabilidade = db.Column(db.String, nullable=False)
    pedidos_id = db.Column(db.Integer, db.ForeignKey('pedidos.id', ondelete='CASCADE'), nullable=False)
    pedido = db.relationship('Pedido', backref=db.backref('pedidos', lazy='dynamic'))

    def __init__(self, produto_id, preco_unitario, quantidade, rentabilidade, pedidos_id):
        self.produto_id = produto_id
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.rentabilidade = rentabilidade
        self.pedidos_id = pedidos_id


class ClienteSchema(ma.Schema):
    id = fields.Integer()
    nome = fields.String(required=True)


class ProdutoSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nome = fields.String(required=True)
    preco_unitario = fields.Float(required=True, digits=2)
    multiplo = fields.Integer(required=False, default=1)


class ItensPedidoSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    produto = fields.Nested(ProdutoSchema)
    preco_unitario = fields.Float(required=True, digits=2)
    quantidade = fields.Integer(required=True)
    rentabilidade = fields.String(required=True)
    pedido_id = fields.Integer(required=False)


class PedidoSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    creation_date = fields.DateTime()
    cliente = fields.Nested(ClienteSchema)
    itens_pedido = fields.Nested(ItensPedidoSchema, many=True)
