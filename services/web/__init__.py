from flask import Flask

from config import FlaskConfig
from database import engine
from database.models import Base as db


def create_app():
    db.metadata.create_all(bind=engine)
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(FlaskConfig)

    with app.app_context():
        from . import blueprints

        return app
