from django.db import models

import datetime


class TaskManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(state=False)

    def today(self):
        return self.get_queryset().filter(end_time__date=datetime.date.today())

    def week(self):
        today = datetime.date.today()
        return self.get_queryset().filter(end_time__range=(today, today + datetime.timedelta(days=7)))

    def old_unfinished_task(self):
        return self.get_queryset().filter(end_time__lt=datetime.date.today(), state=False)

    def tasks_for_user(self, user):
        return self.get_queryset().filter(author=user)

    def tasks_for_user_and_project(self, user, project):
        return self.get_queryset().filter(project=project, author=user, state=False)

    def today_tasks_for_user(self, user):
        return self.get_queryset().filter(end_time__lt=datetime.date.today(), author=user, state=False)

    def week_tasks_for_user(self, user):
        today = datetime.date.today()
        return self.get_queryset().filter(end_time__range=(today, today + datetime.timedelta(days=7)),
                                          state=False,
                                          author=user) | \
               self.get_queryset().filter(end_time__lt=datetime.date.today(), state=False, author=user)

    def archive_tasks_for_user(self, user):
        return self.get_queryset().filter(author=user, state=True)
