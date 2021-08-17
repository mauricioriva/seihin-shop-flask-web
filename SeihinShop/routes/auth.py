from flask import request, Blueprint, render_template, redirect, url_for, g, session
from flask_mail import Message, Mail
import functools, secrets, string
from ..db import get_db

mail = Mail()

# from flaskr.db import get_db
def getMail(app):
    mail.init_app(app)

auth_bp = Blueprint('auth_page', __name__, template_folder='./../templates/auth')

@auth_bp.route('/oauth/login', methods=['GET', 'POST'])
def login():
    error = None
    # self.password = generate_password_hash(password)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_db().execute('SELECT * FROM user WHERE username=?', (username,)).fetchone()
        if (not user):
            return redirect(url_for('auth_page.login'))
        if (user[2] == password):
            # return check_password_hash(self.password, password) # Implementar hash
            # Guardar entidad en g
            session['user_id'] = user[0]
            return redirect(url_for('products_page.products'))
        else:
            return redirect(url_for('auth_page.login'))
    else:
        return render_template('login.html', error=error)

@auth_bp.route('/oauth/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        last_name = request.form['last_name']
        email = request.form['email']
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        get_db().execute('INSERT INTO user (name, last_name, username, password, email) VALUES (?, ?, ?, ?, ?)', (name, last_name, username, password, email))
        get_db().commit()
        msg = Message("Gracias por Registrarte en Seihin Shop",
            sender="seihinshop2021@gmail.com",
            recipients=[email])
        msg.body = 'Bienvenid@ a Seihin Shop ' + name + 'Tu nombre de usuario: ' + username +'\nTu contraseña es: ' + password
        msg.html = '<p>Bienvenid@ a <strong>Seihin Shop </strong>' + name + '</p>\n<p>Tu nombre de usuario: ' + username + '</p>\n<p>Tu contraseña es: ' + password + '</p>'
        mail.send(msg)
        return redirect(url_for('auth_page.login'))
    else:
        return render_template('signup.html', error=error)

@auth_bp.route('/oauth/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('auth_page.login'))

@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth_page.login'))
        return view(**kwargs)
    return wrapped_view

@auth_bp.route('/', methods=['GET'])
def home():
    return redirect(url_for('auth_page.login'))
