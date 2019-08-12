from models import db


class Pedido(db.Model):
    __tablename__ = 'pedidos'
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id', ondelete='CASCADE'), nullable=False)
    cliente = db.relationship('Cliente', backref=db.backref('clientes', lazy='dynamic'))
    itens_pedido = db.relationship('ItensPedido', lazy='select', backref=db.backref('itens_pedidos', lazy='joined'))

    def __init__(self, cliente_id):
        self.cliente_id = cliente_id
