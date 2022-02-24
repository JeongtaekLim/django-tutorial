from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def signup(request):
    user = User(username="pai", password='1234', email='tmp@naver.com')
    user.save()
    return HttpResponse('hello')

