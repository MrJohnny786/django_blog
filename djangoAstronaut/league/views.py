from django.shortcuts import render
from .models import Game
from django.http import HttpResponse

# Create your views here.
def league_games(request):
    games = Game.objects.all().order_by('date')
    return render(request, 'league/league_games.html', {'games': games})


def game_details(request, g_id):    
    game = Game.objects.get(g_id = g_id)
    return render(request, 'league/game_details.html', {'data': game})