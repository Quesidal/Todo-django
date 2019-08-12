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
        old_proj = get_project_for_uuid(kwargs['proj_uuid'])
        if old_proj.count_active_task == 0:
            old_proj.delete()
        return redirect(request.META.get('HTTP_REFERER'))


class ProjectUpdateView(TaskListView):
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
        update_proj = get_project_for_uuid(proj_uuid)
        update_proj.name = form.cleaned_data['name']
        update_proj.color = form.cleaned_data['color']
        update_proj.save()

