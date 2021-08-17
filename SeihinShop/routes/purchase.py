from flask import request, Blueprint, render_template, session
from flask.helpers import url_for
from werkzeug.utils import redirect
from ..db import get_db
from datetime import date
purchase_bp = Blueprint('purchase_page', __name__, template_folder='./../templates/purchase')

# GET products purchased by user (obtienes la lista de productos comprados) (Devuelve un html)
# HINT: return render_template('your_view.html', your_list=your_list)
@purchase_bp.route('/users/purchases', methods=['GET'])
def purchases():
    user_id = session.get('user_id')
    name = get_db().execute(f'SELECT name FROM user WHERE user.id = {user_id}').fetchall()
    purchases = get_db().execute(
        f'SELECT p.name, p.price, pur.id, pur.date FROM product p LEFT JOIN purchase AS pur ON pur.product_id = p.id WHERE pur.user_id = {user_id}').fetchall()
    return render_template('purchase/list-purchases.html', purchases=purchases, name=name)
    
# POST purchase, un usuario compra un producto
@purchase_bp.route('/products/<product_id>/users/purchase', methods=['POST', 'GET'])
def user_purchase_product(product_id):
    user_id = session.get('user_id')
    error = None
    if request.method == 'POST':
        payment_selected = request.form['payment']
        address_selected = request.form['address']

        get_db().execute(f'INSERT INTO purchase (user_id, product_id, date, address, payment) VALUES (?, ?, ?, ?, ?)', (user_id, product_id, date.today(), address_selected, payment_selected))
        get_db().commit()

        get_db().execute(f'UPDATE product SET on_sale = on_sale - 1 WHERE id = {product_id}')
        get_db().commit()

        return redirect(url_for(f'purchase_page.purchases', user_id=user_id ))
    else:
        return render_template('purchase.html', error=error)