from django.urls import path
from polls.views import detail, results, vote, index

app_name = 'polls'
urlpatterns = [
    path('<int:question_id>/', detail),
    path('<int:question_id>/results/', results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('<int:question_id>/detail/', detail, name='detail'),
    path('', index, name='index')
]
