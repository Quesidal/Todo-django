from django.db import models
from django.conf import settings

from tasks.helper import UUIDTimestampedModel
from .managers import TaskManager

PRIORITY = ((0, 'Low'),
            (1, 'Medium'),
            (2, 'High'))


class Project(UUIDTimestampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    name = models.CharField(max_length=255, verbose_name='Project name')
    color = models.CharField(max_length=255, verbose_name='Project color')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        db_table = 'projects'

    def __str__(self):
        return f'{self.name}'


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
    objects = TaskManager()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        db_table = 'tasks'

    def __str__(self):
        if len(self.text) > 10:
            return f'{self.text[:50]}...'
        return f'{self.text}'
