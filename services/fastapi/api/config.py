from dotenv import load_dotenv
from os import getenv


load_dotenv()


class Config(object):
    TOKEN = getenv('TOKEN')
    CONNECTION_STRING = getenv('CONNECTION_STRING')
