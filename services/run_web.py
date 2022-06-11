from loguru import logger
from web import create_app


app = create_app()


def run():
    try:
        app.run(debug=True, host='0.0.0.0')
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    run()
