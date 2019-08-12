from django.core.signals import request_finished
from django.dispatch import receiver

from .models import Task


@receiver(request_finished)
def old_task_updater(sender, **kwargs):
    old_tasks = Task.objects.old_unfinished_task()
    old_tasks.update(priority='3', text='updated tasks')
    # print('tasks was updated')
