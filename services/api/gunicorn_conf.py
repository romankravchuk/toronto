from multiprocessing import cpu_count
from src.config import Config

# Socket Path
bind = 'unix:/var/www/fastapi-app/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = Config.ACCESS_LOG_PATH
errorlog =  Config.ERROR_LOG_PATH