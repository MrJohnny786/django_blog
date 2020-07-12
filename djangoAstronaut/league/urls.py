
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'league'

urlpatterns = [
    url(r'^$', views.league_games, name='list'),
    url(r'^(?P<g_id>[\w-]+)/$', views.game_details, name='detail'),
]
