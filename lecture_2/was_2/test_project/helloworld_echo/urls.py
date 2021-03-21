from django.urls import path
from . import views

urlpatterns = [
    path('helloworld', views.helloworld, name='helloworld'),
    path('tfserving', views.tfserving, name='tfserving'),
]

