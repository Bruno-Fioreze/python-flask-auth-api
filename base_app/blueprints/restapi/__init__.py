from flask import Blueprint
from flask_restx import Api

from .auth import AuthResource

bp = Blueprint("restapi", __name__)
api = Api(bp)

def init_app(app):
    cls_base = documentation_class(AuthResource)
    api.add_resource(cls_base, "/auth/")
    app.register_blueprint(bp)


def documentation_class(cls):
    @api.route('/auth/')
    class AuthResource(cls):
        ...

    return AuthResource