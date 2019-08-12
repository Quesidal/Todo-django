from django.core.management import BaseCommand
from faker import Faker

from django.contrib.auth.models import User

from tasks.models import Project

fake = Faker()


class Command(BaseCommand):
    help = 'Generate 10 random projects'

    def handle(self, *args, **kwargs):
        if User.objects.count() == 0:
            print('Please, add users first')
            return
        print('---------start project generation---------')
        for i in range(10):
            new_project = Project()
            new_project.author = User.objects.all().order_by("?").first()
            new_project.name = fake.company()
            new_project.color = fake.hex_color()
            new_project.save()
            print(f'Project{i + 1}  ' + new_project.__str__())
        print('---------end project generation---------')
