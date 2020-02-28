from django.urls import path

from . import views

urlpatterns = [
    path('help/', views.help, name='help'),
    path('users/', views.users, name='users'),
    path('signup/', views.signup, name='signup')
]
