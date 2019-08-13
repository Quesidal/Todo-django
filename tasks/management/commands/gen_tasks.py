from django.contrib.auth.models import User
from django.core.management import BaseCommand

from tasks.management.commands._private import DataSetUp
from tasks.models import Project


class Command(BaseCommand):
    help = 'Generate 10 random tasks'

    def handle(self, *args, **kwargs):
        if User.objects.count() == 0:
            print('Please, add users first')
            return

        if Project.objects.count() == 0:
            print('Please, add projects first')
            return

        print('---------start task generation---------')
        for i, task in enumerate(DataSetUp().generate_tasks(10)):
            print(f'Task{i + 1}  ' + task.__str__())
        print('---------end task generation---------')
