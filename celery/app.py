from celery import Celery
from celery import backends
from flask import Flask
from time import sleep
import os
import structlog
# tasks.py
# from celery_redis_sentinel import register

# has to be called before creating celery app
# register()

logger = structlog.get_logger()

redis_server = os.environ['REDIS_SERVER']
db_server = os.environ['POSTGRES_SERVER']
db_user = os.environ['POSTGRES_USER']
db_pass = os.environ['POSTGRES_PASS']

# redis_server = 'localhost:37677'
# db_server = 'localhost:35341'
# db_user = 'postgres'
# db_pass = 'postgres'


## CELERY ROUTES
# CELERY_ROUTES = {
#     'app.tasks.count': {'queue': 'queue1'},
#     'app.tasks.other': {'queue': 'queue2'},
# }

web = Flask(__name__)
counting = Celery('app', 
  broker=f'redis-sentinel://{redis_server}', 
  backend=f'db+postgresql+psycopg2://{db_user}:{db_pass}@{db_server}'
)

@counting.task
def count(num):
    logger.info( 'Counting to ' + str(num) )
    for i in range(num):
        logger.info(i+1)
        sleep(1)
        pass
    return 'Done.'

@web.route('/start/<number>')
def start(number):
    count.delay(int(number))
    return 'Task scheduled: counting to ' + str(number)
