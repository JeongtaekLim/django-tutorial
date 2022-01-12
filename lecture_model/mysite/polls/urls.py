from django.urls import path
from polls.views import details, reuslts, vote, index

urlpatterns = [
    path('<int:question_id>/', details),
    path('<int:question_id>/results', reuslts),
    path('<int:question_id>/vote', vote),
    path('index/', index)
]
