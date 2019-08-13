from django import template

from tasks.models import Task

register = template.Library()


@register.simple_tag
def task_count_for_user_project(user, project):
    return Task.objects.filter(project=project, state=False, author=user).count()
