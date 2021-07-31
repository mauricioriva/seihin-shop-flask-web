from SeihinShop.routes.product import create_product
from flask import request, Blueprint

review_bp = Blueprint('reviews_page', __name__, template_folder='templates')

# GET reviews (obtienes la lista de resenas del producto) (Devuelve un html)
# POST reviews (crea una nueva resena sobre un producto)
# HINT: return render_template('your_view.html', your_list=your_list)
@review_bp.route('/products/<product_id>/reviews', methods=['GET', 'POST'])
def reviews(product_id):
    if request.method == 'GET':
        return list_reviews(request, product_id)
    else:
        return create_review(request, product_id)

# Crea una resena sobre el producto
def create_review(req, product_id):
    pass

# Devuelve la lista de resenas del producto (Devuelve HTML)
def list_reviews(req, product_id):
    pass

# Devuelve plantilla HTML para crear nueva resena sobre ese producto
@review_bp.route('/products/<product_id>/reviews/new', methods=['GET'])
def new_review(product_id):
    pass
