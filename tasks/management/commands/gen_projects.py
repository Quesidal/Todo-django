from django.core.management import BaseCommand

from django.contrib.auth.models import User

from tasks.management.commands._private import DataSetUp


class Command(BaseCommand):
    help = 'Generate 4 random projects'

    def handle(self, *args, **kwargs):
        if User.objects.count() == 0:
            print('Please, add users first')
            return
        print('---------start project generation---------')
        for i, project in enumerate(DataSetUp().generate_projects(4)):
            print(f'Project{i + 1}  ' + project.__str__())
        print('---------end project generation---------')
