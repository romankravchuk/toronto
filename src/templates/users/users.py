from flask import Blueprint, flash, abort
from flask import redirect, render_template, request, url_for

from src.models import User, db

users_bp = Blueprint('users_bp', __name__, template_folder='templates')


@users_bp.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)


@users_bp.route('/users/edit', methods=['GET', 'POST'])
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
def delete():
    user_id = request.args.get('id', type=str)
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        
        flash("{} deleted successfully".format(user.username), 'info')

    return redirect(url_for('users_bp.users'))