from flask import Blueprint
from flask_restful import Api
from resources import ClienteResource, ProdutoResource, PedidoResource
import os
from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp)

    from models.Model import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app = create_app("config")
    app.run(port=port)


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(ClienteResource, '/clientes')
api.add_resource(ProdutoResource, '/produtos')
api.add_resource(PedidoResource, '/pedidos')
