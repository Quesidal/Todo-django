from django.urls import path, include
from .views import TaskList, SignInView

urlpatterns = [
    path('', TaskList.as_view(), name='main page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signin', SignInView.as_view(), name='sign in'),
    path('task/crate', ),

]
