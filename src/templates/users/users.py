from math import ceil
from flask import Blueprint, flash, abort
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from src.models import User, db
from src.config import Config

users_bp = Blueprint('users_bp', __name__, template_folder='templates')


@users_bp.route('/users')
@login_required
def users():
    page = request.args.get('page', default=1, type=int)
    
    page_size = (page - 1) * Config.QUERY_LIMIT;
    users_count = User.query.count()
    last_page = ceil(users_count / Config.QUERY_LIMIT)

    users = User.query.order_by(User.id).limit(Config.QUERY_LIMIT).offset(page_size).all()

    return render_template('users.html', users=users, page=page, last_page=last_page)


@users_bp.route('/users/edit', methods=['GET', 'POST'])
@login_required
def edit():
    user_id = request.args.get('id', type=str)
    user = User.query.get(user_id)

    if not user:
        abort(404)

    if request.method == 'GET':
        return render_template('edit.html', user=user)

    username = request.form['username']
    email = request.form['email']
        
    user.username = username
    user.email = email

    db.session.commit()

    flash("{} updated successfully".format(user.username), "info")

    return redirect(url_for('users_bp.users'))
    



@users_bp.route('/users/delete', methods=['POST'])
@login_required
def delete():
    user_id = request.args.get('id', type=str)
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        
        flash("{} deleted successfully".format(user.username), 'info')

    return redirect(url_for('users_bp.users'))