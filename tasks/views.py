from django.views.generic import TemplateView, ListView
from .models import Task


class MainView(TemplateView):
    template_name = "tasks/task_list.html"


class TaskList(ListView):
    model = Task

    def get(self, request, *args, **kwargs):
        pass
