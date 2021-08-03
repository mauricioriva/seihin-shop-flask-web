from flask import request, Blueprint, render_template
from ..db import get_db

user_bp = Blueprint('users_page', __name__, template_folder='./../templates/user')

# GET users (obtienes la lista de usuarios registrados) (Devuelve un html)
# HINT: return render_template('your_view.html', your_list=your_list)
@user_bp.route('/users', methods=['GET'])
def users():
    users = get_db().execute(
        'SELECT * FROM user'
    ).fetchall()
    return render_template('list-users.html', users=users)

# GET user, obtienes la informacion de un usuario (Devuelve un html)
# HINT: return render_template('your_view.html', your_list=your_list)
@user_bp.route('/users/<user_id>', methods=['GET', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        user = get_db().execute(
            'SELECT * FROM user WHERE id=?', (user_id)
        ).fetchone()
        return render_template('user.html', user=user)
    else:
        pass #Guardar
