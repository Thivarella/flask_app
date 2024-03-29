from flask import Blueprint
from flask_restful import Api
from resources import ClienteResource, ProdutoResource, PedidoResource, WelcomeResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(WelcomeResource, '/')
api.add_resource(ClienteResource, '/clientes')
api.add_resource(ProdutoResource, '/produtos')
api.add_resource(PedidoResource, '/pedidos')
