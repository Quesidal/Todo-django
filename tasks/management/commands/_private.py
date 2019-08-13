import datetime
import random

import pytz
from django.contrib.auth.models import User
from faker import Faker

from tasks.models import Project, PRIORITY, Task


class DataSetUp:

    def __init__(self):
        self.fake = Faker()

    def generate_projects(self, count):
        user_count = User.objects.count()
        for i in range(count):
            new_project = Project.objects.create(
                author=User.objects.all()[random.randint(0, user_count - 1)],
                name=self.fake.company(),
                color=self.fake.hex_color()
            )
            yield new_project

    def generate_tasks(self, count):
        user_count = User.objects.count()
        for i in range(count):
            user = User.objects.all()[random.randint(0, user_count - 1)]
            proj_count = Project.objects.filter(author=user).count()
            if proj_count == 0:
                yield "---User haven't projects, go to next task---"
                continue
            if proj_count == 1:
                project = Project.objects.filter(author=user).first()
            else:
                project = Project.objects.filter(author=user)[random.randint(0, proj_count - 1)]

            new_task = Task.objects.create(
                author=user,
                text=self.fake.text(),
                end_time=self.date_for_task(),
                priority=PRIORITY[random.randint(0, 2)][0],
                project=project,
                state=bool(random.getrandbits(1))
            )
            yield new_task

    def generate_users(self, count):
        users_count = User.objects.count()
        for i in range(count):
            username = self.fake.first_name() + str(users_count + i)
            user = User.objects.create_user(username=username,
                                            email=self.fake.ascii_email(),
                                            password=username)
            yield user

    def date_for_task(self):
        today = datetime.date.today()
        return self.fake.date_time_between(start_date=today - datetime.timedelta(days=2),
                                           end_date=today + datetime.timedelta(days=30),
                                           tzinfo=pytz.UTC)
