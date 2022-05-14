from flask import Blueprint, flash, request, session
from flask import redirect, render_template, url_for
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from src.models import SessionUser, db

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates')


@auth_bp.route('/login')
def login():
    return render_template('login.html')


@auth_bp.route('/login', methods=['POST'])
def login_post():
    form = request.form

    username = form.get('username')
    password = form.get('password')
    remember = True if form.get('remember') else False

    user = SessionUser.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth_bp.login'))

    login_user(user, remember=remember)
    return redirect(url_for('auth_bp.profile'))


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()

    if session.get('was_once_logged_in'):
        del session['was_once_logged_in']

    flash('You have successfully logged out.')

    return redirect(url_for('auth_bp.login'))


@auth_bp.route('/signup')
def signup():
    return render_template('signup.html')


@auth_bp.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username', type=str)
    password = request.form.get('password', type=str)

    user = SessionUser.query.filter_by(username=username).first()

    if user:
        flash('User already exists')
        return redirect(url_for('auth_bp.signup'))

    password_hash = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = SessionUser(username=username, password=password_hash)


    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth_bp.login'))


@auth_bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)
