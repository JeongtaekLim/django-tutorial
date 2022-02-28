# -*- coding: utf-8 -*-
# @Time    : 2022/02/25 12:02 오전
# @Author  : KimSeong
# @Email   : plznw4me@publicai.co.kr
# @File    : forms.py
# @Software: PyCharm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import CustomUser
from django import forms


# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(max_length=200)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', "password1", "password2")

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    region = forms.CharField()
    phone_number = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'region')
