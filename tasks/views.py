from django.http import HttpResponseNotFound
from django.shortcuts import redirect, get_object_or_404
from django.views import View

from .mixins import TaskListLoginMixin
from .models import Task, Project
from .forms import TaskForm, ProjectForm


# Displaing views


class TaskListForProjectView(TaskListLoginMixin):
    def get_my_date(self) -> dict:
        project = get_object_or_404(Project, pk=self.proj_uuid)
        my_date = {'tasks': Task.objects.tasks_for_user_and_project(self.request.user, project).order_by('-priority')}
        return my_date


class TaskListTodayView(TaskListLoginMixin):
    def get_my_date(self) -> dict:
        my_date = {'tasks': Task.objects.today_tasks_for_user(self.request.user).order_by('-priority')}
        return my_date


class TaskListWeekView(TaskListLoginMixin):
    def get_my_date(self) -> dict:
        my_date = {'tasks': Task.objects.week_tasks_for_user(self.request.user).order_by('-priority')}
        return my_date


class TaskArchiveView(TaskListLoginMixin):
    def get_my_date(self) -> dict:
        my_date = {'tasks': Task.objects.archive_tasks_for_user(self.request.user).order_by('-priority')}
        return my_date


# Handling views
class TaskAddView(View):
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            self._save_task_from_form(form)
        return redirect('/')

    def _save_task_from_form(self, form):
        new_task = Task()
        new_task.author = self.request.user
        new_task.text = form.cleaned_data['text']
        new_task.end_time = form.cleaned_data['end_time']
        new_task.priority = form.cleaned_data['priority']
        new_task.project = get_object_or_404(Project, pk=form.cleaned_data['project'])
        new_task.save()


class TaskUpdateView(TaskListLoginMixin):
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            self._update_task_from_form(form, kwargs['task_uuid'])
        return redirect(request.META.get('HTTP_REFERER'))

    def get(self, request, *args, **kwargs):
        request.session['task_uuid'] = kwargs.get('task_uuid')
        return redirect(request.META.get('HTTP_REFERER'))

    @staticmethod
    def _update_task_from_form(form, task_uuid):
        update_task = get_object_or_404(Task, pk=task_uuid)
        update_task.text = form.cleaned_data['text']
        update_task.end_time = form.cleaned_data['end_time']
        update_task.priority = form.cleaned_data['priority']
        update_task.project = get_object_or_404(Project, pk=form.cleaned_data['project'])
        update_task.save()


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        old_task = get_object_or_404(Task, pk=kwargs['task_uuid'])
        old_task.delete()
        return redirect(request.META.get('HTTP_REFERER'))


class TaskDoneView(View):
    def get(self, request, *args, **kwargs):
        done_task = get_object_or_404(Task, pk=kwargs['task_uuid'])
        done_task.state = True
        done_task.save()
        return redirect(request.META.get('HTTP_REFERER'))


# project views
class ProjectAddView(View):
    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)
        if form.is_valid():
            self._save_project_from_form(form)
        return redirect(request.META.get('HTTP_REFERER'))

    def _save_project_from_form(self, form):
        new_project = Project()
        new_project.author = self.request.user
        new_project.name = form.cleaned_data['name']
        new_project.color = form.cleaned_data['color']
        new_project.save()


class ProjectDeleteView(View):
    def get(self, request, *args, **kwargs):
        old_proj = get_object_or_404(Project, pk=kwargs['proj_uuid'])
        if old_proj.count_active_task == 0:
            old_proj.delete()
            return redirect('/')
        return HttpResponseNotFound('<h1>Sorry, project have tasks</h1>')


class ProjectUpdateView(TaskListLoginMixin):
    template_name = 'tasks/main_page.html'

    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)
        if form.is_valid():
            self._update_proj_from_form(form, kwargs['proj_uuid'])
        return redirect(request.META.get('HTTP_REFERER'))

    def get(self, request, *args, **kwargs):
        request.session['edit_project'] = kwargs.get('proj_uuid')
        return redirect(request.META.get('HTTP_REFERER'))

    @staticmethod
    def _update_proj_from_form(form, proj_uuid):
        update_proj = get_object_or_404(Project, pk=proj_uuid)
        update_proj.name = form.cleaned_data['name']
        update_proj.color = form.cleaned_data['color']
        update_proj.save()

