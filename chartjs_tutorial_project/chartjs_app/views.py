from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, template_name='chartjs_app/index.html')


def async_(request):
    return render(request, template_name='chartjs_app/async.html')

@csrf_exempt
def ajax_test(request):
    content = render(request, template_name='chartjs_app/index.html').content
    content = content.decode('utf-8')
    data = {'hello': content}
    return JsonResponse(data)
