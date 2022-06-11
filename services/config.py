from os import getenv
from dotenv import load_dotenv


load_dotenv()


class FlaskConfig:
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
    CONNECTION_STRING = getenv('CONNECTION_STRING')


class BotConfig(object):
    TOKEN = getenv('TOKEN')
    BOT = 'toronto'
    ID = 976496233763987456
    PREFIX = "?"
    OWNERS = (324462804939833345, )
    GUILDS = (616889320841674753, 879709795760889937)
    COGS = ['tasks']
