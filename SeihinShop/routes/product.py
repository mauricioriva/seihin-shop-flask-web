from flask import request, Blueprint

product_bp = Blueprint('products_page', __name__, template_folder='templates')

# GET Products (obtienes la lista de productos registrados (buscador))
# Devuelve lista de productos (Devuelve un html)
# HINT: return render_template('your_view.html', your_list=your_list)
@product_bp.route('/products', methods=['GET'])
def products():
    pass

# GET Product Id, devuelve los datos de ese producto
# PUT Product Id, actualiza los datos de ese producto
@product_bp.route('/products/<product_id>', methods=['GET', 'PUT'])
def existingProduct(product_id):
    if request.method == 'GET':
        return get_product(request, product_id)
    else:
        return update_product(request, product_id)

# Obtiene la informacion de un producto (Devuelve un html)
# HINT: return render_template('your_view.html', your_list=your_list)
def get_product(req, id):
    pass

# Actualiza la informacion de un producto
def update_product(req, id):
    pass

# Devuelve la plantilla HTML para guardar un nuevo producto
# HINT: return render_template('your_view.html', your_list=your_list)
@product_bp.route('/products/new', methods=['GET'])
def new_product_template():
    pass

# GET obtiene los productos que vende el usuario (Devuelve html)
# POST crea un nuevo producto por el usuario 
@product_bp.route('/products/users/<user_id>', methods=['GET', 'POST'])
def sell(user_id):
    if request.method == 'GET':
        return list_sell_products(request, user_id)
    else:
        return create_product(request, user_id)

# Devuelve una lista con los productos que vende el usuario (HTML)
def list_sell_products(req, user_id):
    pass

# Un usuario registra un producto
def create_product(req, user_id):
    pass
