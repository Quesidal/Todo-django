import random
import string
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from .models import Task, PRIORITY, Project

COUNT_TASK = 10


def gen_datetime(min_year=1900, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


def run():
    for i in range(COUNT_TASK):
        new_task = Task()
        new_task.author = User.objects.order_by("?").first()
        new_task.text = "".join([random.choice(string.ascii_lowercase) for i in range(15)])
        new_task.end_time = gen_datetime()
        new_task.priority = PRIORITY[random.randint(0, 2)][0]
        new_task.project = Project.objects.all().order_by("?").first()
        new_task.save()
