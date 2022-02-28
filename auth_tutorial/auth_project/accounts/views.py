# accounts/views.py
from django.contrib import auth
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import CustomUserCreationForm
from django.contrib.contenttypes.models import ContentType

from accounts.models import GoldUser


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
        form = CustomUserCreationForm(request.POST)
        result = form.is_valid()
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, template_name='accounts/signup.html', context={'errors': form.errors})

    elif request.method == 'GET':
        form = CustomUserCreationForm()
        return render(request, template_name='accounts/signup.html', context={'form': form})

    else:
        raise NotImplementedError


@login_required
@permission_required('accounts.gold_member', login_url=reverse_lazy('accounts:gold_member_guide'))
def only_gold(request):
    return HttpResponse('Welcome gold member(호갱)')


def gold_member_guide(request):
    return HttpResponse('Gold 회원이 되면 좋은점. 1. 꽁짜 커피 ')


@login_required
def buy_gold_member(request):
    user = get_user_model().objects.get(username=request.user)
    content_type = ContentType.objects.get_for_model(GoldUser)
    perm = Permission.objects.get(codename='gold_member', content_type=content_type)
    user.user_permissions.add(perm)
    return HttpResponse("Now {} got gold member".format(request.user))
