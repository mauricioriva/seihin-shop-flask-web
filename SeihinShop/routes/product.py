from flask import request, Blueprint, g, session, redirect, url_for
from flask.templating import render_template
from ..db import get_db

product_bp = Blueprint('products_page', __name__, template_folder='./../templates/product')

# GET Products (obtienes la lista de productos registrados (buscador))
# Devuelve lista de productos (Devuelve un html)
# HINT: return render_template('your_view.html', your_list=your_list)
@product_bp.route('/products', methods=['GET'])
def products():
    products = get_db().execute(
        'SELECT * FROM product LEFT JOIN user ON product.user_id = user.id WHERE product.on_sale = 1').fetchall()
    if (len(products) > 0):
        return render_template('list-products.html', products=products)
    return render_template('list-products.html')

# GET Product Id, devuelve los datos de ese producto
# PUT Product Id, actualiza los datos de ese producto
@product_bp.route('/products/<product_id>', methods=['GET', 'POST'])
def existing_product(product_id):
    if request.method == 'GET':
        return get_product(product_id)
    else:
        return update_product(request, product_id)

# Obtiene la informacion de un producto (Devuelve un html)
# HINT: return render_template('your_view.html', your_list=your_list)
def get_product(id):
    product = get_db().execute(
        'SELECT * FROM product WHERE id=?', (id)
    ).fetchone()
    return render_template('product.html', product=product)

# Actualiza la informacion de un producto
def update_product(req, id):
    name = req.form['name']
    description = req.form['description']
    price = int(req.form['price'])
    on_sale = int(req.form['on_sale'])
    get_db().execute('UPDATE product SET name=?, description=?, price=?, on_sale=? WHERE id=?', (name, description, price, on_sale, id))
    get_db().commit()
    return redirect(url_for('products_page.existing_product', product_id=id))

# Devuelve la plantilla HTML para guardar un nuevo producto
# HINT: return render_template('your_view.html', your_list=your_list)
@product_bp.route('/products/new', methods=['GET', 'POST'])
def new_product_template():
    if request.method == 'GET':
        return render_template('new-product.html')
    else:
        return create_product(request)

# Un usuario registra un producto
def create_product(req):
    name = req.form['name']
    description = req.form['description']
    price = int(req.form['price'])
    get_db().execute('INSERT INTO product (name, description, price, on_sale, user_id) VALUES (?, ?, ?, ?, ?)', (name, description, price, 0, session.get('user_id')))
    get_db().commit()
    return redirect(url_for('products_page.products'))

# GET obtiene los productos que vende el usuario (Devuelve html)
# POST crea un nuevo producto por el usuario 
@product_bp.route('/products/my_products', methods=['GET'])
def my_products():
    products = get_db().execute('SELECT * FROM product WHERE product.user_id = ?', (session.get('user_id'),)).fetchall()
    if (len(products) > 0):
        return render_template('list-user-products.html', products=products)
    return render_template('list-user-products.html')

@product_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    #print(user_id)
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()
