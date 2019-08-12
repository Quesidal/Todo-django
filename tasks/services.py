from django.db.models import QuerySet

from .models import Task, Project


def get_task_for_uuid(uuid: str) -> Task:
    return Task.objects.get(pk=uuid)


def get_project_for_uuid(uuid: str) -> Project:
    return Project.objects.get(pk=uuid)
