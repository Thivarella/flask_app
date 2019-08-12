from flask_marshmallow import Schema
from marshmallow import fields


class ClienteSchema(Schema):
    id = fields.Integer()
    nome = fields.String(required=True)
