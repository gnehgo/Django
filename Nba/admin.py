from django.contrib import admin

from Nba import models

admin.site.register(models.Player)
admin.site.register(models.Stat)
admin.site.register(models.GameStat)

