from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def echo(request):
    if request.type == 'GET':
        msg = 'helloworld'
    elif request.type == 'POST':
        msg = 'helloworld'
    else:
        raise NotImplementedError
    return HttpResponse(msg)
