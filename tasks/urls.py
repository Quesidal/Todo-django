from django.urls import path, include, re_path
from .views import TaskListView, TaskAddView, TaskGenView, TaskDeleteView, TaskUpdateView, TaskDoneView, \
    TaskListForProjectView, TaskListTodayView, TaskListWeekView, TaskArchiveView

urlpatterns = [
    path('', TaskListTodayView.as_view(), name='main page'),

    path('task/generate', TaskGenView.as_view(), name='task gen'),

    path('task/add', TaskAddView.as_view(), name='task add'),
    re_path(r'^task/done/(?P<task_uuid>[\S]{36})$', TaskDoneView.as_view(), name='task done'),
    re_path(r'^task/update/(?P<task_uuid>[\S]{36})$', TaskUpdateView.as_view(), name='task edit'),
    re_path(r'^task/delete/(?P<task_uuid>[\S]{36})$', TaskDeleteView.as_view(), name='task delete'),

    re_path(r'^task/project/(?P<proj_uuid>[\S]{36})$', TaskListForProjectView.as_view(), name='task delete'),

    path('task/week', TaskListWeekView.as_view(), name='task for week'),
    path('task/archive', TaskArchiveView.as_view(), name='task archive'),
    path('task/all', TaskListView.as_view(), name='task all'),
]
