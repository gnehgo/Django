from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from Nba.models import *


class RegisterUserForm( UserCreationForm ):
    username = forms.CharField( label='Логин',
                                widget=forms.TextInput( attrs={'class': 'form-input', 'placeholder': 'Username'} ) )
    email = forms.CharField( label='Email', widget=forms.TextInput( attrs={'placeholder': 'Email'} ) )
    password1 = forms.CharField( label='Пароль', widget=forms.PasswordInput() )
    password2 = forms.CharField( label='Повтор пароля', widget=forms.PasswordInput() )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm( AuthenticationForm ):
    username = forms.CharField( label='Логин',
                                widget=forms.TextInput( attrs={'class': 'form-input', 'placeholder': 'Username'} ) )
    password = forms.CharField( label='Пароль', widget=forms.PasswordInput() )
    error_messages = {
        'invalid_login': _(
            "Неверный пароль"
        )}


class ProfileForm( PasswordChangeForm ):
    old_password = forms.CharField( label='Старый пароль', widget=forms.PasswordInput( attrs={'class': 'form-input'} ) )
    new_password1 = forms.CharField( label='Новый пароль', widget=forms.PasswordInput( attrs={'class': 'form-input'} ) )
    new_password2 = forms.CharField( label='Повтор пароля',
                                     widget=forms.PasswordInput( attrs={'class': 'form-input'} ) )


class addGameForm(ModelForm):
        data = forms.DateField( label='Date', widget=forms.SelectDateWidget)
        class Meta:
            model = GameStat
            fields = ['data', 'team1', 'team2', 'score']


