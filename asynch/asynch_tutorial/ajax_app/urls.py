from django.urls import path

from ajax_app.views import echo, ajax_test, simple_page

app_name = 'ajax_app'
urlpatterns = [
    path('echo/', echo),
    path('ajax_test/', ajax_test, name='ajax_test'),
    path('simple_page/', simple_page, name='simple_page'),
]
