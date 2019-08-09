from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm
from .services import get_project_by_name, get_projects_for_user, get_task_for_user


class TestView(TemplateView):
    template_name = 'tasks/main_page.html'


class SignInView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signin.html'


class LoginView(TemplateView):
    template_name = "registration/login.html"


class TaskList(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    model = Task
    template_name = "tasks/main_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_my_date())
        return context

    def get_my_date(self) -> dict:
        my_date = {'projects': get_projects_for_user(self.request.user),
                   'tasks': get_task_for_user(self.request.user),
                   'form': TaskForm()}
        return my_date


class TaskAddView(TemplateView):
    template_name = "tasks/main_page.html"

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            self.__save_task_from_form(form)
        return redirect('/')

    def __save_task_from_form(self, form):
        new_task = Task()
        new_task.author = self.request.user
        new_task.text = form.cleaned_data['text']
        new_task.end_time = form.cleaned_data['end_time']
        new_task.priority = form.cleaned_data['priority']
        new_task.project = get_project_by_name(form.cleaned_data['project'])
        new_task.save()
