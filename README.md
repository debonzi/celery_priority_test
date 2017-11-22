# Celery Priority Test
## How to run?

#### Start Worker with concurency 1 to make it easier to see results
```
 celery -A tasks worker -c 1 --loglevel=info
```

#### Send 10000 tasks with low priority executing
```
python low.py
```

#### While watching the tasks been executed in the worker terminal, send a task with high priority with command
```
python high.py
```

#### You should see the a verbose log for the task with high priority

## Important stuff:
`config.py:CELERYD_PREFETCH_MULTIPLIER=1`

Checkout http://docs.celeryproject.org/en/latest/userguide/optimizing.html#optimizing-prefetch-limit
