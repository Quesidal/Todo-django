from django.urls import path, include, re_path
from .views import TaskListView, SignInView, TaskAddView, TaskGenView, TaskDeleteView, TaskUpdateView, TaskDoneView

urlpatterns = [
    path('', TaskListView.as_view(), name='main page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signin', SignInView.as_view(), name='sign in'),

    path('task/add', TaskAddView.as_view(), name='task add'),

    path('task/generate', TaskGenView.as_view(), name='task gen'),

    re_path(r'^task/done/(?P<uuid>[\S]{36})$', TaskDoneView.as_view(), name='task done'),
    re_path(r'^task/update/(?P<uuid>[\S]{36})$', TaskUpdateView.as_view(), name='task edit'),
    re_path(r'^task/delete/(?P<uuid>[\S]{36})$', TaskDeleteView.as_view(), name='task delete'),
]
