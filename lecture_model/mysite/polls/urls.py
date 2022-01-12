from django.urls import path
from polls.views import detail, reuslts, vote, index

app_name = 'polls'
urlpatterns = [
    path('<int:question_id>/', detail),
    path('<int:question_id>/results/', reuslts),
    path('<int:question_id>/vote/', vote),
    path('<int:question_id>/details/', detail, name='detail'),
    path('', index, name='index')
]
