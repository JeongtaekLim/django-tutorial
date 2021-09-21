from django.urls import path, include
from . import views

urlpatterns = [
    path('helloworld', views.helloworld, name='helloworld'),
    path('auth_check', views.auth_check, name='auth_check'),
    path('tfserving', views.tfserving, name='tfserving'),
]

