from flask_restful import Resource
from flask import request
from flasgger import SwaggerView
from base_app.models import User
from base_app.schemas import UserSchema
from base_app.ext.database import db
from marshmallow import ValidationError
 
class UserResource(Resource, SwaggerView):
    schema = UserSchema()

    def post(self):
        try:
            data = self.schema.load(request.json)
            user = User.query.filter_by(username=data['username']).first()
            if user:
                return {'error': 'username exists'}, 400
            user = User(**data)
            db.session.add(user)
            db.session.commit()
            return {"message": "user created"}, 200
        except ValidationError as err:
            return err.messages, 400
