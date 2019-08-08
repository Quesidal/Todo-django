from django.db import models
from django.conf import settings
from django_utils.models import UUIDTimestampedModel

PRIORITY = (('L', 'Low'),
            ('M', 'Medium'),
            ('H', 'High'))


class Project(UUIDTimestampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    name = models.CharField(max_length=255, verbose_name='Project name')
    description = models.CharField(max_length=255, verbose_name='Project description')

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

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        db_table = 'tasks'

    def __str__(self):
        return f'{self.text}'
