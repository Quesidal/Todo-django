from django.db.models import QuerySet

from .models import Task


def get_task_for_user(user: object) -> QuerySet:
    return Task.objects.filter(author=user)


def get_task_for_uuid(uuid: str) -> Task:
    return Task.objects.get(pk=uuid)
