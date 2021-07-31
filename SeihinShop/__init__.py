from flask import Flask

def create_app():
    from . import routes #, models
    app = Flask(__name__)
    # models.init_app(app)
    routes.init_app(app)
    app.secret_key = '1234ed'
    return app
