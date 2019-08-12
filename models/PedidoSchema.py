from marshmallow import fields
from flask_marshmallow import Schema
from models import ClienteSchema, ItensPedidoSchema


class PedidoSchema(Schema):
    id = fields.Integer(dump_only=True)
    creation_date = fields.DateTime()
    cliente = fields.Nested(ClienteSchema)
    itens_pedido = fields.Nested(ItensPedidoSchema, many=True)
