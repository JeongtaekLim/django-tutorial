# accounts/urls.py
from django.urls import path

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('custom_login/', custom_login, name='custom_login'),

]
