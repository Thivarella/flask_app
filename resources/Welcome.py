from flask_restful import Resource


class WelcomeResource(Resource):
    @staticmethod
    def get():
        return {'Bem vindo'}, 200

    @staticmethod
    def post():
        return {'Bem vindo'}, 200
