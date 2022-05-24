from dotenv import load_dotenv
from os import getenv


load_dotenv()


class Config(object):
    CONNECTION_STRING = getenv('CONNECTION_STRING')
    ACCESS_LOG_PATH = getenv('ACCESS_LOG_PATH')
    ERROR_LOG_PATH = getenv('ERROR_LOG_PATH')
