from flask_restful import Resource
from models import Cliente, ClienteSchema

clientes_schema = ClienteSchema(many=True)
cliente_schema = ClienteSchema()


class ClienteResource(Resource):
    @staticmethod
    def get():
        clientes = Cliente.query.all()
        clientes = clientes_schema.dump(clientes).data

        return {'status': 'success', 'data': clientes}, 200
