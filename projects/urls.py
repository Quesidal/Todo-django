from django.urls import path, include, re_path
from .views import ProjectAddView, ProjectDeleteView, ProjectUpdateView

urlpatterns = [
    path('project/add', ProjectAddView.as_view(), name='project add'),
    re_path(r'^project/update/(?P<uuid>[\S]{36})$', ProjectUpdateView.as_view(), name='project edit'),
    re_path(r'^project/delete/(?P<uuid>[\S]{36})$', ProjectDeleteView.as_view(), name='project delete'),
]
