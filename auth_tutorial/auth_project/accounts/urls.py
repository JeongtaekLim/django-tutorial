# accounts/urls.py
from django.urls import path

from .views import SignUpView, custom_login, only_login, only_pai, signup

app_name = 'accounts'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('custom_login/', custom_login, name='custom_login'),
    path('only_login', only_login, name='only_login'),
    path('only_pai', only_pai, name='only_pai'),
]
