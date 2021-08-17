from .auth import auth_bp, getMail
from .product import product_bp
from .purchase import purchase_bp
from .review import review_bp
from .user import user_bp

def init_app(app):
    getMail(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(purchase_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(user_bp)
