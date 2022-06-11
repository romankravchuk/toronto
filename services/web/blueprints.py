from flask import current_app as app
from flask import render_template
from flask_login import LoginManager
from werkzeug.exceptions import NotFound

from database.user import user_system
from logger import logger

from .routes.auth import auth
from .routes.members import members


app.register_blueprint(auth)
app.register_blueprint(members)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(NotFound)
def not_found(error):
    logger.error(error)
    return render_template('404.html'), 404


@login_manager.user_loader
def load_user(user_id):
    return user_system.get_by_id(int(user_id))
