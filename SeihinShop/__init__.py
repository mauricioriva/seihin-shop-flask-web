from flask import Flask

def create_app():
    from . import routes 
    from . import db
    app = Flask(__name__)
    app.config['DATABASE'] = '/tmp/flaskr.db'
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'seihinshop2021@gmail.com'
    app.config['MAIL_PASSWORD'] = 'MefgQCXF7v4nPMY'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    db.init_app(app)
    routes.init_app(app)
    app.secret_key = '1234qwer'
    return app
