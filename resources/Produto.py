from flask_restful import Resource
from models import Produto, ProdutoSchema

produtos_schema = ProdutoSchema(many=True)
produto_schema = ProdutoSchema()


class ProdutoResource(Resource):
    @staticmethod
    def get():
        produtos = Produto.query.all()
        produtos = produtos_schema.dump(produtos).data
        return {"status": "success", "data": produtos}, 200
