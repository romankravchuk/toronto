from dotenv import load_dotenv
from os import environ


load_dotenv()


class Settings(object):
    TOKEN = environ.get('TOKEN')
    BOT = 'toronto'
    ID = 976496233763987456
    PREFIX = "?"
    CONNECTION_STRING = environ.get('DATABASE_URL')
    OWNERS = (324462804939833345, )
    GUILDS = (616889320841674753, 879709795760889937)
    COGS = ['tasks']
