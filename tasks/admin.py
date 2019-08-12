from django.contrib import admin

from .models import Project, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ['task_create']

    @staticmethod
    def task_create(obj):
        return f'{obj.created}'
