from django.db.models import QuerySet

from .models import Project, Task


def get_project_by_name(name: str) -> Project:
    return Project.objects.get(name=name)


def get_projects_for_user(user: object) -> QuerySet:
    return Project.objects.filter(author=user)


def get_task_for_user(user: object) -> QuerySet:
    return Task.objects.filter(author=user)
