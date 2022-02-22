from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from polls.forms import SignUpQuestionerForm
from polls.models import Question, Choice
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "you didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def add_question(request):
    """
    Description:
        question 을 추가합니다.
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'polls/add_question.html')

    else:
        question = request.POST['question_text']
        # save data
        Question.objects.create(question_text=question, pub_date=timezone.now())
        print(Question.objects.all())
        return HttpResponse('hello')


def show_questions(request):
    """
    Description:
        Questions 모든 정보를 보여줍니다.
    """

    querys = Question.objects.all()
    fields = Question._meta.get_fields()

    # db instance 에서 가져 올 수 있는 field 이름 가져오기
    valid_fields = {}
    for field in fields:
        for query in querys:
            try:
                eval('query.{}'.format(field.name))
                valid_fields[str(field.name)] = field.name
            except AttributeError as ae:
                print(ae)

    # 모든 db 을 보여주는 table 만들기
    query_table = []
    for query in querys:
        elements = []
        msg = ''
        for name in valid_fields:
            element = str(eval('query.{}'.format(valid_fields[name])))
            elements.append(str(element))
            msg += str(element)
        query_table.append(elements)
        print(msg)

    return render(request, 'polls/show_questions.html',
                  context={"query_table": query_table, "valid_fields": valid_fields})


def search_questions(request):
    fields = Question._meta.get_fields()
    querys = Question.objects.all()

    # db instance 에서 가져 올 수 있는 field 이름 가져오기
    valid_fields = {}
    for field in fields:
        for query in querys:
            try:
                eval('query.{}'.format(field.name))
                valid_fields[str(field.name)] = field.name
            except AttributeError as ae:
                pass;

    if request.method == 'GET':
        context = {"valid_fields": valid_fields}
        return render(request, 'polls/search_questions.html', context=context)

    elif request.method == 'POST':
        if 'search_word' in request.POST.keys():
            # 입력된 field 와 값에 해당 하는 하나의 instance 을 가져옵니다.
            # html form 에서 field , search_word 란 이름으로 변수를 가져옵니다.
            trgt_field = request.POST["field"]
            trgt_word = request.POST["search_word"]

            # Question DB에서 입력된 row 을 가져옵니다.
            # search_word_result = Question.objects.all().get(**{trgt_field: trgt_word})
            search_word_results = Question.objects.all().filter(**{trgt_field: trgt_word})

            # QuerySet 에서 각 field 이름에 해당 하는 정보를 가져옵니다.
            valid_values_bucket = []
            for search_word_result in search_word_results:
                valid_values = []
                for field in valid_fields:
                    value = getattr(search_word_result, field)
                    valid_values.append(value)
                valid_values_bucket.append(valid_values)

            # 입력 받은 정보를 html page 에 보내줍니다.
            context = {"valid_fields": valid_fields, "search_word_results": search_word_results,
                       "valid_values_bucket": valid_values_bucket}
            return render(request, 'polls/search_questions.html', context=context)

        else:
            result = Question.objects.values(request.POST['select_query'])
            context = {"valid_fields": valid_fields, "result": result}
            return render(request, 'polls/search_questions.html', context=context)
    else:
        raise NotImplementedError


def signup_questioner(request):
    """
    Description:
        질문자를 등록 합니다.
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = SignUpQuestionerForm()
        return render(request, 'polls:signup_questioner.html', {'form': form})

    elif request.method == 'POST':
        pass
    else:
        raise NotImplementedError
