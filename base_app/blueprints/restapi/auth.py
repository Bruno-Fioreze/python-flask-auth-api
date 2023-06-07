from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)
from flask_restful import Resource
from flask import request, jsonify
from datetime import timedelta
from flasgger import SwaggerView


class AuthMeResource(Resource, SwaggerView):
    parameters = [
        {
            "name": "JWT Token",
            "in": "header",
            "type": "string",
            "required": True,
            "example": "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6Ik...",
        }
    ]
    responses = {
        200: {
            "description": "A list of colors (may be filtered by palette)",
        }
    }

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()

        jwt_data = get_jwt()
        data = {"user": current_user}

        data = {**data, **jwt_data}

        return {"data": data}, 200


class AuthSignInResource(Resource, SwaggerView):

    parameters = [
        {
            "name": "Payload",
            "in": "body",
            "schema": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "password": {"type": "string"},
                },
                "required": ["username", "password"],
            },
        }
    ]
    responses = {
        200: {
            "description": "A list of colors (may be filtered by palette)",
        }
    }

    def post(self):

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
