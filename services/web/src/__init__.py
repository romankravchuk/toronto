from flask import Flask

from .config import FlaskConfig
from .database import db


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(FlaskConfig)

    db.init_app(app)

    with app.app_context():
        from . import blueprints

        db.create_all()

        return app
