from django.urls import path
from polls.views import vote, IndexView, DetailView, ResultsView

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', ResultsView.as_view()),
    path('<int:question_id>/vote/', vote, name='vote'),
]
