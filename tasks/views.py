from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from projects.services import get_projects_for_user, get_project_for_uuid
from tasks.task_generator import run
from .models import Task
from .forms import TaskForm
from .services import get_task_for_user, get_task_for_uuid




class TaskListView(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    model = Task
    template_name = "tasks/main_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_my_date())
        return context

    def get_my_date(self) -> dict:
        my_date = {'projects': get_projects_for_user(self.request.user),
                   'tasks': get_task_for_user(self.request.user).order_by('-priority')
                   }
        return my_date


class TaskListForProjectView(TaskListView):

    def get(self, request, *args, **kwargs):
        self.proj_uuid = kwargs['uuid']
        return super().get(self, request, *args, **kwargs)

    def get_my_date(self) -> dict:
        project = get_project_for_uuid(self.proj_uuid)
        my_date = {'projects': get_projects_for_user(self.request.user),
                   'tasks': get_task_for_user(self.request.user).filter(project=project)
                   }
        return my_date


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
        new_task.project = get_project_for_uuid(form.cleaned_data['project'])
        new_task.save()


class TaskUpdateView(TaskListView):
    template_name = 'tasks/main_page.html'

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            self._update_task_from_form(form, kwargs['uuid'])
        return redirect('/')

    def get(self, request, *args, **kwargs):
        self.uuid = kwargs['uuid']
        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_task'] = self.uuid
        return context

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
        old_task = get_task_for_uuid(kwargs['uuid'])
        old_task.delete()
        return redirect('/')


class TaskDoneView(View):
    def get(self, request, *args, **kwargs):
        done_task = get_task_for_uuid(kwargs['uuid'])
        done_task.state = True
        done_task.save()
        return redirect('/')


class TaskGenView(TemplateView):
    template_name = "tasks/base_main_page.html"

    def get(self, request, *args, **kwargs):
        run()
        return redirect('/')
