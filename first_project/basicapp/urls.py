from django.urls import path, re_path

from . import views

app_name = 'basicapp'

urlpatterns = [
    path('', views.index, name='index'),
    re_path('^relative/$', views.relative, name='relative'),
    re_path('^other/$', views.other, name='other'),
]
