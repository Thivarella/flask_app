from models import db


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
