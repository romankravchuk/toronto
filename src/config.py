from os import getenv
from dotenv import load_dotenv


load_dotenv()


class FlaskConfig:
    SQLALCHEMY_DATABASE_URI = getenv('CONNECTION_STRING')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY')


class Config:
    QUERY_LIMIT=5
