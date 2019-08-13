from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Task, Project


class BaseTaskListMixin(LoginRequiredMixin, ListView):
    login_url = 'accounts/login/'
    model = Task
    template_name = "tasks/main_page.html"

    def get(self, request, *args, **kwargs):
        self.proj_uuid = kwargs.get('proj_uuid')
        self.task_uuid = kwargs.get('task_uuid') or request.session.get('task_uuid')
        self.edit_proj = request.session.get('edit_project')
        self.drop_my_data_from_session(request)
        return super().get(self, request, *args, **kwargs)

    @staticmethod
    def drop_my_data_from_session(request):
        request.session['task_uuid'] = None
        request.session['edit_project'] = None
        request.session['selected_project'] = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_date = {'projects': Project.objects.filter(author=self.request.user),
                     'today_task_count': Task.objects.today_tasks_for_user(self.request.user).count(),
                     'week_task_count': Task.objects.week_tasks_for_user(self.request.user).count(),
                     'selected_task': self.task_uuid,
                     'selected_project': self.proj_uuid,
                     'edit_project': self.edit_proj}
        context.update(base_date)
        context.update(self.get_my_data())
        return context

    def get_my_data(self):
        my_date = {'tasks': Task.objects.tasks_for_user(self.request.user).order_by('-priority')}
        return my_date
