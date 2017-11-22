# -*- encoding: utf-8 -*-
from tasks import slow_task

for i in range(1000):
    slow_task.apply_async(("LOW!!!!!!",), priority=9)
