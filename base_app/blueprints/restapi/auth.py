from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_restful import Resource
from flask import request


class AuthResource(Resource):
    def post(self):
        username = request.json.get("username")
        password = request.json.get("password")

        if username == "usuário" and password == "senha":
            access_token = create_access_token(identity=username)
            return {"access_token": access_token}, 200

        return {"error": "Usuário ou senha inválidos"}, 401
