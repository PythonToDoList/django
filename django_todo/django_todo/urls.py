"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django_todo.views import snippet_list, ProfileView, Registration
from tasks.views import AllTasks, SingleTasks
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/$', snippet_list, name="info"),
    url(r'^api/v1/accounts/$', Registration.as_view(), name="register"),
    url(
        r'^api/v1/accounts/login/$',
        views.LoginView.as_view(
            template_name='rest_framework/login.html',
        ),
        name='login'
    ),
    url(r'^api/v1/accounts/logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^api/v1/accounts/(?P<username>[\w]+)/$', ProfileView.as_view(), name='profile'),
    url(r'^api/v1/accounts/(?P<username>[\w]+)/tasks', AllTasks.as_view(), name='many_tasks'),
    url(r'^api/v1/accounts/(?P<username>[\w]+)/tasks/(?P<id>[\d]+)', SingleTasks.as_view(), name='one_task')
]
