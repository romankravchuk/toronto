from math import ceil
from flask import Blueprint, flash, abort
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from ..database import db
from ..models.user import User
from ..config import Config

users = Blueprint('users', __name__, template_folder='templates', url_prefix='/users')


@users.route('/')
@login_required
def index():
    page = request.args.get('page', default=1, type=int)
    
    page_size = (page - 1) * Config.QUERY_LIMIT;
    users_count = User.query.count()
    last_page = ceil(users_count / Config.QUERY_LIMIT)

    users = User.query.order_by(User.id).limit(Config.QUERY_LIMIT).offset(page_size).all()

    return render_template('users/users.html', users=users, page=page, last_page=last_page)


@users.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    user_id = request.args.get('id', type=str)
    user = User.query.get(user_id)

    if not user:
        abort(404)

    if request.method == 'GET':
        return render_template('users/edit.html', user=user)

    username = request.form['username']
    email = request.form['email']
        
    user.username = username
    user.email = email

    db.session.commit()

    flash("{} updated successfully".format(user.username), "info")

    return redirect(url_for('users.users'))
    



@users.route('/delete', methods=['POST'])
@login_required
def delete():
    user_id = request.args.get('id', type=str)
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        
        flash("{} deleted successfully".format(user.username), 'info')

    return redirect(url_for('users.index'))