from flask import Blueprint
from flask_restful import Api

from .auth import AuthResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(AuthResource, "/auth/sigin")
    app.register_blueprint(bp)
