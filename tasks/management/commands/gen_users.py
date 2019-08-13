from django.core.management import BaseCommand

from tasks.management.commands._private import DataSetUp


class Command(BaseCommand):
    help = 'Generate 2 random users'

    def handle(self, *args, **kwargs):
        print('---------start user generation---------')
        for i, user in enumerate(DataSetUp().generate_users(2)):
            print(f'User{i + 1}  username: {user.username}  password: {user.username}')
        print('---------end user generation---------')
