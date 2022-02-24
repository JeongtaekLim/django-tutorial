from django.urls import path
from auth_app1.views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
]
