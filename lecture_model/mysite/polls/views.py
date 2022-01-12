from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from polls.models import Question


@csrf_exempt
def helloworld(request, **kwargs):
    print(kwargs)
    return HttpResponse('helloworld')


@csrf_exempt
def details(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def reuslts(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


@csrf_exempt
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))