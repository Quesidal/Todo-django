from django.core.management import BaseCommand

from tasks.management.commands._private import DataSetUp


class Command(BaseCommand):
    help = 'Generate 1 user 4 projects 40 tasks'

    def handle(self, *args, **kwargs):
        self.setup_test_data()

    @staticmethod
    def setup_test_data():
        my_data = DataSetUp()

        user = list(my_data.generate_users(1))[0]

        for i, task in enumerate(my_data.generate_projects(4)):
            print(f'Project{i + 1}  ' + task.__str__())

        for i, task in enumerate(my_data.generate_tasks(40)):
            print(f'Task{i + 1}  ' + task.__str__())

        print(f'\nUser1  username: {user.username}  password: {user.username}')
