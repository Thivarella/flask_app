from marshmallow import fields
from flask_marshmallow import Schema
from models import ProdutoSchema


class ItensPedidoSchema(Schema):
    id = fields.Integer(dump_only=True)
    produto = fields.Nested(ProdutoSchema)
    preco_unitario = fields.Float(required=True, digits=2)
    quantidade = fields.Integer(required=True)
    rentabilidade = fields.String(required=True)
    pedido_id = fields.Integer(required=False)
