from flask import request, Blueprint, render_template
from flask.helpers import url_for
from werkzeug.utils import redirect
from ..db import get_db
import datetime
purchase_bp = Blueprint('purchase_page', __name__, template_folder='templates')

# GET products purchased by user (obtienes la lista de productos comprados) (Devuelve un html)
# HINT: return render_template('your_view.html', your_list=your_list)
@purchase_bp.route('/users/<user_id>/purchases', methods=['GET'])
def purchases(user_id):
    purchases = get_db().execute(
        f'SELECT p.name, p.price, pur.id, pur.date FROM product p LEFT JOIN purchase AS pur ON pur.product_id = p.id WHERE pur.user_id = {user_id}').fetchall()
    return render_template('purchase/list-purchases.html', purchases=purchases)

# POST purchase, un usuario compra un producto
@purchase_bp.route('/products/<product_id>/users/<user_id>/purchase', methods=['POST'])
def user_purchase_product(product_id,user_id):
    get_db().execute(f'INSERT INTO purchase (user_id, product_id, date) VALUES ({user_id}, {product_id}, {datetime.datetime.date()})')
    get_db().commit()
    return redirect(url_for('/users/<user_id>/purchases'))
