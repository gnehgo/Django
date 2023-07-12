from django.contrib.auth.views import PasswordChangeView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.contrib import admin
from django.urls import include, path, re_path

import Nba.views as views


class RegisterUser:
    pass


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('test/', views.test_link),
                  path('signUp1/', views.signUp_link),
                  path('signIn/', views.LoginUser.as_view()),
                  path('', views.index),
                  path('stat/', views.stat_link),
                  path('signUp/', views.RegisterUser.as_view()),
                  path('profile/', views.Profile.as_view(), name='profile'),
                  path('accounts/', include("django.contrib.auth.urls")),
                  path('addgame/', views.addgame, name='addgame'),
                  path('games/', views.games)
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
