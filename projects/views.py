from django.shortcuts import redirect
from django.views import View

from projects.forms import ProjectForm
from projects.models import Project
from projects.services import get_project_for_uuid
from tasks.views import TaskListView


class ProjectAddView(View):
    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)
        if form.is_valid():
            self._save_project_from_form(form)
        return redirect('/')

    def _save_project_from_form(self, form):
        new_project = Project()
        new_project.author = self.request.user
        new_project.name = form.cleaned_data['name']
        new_project.color = form.cleaned_data['color']
        new_project.save()


class ProjectDeleteView(View):
    def get(self, request, *args, **kwargs):
        old_task = get_project_for_uuid(kwargs['uuid'])
        old_task.delete()
        return redirect('/')


class ProjectUpdateView(TaskListView):
    template_name = 'tasks/main_page.html'

    def post(self, request, *args, **kwargs):
        form = ProjectForm(request.POST)
        if form.is_valid():
            self._update_proj_from_form(form, kwargs['uuid'])
        return redirect('/')

    def get(self, request, *args, **kwargs):
        self.uuid = kwargs['uuid']
        return super().get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_project'] = self.uuid
        return context

    @staticmethod
    def _update_proj_from_form(form, proj_uuid):
        update_proj = get_project_for_uuid(proj_uuid)
        update_proj.name = form.cleaned_data['name']
        update_proj.color = form.cleaned_data['color']
        update_proj.save()
