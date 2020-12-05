
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from .tools import main

app_name = 'league'



urlpatterns = [
    url(r'^$', views.league_games, name='list'),
    url(r'^add/$', views.post_summoner, name='create'),
    #url(r'^(?P<g_id>[\w-]+)/$', views.game_details, name='detail'),
    url(r'^find/$', views.find_existing, name= 'find')
]
