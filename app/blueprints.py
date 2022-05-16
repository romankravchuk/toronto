from flask import current_app as app
from flask import render_template
from flask_login import LoginManager
from werkzeug.exceptions import NotFound

from .models.session_user import SessionUser
from .routes.users import users
from .routes.auth import auth

app.register_blueprint(auth)
app.register_blueprint(users)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(NotFound)
def not_found(error):
    return render_template('404.html'), 404


@login_manager.user_loader
def load_user(user_id):
    return SessionUser.query.get(int(user_id))
