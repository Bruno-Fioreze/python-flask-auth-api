from marshmallow import Schema, fields

# from .models import User


class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    # class Meta:
    #     model = User
