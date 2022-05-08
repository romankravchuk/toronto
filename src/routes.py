from flask import current_app as app
from flask import render_template
from flask_login import LoginManager

from .templates.users import users
from .templates.auth import auth
from .models import SessionUser

app.register_blueprint(users.users_bp)
app.register_blueprint(auth.auth_bp)

login_manager = LoginManager()
login_manager.login_view = 'auth_bp.login'
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


@login_manager.user_loader
def load_user(user_id):
    return SessionUser.query.get(int(user_id))
