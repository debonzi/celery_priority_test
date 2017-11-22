# -*- encoding: utf-8 -*-
from kombu import Exchange, Queue

BROKER_URL = 'redis://localhost:6379/15'
CELERYD_PREFETCH_MULTIPLIER = 1
CELERY_QUEUES = [
    Queue('celery_priority_test', Exchange('celery_priority_test'), routing_key='celery_priority_test')
]
