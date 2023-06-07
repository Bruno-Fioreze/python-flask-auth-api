from flask import Blueprint
from flask_restful import Api
from .auth import AuthMeResource, AuthSignInResource

bp = Blueprint("restapi", __name__)
api = Api(bp)


def init_app(app):
    api.add_resource(AuthMeResource, "/auth/")
    api.add_resource(AuthSignInResource, "/auth/")
    app.register_blueprint(bp)
