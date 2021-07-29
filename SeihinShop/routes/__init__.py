# project/routes/__init__.py
# from .account import account_bp
from .product import product_bp

def init_app(app):
    # app.register_blueprint(account_bp)
    app.register_blueprint(product_bp)
