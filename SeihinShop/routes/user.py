from flask import request, Blueprint

user_bp = Blueprint('users_page', __name__, template_folder='templates')

# GET users (obtienes la lista de usuarios registrados) (Devuelve un html)
# HINT: return render_template('your_view.html', your_list=your_list)
@user_bp.route('/users', methods=['GET'])
def users():
    pass

# GET user, obtienes la informacion de un usuario (Devuelve un html)
# HINT: return render_template('your_view.html', your_list=your_list)
@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    pass

# GET User Id, devuelve los datos de la persona que inicio sesion (Devuelve un html)
# PUT User Id, actualiza los datos de la persona que inicio sesion
@user_bp.route('/account/<account_id>', methods=['GET', 'PUT'])
def account(account_id):
    if request.method == 'GET':
        pass
    else:
        pass
