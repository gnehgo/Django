import form as form
from django.contrib.auth import get_user_model
from django.http import HttpResponse

import Nba.models as mod

from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render

from .forms import *
from .models import *


def test_link(request):
    return render(request, 'test.html')


def signUp_link(request):
    return render( request, 'registration/signUp.html' )


def signIn_link(request):
    return render(request, 'signIn.html')


def stat_link(request):
    stat_list = mod.Stat.objects.all()
    return render(request, 'stat.html', {"stat_list": stat_list})


def signIn_link(request):
    return render(request, 'signIn.html')


def index(request):
    player_list = mod.Player.objects.all()
    return render(request, 'index.html', {"player_list": player_list})


def games(request):
    game_list = mod.GameStat.objects.all()
    return render(request, 'games.html', {"game_list": game_list})


def login_link(request):
    return render( request, 'registration/login.html' )


def login(request):
    return HttpResponse("Авторизация")


def profile(request):
    return render(request, "registration/../templates/profile.html" )


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    User._meta.get_field('email')._unique = True
    template_name = 'registration/signUp.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(user)
        return redirect('../profile/')

@login_required
def account(request):
    if request.user.is_superuser:
        accounts = get_user_model().objects.all()

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login/'

class Profile(PasswordChangeView):
    form_class = ProfileForm
    template_name = 'registration/profile.html'

def addgame(request):
    if request.method == 'POST':
        form = addGameForm(request.POST)
        if form.is_valid():
            form.save()
    form = addGameForm()
    return render(request, 'addgame.html', {'form': form})
