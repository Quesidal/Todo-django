from django.db.models import QuerySet

from projects.models import Project


def get_project_for_uuid(uuid: str) -> Project:
    return Project.objects.get(pk=uuid)


def get_projects_for_user(user: object) -> QuerySet:
    return Project.objects.filter(author=user)
