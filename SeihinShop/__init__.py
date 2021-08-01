from flask import Flask

def create_app():
    from . import routes 
    from . import db
    app = Flask(__name__)
    app.config['DATABASE'] = '/tmp/flaskr.db'
    db.init_app(app)
    routes.init_app(app)
    app.secret_key = '1234qwer'
    return app
