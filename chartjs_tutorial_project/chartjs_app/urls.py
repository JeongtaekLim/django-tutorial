# -*- coding: utf-8 -*-
# @Time    : 2022/03/29 12:20 오전
# @Author  : KimSeong
# @Email   : plznw4me@publicai.co.kr
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from chartjs_app.views import home, async_, ajax_test

app_name = 'chartjs_app'

urlpatterns = [
    path('home', home, name='hone'),
    path('async', async_, name='async'),
    path('ajax_test', ajax_test, name='ajax_test')
]
