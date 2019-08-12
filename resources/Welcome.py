from flask_restful import Resource


class WelcomeResource(Resource):
    @staticmethod
    def get():
        return {'message': 'Bem vindo'}, 200

    @staticmethod
    def post():
        return {'message': 'Bem vindo'}, 200
