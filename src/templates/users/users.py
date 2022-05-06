from flask import Blueprint, flash
from flask import make_response, redirect, render_template, request, url_for

from src.models import User, db

users_bp = Blueprint('users_bp', __name__)


@users_bp.route('/users')
def users():
    users = User.query.all()
    return render_template('/users/index.html', users=users)


@users_bp.route('/users/edit', methods=['GET', 'POST'])
def edit():
    user_id = request.args.get('id', type=str)
    user = User.query.get(user_id)

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        if not username:
            return make_response('Username is requierd!')
        
        user.username = username
        user.email = email

        db.session.commit()

        flash("User Updated Successfully")

        return redirect(url_for('users_bp.users'))
    
    return render_template('/users/edit.html', user=user)


@users_bp.route('/users/delete', methods=['POST'])
def delete():
    user_id = request.args.get('id', type=str)
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        
        flash("User Deleted Successfully")

    return redirect(url_for('users_bp.users'))