from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Task


class SignInView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signin.html'


class LoginView(TemplateView):
    template_name = "registration/login.html"


class TaskList(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    model = Task
    template_name = "tasks/task_list.html"

    def get_queryset(self):
        """Filter only user's tasks"""
        return Task.objects.filter(author=self.request.user)
