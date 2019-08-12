from django.db.models import QuerySet

from .models import Task, Project


def get_task_for_user(user: object) -> QuerySet:
    return Task.objects.filter(author=user)


def get_today_task_for_user(user: object) -> QuerySet:
    return Task.objects.filter(author=user).today().active() | Task.objects.old_unfinished_task()


def get_week_task_for_user(user: object) -> QuerySet:
    return Task.objects.filter(author=user).week().active() | Task.objects.old_unfinished_task()


def get_task_for_uuid(uuid: str) -> Task:
    return Task.objects.get(pk=uuid)


def update_old_unfinished_tasks() -> int:
    old_tasks = Task.objects.old_unfinished_task()
    old_tasks.update(priority='3', text='updated tasks')
    return old_tasks.count()


def get_archive_task_for_user(user: object) -> QuerySet:
    return Task.objects.filter(author=user).filter(state=True)


def get_project_for_uuid(uuid: str) -> Project:
    return Project.objects.get(pk=uuid)


def get_projects_for_user(user: object) -> QuerySet:
    return Project.objects.filter(author=user)
