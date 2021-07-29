from flask import request, Blueprint

product_bp = Blueprint('simple_page', __name__, template_folder='templates')


@product_bp.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        return create_product(request)
    else:
        return list_products(request)

def create_product(req):
    return "<p>Hello, POST product!</p>"

def list_products(req):
    return "<p>Hello, GET product!</p>"
