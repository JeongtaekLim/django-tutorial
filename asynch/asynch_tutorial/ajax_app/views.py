import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def echo(request):
    return JsonResponse({"instance": 'hello ajax'}, status=200)


@csrf_exempt
def ajax_test(request):
    if request.method == 'POST':
        data = {"hello" : "'Hello Ajax' from server"}
        return JsonResponse(data)


def simple_page(request):
    if request.method == 'GET':
        return render(request, 'ajax_app/simple_page.html')
