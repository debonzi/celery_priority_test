# -*- encoding: utf-8 -*-
import logging
import time
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
logger.setLevel(logging.INFO)

app = Celery('tasks')
app.config_from_object('config')


@app.task(queue='celery_priority_test')
def slow_task(priority):
    if priority.startswith('HIGH'):
        logger.info("GOT TASK PRIORITY ----------------- %s" % priority)
    time.sleep(2)
