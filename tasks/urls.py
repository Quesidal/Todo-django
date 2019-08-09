from django.urls import path, include, re_path
from .views import TaskList, SignInView, TaskAddView, TaskGenView, TaskDeleteView

urlpatterns = [
    path('', TaskList.as_view(), name='main page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signin', SignInView.as_view(), name='sign in'),

    path('task/add', TaskAddView.as_view(), name='task add'),
    path('task/generate', TaskGenView.as_view(), name='task gen'),

    re_path(r'^task/delete/(?P<uuid>[\S]{36})$', TaskDeleteView.as_view()),
]
