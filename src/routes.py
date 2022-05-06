from flask import current_app as app
from flask import render_template

from .templates.users import users


app.register_blueprint(users.users_bp)


@app.route('/')
def index():
    return render_template('index.html')
