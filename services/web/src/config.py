from os import getenv
from dotenv import load_dotenv


load_dotenv()


class FlaskConfig:
    SQLALCHEMY_DATABASE_URI = getenv('CONNECTION_STRING')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = getenv('SECRET_KEY')


class Config:
    QUERY_LIMIT = 10
    LOG_FORMAT = "{time} | {level} | {message}"
    ERROR = "ERROR"
    DEBUG = "DEBUG"
    ROTATION = '10 KB'
    COMPRESSION = "zip"
    DEBUG_PATH = getenv('DEBUG_LOG_PATH')
    ERROR_PATH = getenv("ERROR_LOG_PATH")
