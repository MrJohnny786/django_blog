from django.shortcuts import render, redirect
from .models import Games,Summoners,Participants
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from .tools.main import main
import json

# Create your views here.
def league_games(request):
    return render(request, 'league/league_games.html' )

def post_summoner(request):
    print('XD')
    data = request.POST
    #print(data)
    data= data.dict()
    sum_name  = data.get('summoner_name')
    if not sum_name:
        return render(request, 'league/league_games.html')
    main(str(sum_name))
    #if request.method =='POST':
    #games = Games.objects.all()
    demgames = {}
    summoner = Summoners.objects.filter(name= sum_name)
    _partipants = Participants.objects.all().filter(summonerName=sum_name)
    for x in _partipants:
        riotgameId = x._game.riot_game_id
        _games = Games.objects.all().filter(riot_game_id=riotgameId)
        game_partipants = Participants.objects.all().filter(_game=riotgameId)
        riotgameId = str(riotgameId)
        demgames[riotgameId] = []
        demgames[riotgameId].append(_games)
        demgames[riotgameId].append(game_partipants)
    return render(request, 'league/summoner_details.html',{'summoner': summoner, 'games': demgames})

def find_existing(request):
    print('cs')
    if request.method =='POST':
        print(1)
        data = request.POST
        data= data.dict()
        sum_name  = data.get('summoner_name')
        if not sum_name:
            return render(request, 'league/league_games.html')
        ex_summ = Summoners.objects.all().filter(name=sum_name)
        if ex_summ:
            print('here')
            print(ex_summ, type(ex_summ))
            partipants = Participants.objects.all().filter(summonerName=sum_name)
            print(partipants)
            return redirect('league:find',{'data': ex_summ})
        else:
            return render(request, 'league/league_games.html')
    else:
        return render(request, 'league/league_games.html')




def game_details(request, g_id):
    game = Games.objects.get(g_id = g_id)
    return render(request, 'league/game_details.html', {'data': game})

# @login_required(login_url='/accounts/login/')
# def game_create(request):
#     if request.method =='POST':
#         form = forms.CreateGame(request.POST)
#         if form.is_valid():
#             game_instance = form.save(commit=False)
#             game_instance.author = request.user
#             game_instance.save()
#             return redirect('league:list')
#     else:
#         form = forms.CreateGame()
#     return render(request, 'league/game_create.html', {'form': form})