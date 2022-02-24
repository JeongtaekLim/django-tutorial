# accounts/views.py
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def custom_login(request):
    user = authenticate(username='admin', password='1234')
    return HttpResponse('Done')


def only_login(request):
    if request.user.is_authenticated:
        return HttpResponse('Login user')
    elif request.user.is_authenticated is None:
        return HttpResponse('Not login user')


@login_required
def only_login(request):
    return render(request, template_name='accounts/only_login.html')


def only_pai(request):
    if not request.user.email.endwsith('@publicai.co.kr'):
        return redirect('/login/?next=%s' % request.path)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        result = form.is_valid()
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('home')


    elif request.method == 'GET':
        form = UserCreationForm()
        return render(request, template_name='accounts/signup.html', context={'form': form})

    else:
        raise NotImplementedError
