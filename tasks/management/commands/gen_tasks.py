import random

import pytz
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from faker import Faker

from tasks.models import Project, Task, PRIORITY

fake = Faker()


class Command(BaseCommand):
    help = 'Generate 10 random tasks and 10 projects(if they not exists)'

    def handle(self, *args, **kwargs):
        if User.objects.count() == 0:
            print('Please, add users first')
            return
        print('---------start task generation---------')
        if Project.objects.count() == 0:
            for i in range(10):
                new_project = Project()
                new_project.author = User.objects.all().order_by("?").first()
                new_project.name = fake.company()
                new_project.color = fake.hex_color()
                new_project.save()
        for i in range(10):
            new_task = Task()
            new_task.author = User.objects.all().order_by("?").first()
            new_task.text = fake.text()
            new_task.end_time = fake.date_time(tzinfo=pytz.UTC)
            new_task.priority = PRIORITY[random.randint(0, 2)][0]
            new_task.project = Project.objects.all().order_by("?").first()
            new_task.save()
            print(f'Task{i + 1}  ' + new_task.__str__())
        print('---------end task generation---------')
