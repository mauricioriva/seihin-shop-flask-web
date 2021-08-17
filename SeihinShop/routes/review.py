from SeihinShop.routes.product import create_product
from flask import request, Blueprint

review_bp = Blueprint('reviews_page', __name__, template_folder='templates')

# GET reviews (obtienes la lista de resenas del producto) (Devuelve un html)
# POST reviews (crea una nueva resena sobre un producto)
# HINT: return render_template('your_view.html', your_list=your_list)
@review_bp.route('/products/<product_id>/reviews', methods=['GET', 'POST'])
def reviews(product_id):
    product = get_db().execute(
        'SELECT * FROM review WHERE product_id=?', (product_id)
    ).fetchall()
    return render_template('list_reviews', product=product)

# Crea una resena sobre el producto
def create_review(req, product_id):
    description = req.form['description']
    score = int(req.form['score'])
    get_db().execute('INSERT INTO review (description, score) VALUES (?, ?)', (description, score))
    get_db().commit()
    return redirect(url_for('reviews_page.reviews'))

# Devuelve la lista de resenas del producto (Devuelve HTML)
def list_reviews(req, product_id):
    if request.method == 'GET':
        return render_template('list_reviews.html')
    else:
        return create_product(request)

# Devuelve plantilla HTML para crear nueva resena sobre ese producto
@review_bp.route('/products/<product_id>/reviews/new', methods=['GET'])
def new_review(product_id):
    if request.method == 'GET':
        return render_template('new_review.html')
    else:
        return create_product(request)
