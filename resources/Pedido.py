from flask import request
from flask_restful import Resource
from models import db, Pedido, PedidoSchema, ItensPedido, ItensPedidoSchema, \
    Cliente, ClienteSchema, Produto, ProdutoSchema

pedidos_schema = PedidoSchema(many=True)
pedido_schema = PedidoSchema()
itens_pedido_schema = ItensPedidoSchema(many=True)
item_pedido_schema = ItensPedidoSchema()
cliente_schema = ClienteSchema()
produto_schema = ProdutoSchema()


def get_rentabilidade(original, current):
    if original > current:
        return "ruim"
    elif current > original:
        return "ótima"
    else:
        return "boa"


def validate_multiplo(multiplo, quantidade):
    return (quantidade % multiplo) == 0


class PedidoResource(Resource):
    @staticmethod
    def get():
        pedidos = Pedido.query.all()
        pedidos = pedidos_schema.dump(pedidos).data

        return {'status': 'success', 'data': pedidos}, 200

    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        json_data['cliente'] = cliente_schema.dump(
            Cliente.query.get(json_data['cliente']['id'])).data
        for item in json_data['itens_pedido']:
            produto = produto_schema.dump(Produto.query.get(item['id'])).data
            if not validate_multiplo(produto['multiplo'], item['quantidade']):
                return {'status': 'erro na quantidade',
                        'message': 'O item \'{}\' precisa ser solicitado em '
                                   'múltiplos de {}'.format(produto['nome'], produto['multiplo'])}
            item['produto'] = produto
            item['rentabilidade'] = get_rentabilidade(produto['preco_unitario'], item['preco_unitario'])
        data, errors = pedido_schema.load(json_data)
        if errors:
            return errors, 422
        pedido = Pedido(cliente_id=data['cliente']['id'])
        db.session.add(pedido)
        db.session.commit()

        for received_item in json_data['itens_pedido']:
            item = ItensPedido(received_item['produto']['id'], received_item['preco_unitario'],
                               received_item['quantidade'], received_item['rentabilidade'], pedido.id)
            db.session.add(item)
            db.session.commit()
            pedido.itens_pedido.append(item)

        result = pedido_schema.dump(pedido).data

        return {"status": 'success', 'data': result}, 201
