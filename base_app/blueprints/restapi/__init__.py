from flask import Blueprint
from flask_restful import Api
from .auth import AuthMeResource, AuthSignInResource
from .user import UserResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(AuthMeResource, "/auth/")
    api.add_resource(AuthSignInResource, "/auth/")
    api.add_resource(UserResource, "/user/")
    app.register_blueprint(bp)
