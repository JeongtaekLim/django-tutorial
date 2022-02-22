from django.urls import path
from polls.views import vote, IndexView, DetailView, ResultsView, add_question, show_questions, search_questions

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('add_question', add_question, name='add_question'),
    path('show_questions', show_questions, name='show_questions'),
    path('search_questions', search_questions, name='search_questions'),

]
