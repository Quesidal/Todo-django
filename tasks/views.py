from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from projects.services import get_projects_for_user, get_project_for_uuid
from tasks.task_generator import run
from .models import Task
from .forms import TaskForm
from .services import get_task_for_user, get_task_for_uuid, get_today_task_for_user, get_week_task_for_user, \
    get_archive_task_for_user, update_old_unfinished_tasks


# Displaing views
class TaskListView(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    model = Task
    template_name = "tasks/main_page.html"

    def get(self, request, *args, **kwargs):
        self.proj_uuid = kwargs.get('proj_uuid')  # request.session.get('selected_project') or
        self.task_uuid = kwargs.get('task_uuid') or request.session.get('task_uuid')
        self.edit_proj = request.session.get('edit_project')
        self.drop_my_date_from_session(request)
        return super().get(self, request, *args, **kwargs)

    @staticmethod
    def drop_my_date_from_session(request):
        request.session['task_uuid'] = None
        request.session['edit_project'] = None
        request.session['selected_project'] = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_date = {'projects': get_projects_for_user(self.request.user),
                     'today_task_count': get_today_task_for_user(self.request.user).count(),
                     'week_task_count': get_week_task_for_user(self.request.user).count(),
                     'selected_task': self.task_uuid,
                     'selected_project': self.proj_uuid,
                     'edit_project': self.edit_proj}
        context.update(base_date)
        context.update(self.get_my_date())
        return context

    def get_my_date(self) -> dict:
        my_date = {'tasks': get_task_for_user(self.request.user).order_by('-priority')}
        return my_date


class TaskListForProjectView(TaskListView):
    def get_my_date(self) -> dict:
        project = get_project_for_uuid(self.proj_uuid)
        my_date = {'tasks': get_task_for_user(self.request.user).filter(project=project).active().order_by('-priority')}
        return my_date


class TaskListTodayView(TaskListView):
    def get_my_date(self) -> dict:
        my_date = {'tasks': get_today_task_for_user(self.request.user).order_by('-priority')}
        return my_date


class TaskListWeekView(TaskListView):
    def get_my_date(self) -> dict:
        my_date = {'tasks': get_week_task_for_user(self.request.user).order_by('-priority')}
        return my_date


class TaskArchiveView(TaskListView):
    def get_my_date(self) -> dict:
        my_date = {'tasks': get_archive_task_for_user(self.request.user).order_by('-priority')}
        return my_date


# Handling views
class TaskAddView(View):
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            self._save_task_from_form(form)
        return redirect(request.META.get('HTTP_REFERER'))

    def _save_task_from_form(self, form):
        new_task = Task()
        new_task.author = self.request.user
        new_task.text = form.cleaned_data['text']
        new_task.end_time = form.cleaned_data['end_time']
        new_task.priority = form.cleaned_data['priority']
        new_task.project = get_project_for_uuid(form.cleaned_data['project'])
        new_task.save()


class TaskUpdateView(TaskListView):
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
        update_task = get_task_for_uuid(task_uuid)
        update_task.text = form.cleaned_data['text']
        update_task.end_time = form.cleaned_data['end_time']
        update_task.priority = form.cleaned_data['priority']
        update_task.project = get_project_for_uuid(form.cleaned_data['project'])
        update_task.save()


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        old_task = get_task_for_uuid(kwargs['task_uuid'])
        old_task.delete()
        return redirect(request.META.get('HTTP_REFERER'))


class TaskDoneView(View):
    def get(self, request, *args, **kwargs):
        done_task = get_task_for_uuid(kwargs['task_uuid'])
        done_task.state = True
        done_task.save()
        return redirect(request.META.get('HTTP_REFERER'))


class TaskGenView(TemplateView):
    template_name = "tasks/base_main_page.html"

    def get(self, request, *args, **kwargs):
        run()
        return redirect('/')


from django.core.signals import request_finished
from django.dispatch import receiver


@receiver(request_finished)
def task_updater(sender, **kwargs):
    update_old_unfinished_tasks()
