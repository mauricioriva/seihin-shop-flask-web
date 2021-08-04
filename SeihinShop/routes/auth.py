from flask import request, Blueprint, render_template, redirect, url_for, g, session
from werkzeug.security import check_password_hash, generate_password_hash
import functools
from ..db import get_db

# from flaskr.db import get_db

auth_bp = Blueprint('auth_page', __name__, template_folder='./../templates/auth')

@auth_bp.route('/oauth/login', methods=['GET', 'POST'])
def login():
    error = None
    self.password = generate_password_hash(password)
    # self.username = username
        return check_password_hash(self.password, password)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_db().execute('SELECT * FROM user WHERE username=?', (username,)).fetchone()
        if (user[2] == password): 
            # return check_password_hash(self.password, password) # Implementar hash
            # Guardar entidad en g
            g.user = user
            return redirect(url_for('users_page.users'))
        else:
            return redirect(url_for('auth_page.login')), 200
    else:
        return render_template('login.html', error=error)

@auth_bp.route('/oauth/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] # Hashea contrasena
        name = request.form['name']
        last_name = request.form['last_name']
        get_db().execute('INSERT INTO user (name, last_name, username, password) VALUES (?, ?, ?, ?)', (name, last_name, username, password))
        get_db().commit()
        return redirect(url_for('auth_page.login'))
    else:
        return render_template('signup.html', error=error)


@auth_bp.route('/oauth/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('auth_page.login'))
    # pass

@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

@auth_bp.route('/', methods=['GET'])
def home():
    return redirect(url_for('auth_page.login'))
    