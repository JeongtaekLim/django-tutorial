from django.http import HttpResponse
from django.shortcuts import render
import requests
import json
from django.views.decorators.csrf import csrf_exempt

def helloworld(request):
    print(request)
    return HttpResponse('Helloworld')

@csrf_exempt
def tfserving(request):
    print(request.method)
    if request.method == 'POST':
        print('hello')

    # send msg
    url = 'http://172.20.10.5:8501/v1/models/serving:predict'
    data = json.dumps({"instances": [[1.0, 3.0]]})
    ret = requests.post(url, data=data).json()['predictions']

    # msg
    return HttpResponse('return value : {}'.format(ret))
