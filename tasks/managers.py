from django.db import models

import datetime


class TaskQuerySet(models.QuerySet):
    def old_unfinished_task(self):
        return self.filter(end_time__lt=datetime.date.today())

    def week(self):
        today = datetime.date.today()
        return self.filter(end_time__range=(today, today + datetime.timedelta(days=7)))

    def today(self):
        return self.filter(end_time__date=datetime.date.today())

    def active(self):
        return self.filter(state=False)


class TaskManager(models.Manager):
    def get_queryset(self):
        return TaskQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def old_unfinished_task(self):
        return self.get_queryset().old_unfinished_task()
