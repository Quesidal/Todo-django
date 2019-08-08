from django.urls import path
from .views import MainView, TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='main page'),
]
