from django.db import models
from django_utils.models import UUIDTimestampedModel
from django.conf import settings


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
