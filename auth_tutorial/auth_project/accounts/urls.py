# accounts/urls.py
from django.urls import path

from .views import SignUpView, custom_login, only_login, only_pai, signup, only_gold, gold_member_guide, \
    buy_gold_member, change_password, echo

app_name = 'accounts'
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('custom_login/', custom_login, name='custom_login'),
    path('only_login', only_login, name='only_login'),
    path('only_pai', only_pai, name='only_pai'),
    path('only_gold', only_gold, name='only_gold'),
    path('gold_member_guide', gold_member_guide, name='gold_member_guide'),
    path('buy_gold_member', buy_gold_member, name='buy_gold_member'),
    path('change_password', change_password, name='change_password'),
    path('echo', echo, name='echo')
]
