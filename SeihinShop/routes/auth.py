from flask import request, Blueprint, render_template, redirect, url_for, g, session
from werkzeug.security import check_password_hash, generate_password_hash
import functools

# from flaskr.db import get_db

auth_bp = Blueprint('auth_page', __name__, template_folder='./../templates/auth')

@auth_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = [(id, 2)] 
        #get_db().execute(
            #'SELECT * FROM user WHERE id = ?', (user_id,)
        #).fetchone()


@auth_bp.route('/oauth/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # 1 Check username and password in db
        # 2 Redirect to home page
        # return redirect(url_for('products_page.products'))
        session['user_id'] = 2
        print(g.user)
        return render_template('base.html', error=error)
        pass
    else:
        # Display HTML to make POST request
        print(g.user)
        return render_template('login.html', error=error)
        pass

@auth_bp.route('/oauth/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        # 1 Register username and password in db
        # 2 Redirect to login
        # return redirect(url_for('auth_page.login'))
        pass
    else:
        # Display HTML to make POST request
        # return render_template('signup.html', error=error)
        pass

@auth_bp.route('/oauth/logout', methods=['GET'])
def logout():
    # session.clear()
    # return redirect(url_for('auth_page.login'))
    pass
