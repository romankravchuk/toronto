from flask import Blueprint, flash, request, session, g
from flask import redirect, render_template, url_for
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from database.models import User
from database.user import user_system
from logger import logger


auth = Blueprint('auth', __name__, template_folder='templates', url_prefix="/auth")


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    form = request.form

    username = form.get('username')
    password = form.get('password')
    remember = True if form.get('remember') else False

    user = user_system.get_by_username(username=username)

    logger.debug(f"Get user: {user}")

    if not user or not check_password_hash(user.password, password):
        logger.debug(f'Invalid auth params: {username}, {password}')
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    logger.debug(f'User {user} log in')
    return redirect(url_for('auth.profile'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()

    if session.get('was_once_logged_in'):
        del session['was_once_logged_in']

    logger.debug(f'User successfully logged out')
    flash('You have successfully logged out.', 'info')

    return redirect(url_for('auth.login'))


@auth.route('/signup')
def signup():
    return render_template('auth/signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username', type=str)
    password = request.form.get('password', type=str)

    user = user_system.get_by_username(username=username)

    logger.debug(f'Get user: {user}')

    if user:
        logger.debug(f'User {user} already exists')
        flash('User already exists')
        return redirect(url_for('auth.signup'))

    password_hash = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, password=password_hash)

    user_system.create(user=new_user)

    logger.debug(f'User {new_user} successfully signed up')

    return redirect(url_for('auth.login'))


@auth.route('/profile')
@login_required
def profile():
    user = user_system.get_by_id(user_id=current_user.get_id())

    logger.debug(f'Get user: {user}')

    return render_template('auth/profile.html', user=user)
