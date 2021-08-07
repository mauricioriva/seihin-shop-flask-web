from flask import request, Blueprint

purchase_bp = Blueprint('purchase_page', __name__, template_folder='templates')

# GET products purchased by user (obtienes la lista de productos comprados) (Devuelve un html)
# HINT: return render_template('your_view.html', your_list=your_list)
@purchase_bp.route('/purchases', methods=['GET'])
def purchases():
    #GET USER ID FROM SESSION
    pass

# POST purchase, un usuario compra un producto
@purchase_bp.route('/products/<product_id>/users/<user_id>/purchase', methods=['POST'])
def user_purchase_product(product_id,user_id):
    pass
