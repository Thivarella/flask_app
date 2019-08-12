from marshmallow import fields
from flask_marshmallow import Schema


class ProdutoSchema(Schema):
    id = fields.Integer(dump_only=True)
    nome = fields.String(required=True)
    preco_unitario = fields.Float(required=True, digits=2)
    multiplo = fields.Integer(required=False, default=1)
