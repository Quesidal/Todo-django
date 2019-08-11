from django.db import models
from django.conf import settings
from django_utils.models import UUIDTimestampedModel
from projects.models import Project

import datetime

PRIORITY = ((0, 'Low'),
            (1, 'Medium'),
            (2, 'High'))


class TaskQuerySet(models.QuerySet):
    def week(self):
        today = datetime.date.today()
        return self.filter(end_time__range=(today, today + datetime.timedelta(days=7)))

    def today(self):
        return self.filter(end_time__date=datetime.date.today())

    def old_unfinished_task(self):
        return self.filter(end_time__lt=datetime.date.today()).filter(state=False).filter(priority__lt=2)


class Task(UUIDTimestampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    text = models.CharField(max_length=255, verbose_name='Task')
    end_time = models.DateTimeField(verbose_name='Task end time')
    state = models.BooleanField(default=False, verbose_name='Task state')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Task from project')
    priority = models.CharField(
        max_length=255,
        choices=PRIORITY,
        default='Medium',
    )
    objects = TaskQuerySet.as_manager()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        db_table = 'tasks'

    def __str__(self):
        return f'{self.text}'

    @property
    def str_pk(self):
        return str(self.pk)
