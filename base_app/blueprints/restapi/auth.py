from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)
from flask_restx import Resource
from flask import request, jsonify
from datetime import timedelta

class AuthResource(Resource):
    @jwt_required()
    def get(self):
        """
        Descrição da operação GET do endpoint /auth/
        """
        current_user = get_jwt_identity()

        jwt_data = get_jwt()
        data = {"user": current_user}

        data = {**data, **jwt_data}

        return {"data": data}, 200

    def post(self):
        """
        Descrição da operação POST do endpoint /auth/
        """
        username = request.json.get("username")
        password = request.json.get("password")

        if username == "usuário" and password == "senha":
            additional_data = {"user_id": 1, "custom_data": "some_data"}
            access_token = create_access_token(
                identity=username,
                expires_delta=timedelta(hours=1),
                additional_claims=additional_data,
            )
            print(access_token)
            return {"access_token": access_token}, 200

        return {"error": "Usuário ou senha inválidos"}, 401
