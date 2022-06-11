from bot.bot import bot
from logger import logger
from config import BotConfig


def run():
    try:
        bot.run(BotConfig.TOKEN)
    except AttributeError as e:
        logger.error(e)


if __name__ == '__main__':
    run()
