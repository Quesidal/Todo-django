from django.db import models
from django.conf import settings
from django_utils.models import UUIDTimestampedModel

PRIORITY = ('Low', 'Medium', 'High')


class Project(UUIDTimestampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='')
    description = models.CharField(max_length=255, verbose_name='')

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        db_table = 'projects'

    def __str__(self):
        return f'{self.name}'


class Task(UUIDTimestampedModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, verbose_name='')
    end_time = models.DateTimeField()
    state = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
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
