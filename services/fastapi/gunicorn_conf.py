from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/var/www/fastapi-app/gunicorn.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/var/www/fastapi-app/logs/access_log'
errorlog =  '/var/www/fastapi-app/logs/error_log'