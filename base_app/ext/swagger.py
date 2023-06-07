from flasgger import Swagger


def init_app(app):
    swagger = Swagger(app)
    # swag = swagger(app)
    # swag['info']['version'] = "1.0"
    # swag['info']['title'] = "API Base"
