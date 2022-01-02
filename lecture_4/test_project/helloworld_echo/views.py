from django.http import HttpResponse
import requests
import json
from django.views.decorators.csrf import csrf_exempt
import configparser


def helloworld(request):
    request.session.modified = True
    return HttpResponse('Helloworld')


@csrf_exempt
def tfserving(request):
    print(request.method)
    if request.method == 'POST':
        print('hello')

    # load config
    config = configparser.ConfigParser()
    config.read('helloworld_echo/config.ini')
    ip = config['user-ip']['ip']
    url = 'http://{}:8501/v1/models/serving:predict'.format(ip)

    # url = 'http://192.168.0.16:8501/v1/models/serving:predict'
    data = json.dumps({"instances": [[1.0, 3.0]]})
    ret = requests.post(url, data=data).json()['predictions']

    # msg
    return HttpResponse('return value : {}'.format(ret))
