from django.db.models import QuerySet

from .models import Task


def get_task_for_user(user: object) -> QuerySet:
    return Task.objects.filter(author=user)


def get_today_task_for_user(user: object) -> QuerySet:
    return Task.objects.today().filter(author=user)


def get_week_task_for_user(user: object) -> QuerySet:
    return Task.objects.week().filter(author=user)


def get_task_for_uuid(uuid: str) -> Task:
    return Task.objects.get(pk=uuid)


def update_old_unfinished_tasks() -> int:
    old_tasks = Task.objects.old_unfinished_task()
    old_tasks.update(priority='3', text='updated tasks')
    return old_tasks.count()


def get_archive_task_for_user(user: object) -> QuerySet:
    return Task.objects.filter(author=user).filter(state=True)
