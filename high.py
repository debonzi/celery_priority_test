# -*- encoding: utf-8 -*-
from tasks import slow_task

# for i in range(30):
#     slow_task.apply_async(("HIGH!!!!!",), priority=0)
slow_task.apply_async(("HIGH!!!!!",), priority=0)
