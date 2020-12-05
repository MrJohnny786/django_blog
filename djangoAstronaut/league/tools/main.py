#!/usr/bin/env python3
#from django_blog.djangoAstronaut.league import models
from django.db import models
# from django.conf import settings
# settings.configure(DEBUG=True)
from ..models import Participants, Summoners, Games
from .summoner_request import SummonerConnector
from .match_request import GamesConnector
from requests import Session





def main(name):
    
    summoners_name = name
    session = Session()
    newSummoner = SummonerConnector(session, summoners_name)
    data = newSummoner.connect()
    if not data:
        print('Failed to fetch the summoner :(')
        return False
    # existing_sum = Summoners.objects.all().filter(name=data.get('name'))
    # if existing_sum:
    #     print(existing_sum.json())
    dd = Summoners.objects.update_or_create(
        _id= data.get('id'),
        defaults={
           'accountId':data.get('accountId'), 
            'puuid':data.get('puuid'), 
            'name':data.get('name'), 
            'profileIconId':data.get('profileIconId'), 
            'summonerLevel':data.get('summonerLevel'),
        }
    )

    newGames = GamesConnector(session, data.get('accountId'))
    game_data = newGames.connect()
    if not game_data:
        print('Failed to fetch games  :(')
        return False
    i = 0
    for match in game_data:
        #break
        info = match.get('info')[0]
        gj = Games.objects.all().filter(riot_game_id=info.get('riot_game_id'))
        
        if not gj:
            i=i+1
            g = Games(riot_game_id=info.get('riot_game_id'),
                # defaults={
                platform_id=info.get('platform_id'), 
                queue=info.get('queue'),
                season=info.get('season'), 
                timestamp=info.get('timestamp'),
                game_duration=info.get('game_duration'),
                _map=info.get('_map'),
                #}
            )
            g.save()
            part_c = 0
            for z in match.get('participants'):
                part_c = part_c+1
                for y in z:
                    p = Participants(
                        summonerName=y.get('summonerName'),
                        accountId=y.get('accountId'),
                        profileIcon=100,
                        participantId=y.get('participantId'), 
                        teamId=y.get('teamId'),
                        championId = y.get('championId'),
                        spell1Id=y.get('spell1Id'),
                        spell2Id=y.get('spell2Id'),
                        win=y.get('win'),
                        item0=y.get('item0'),
                        item1=y.get('item1'),
                        item2=y.get('item2'),
                        item3=y.get('item3'),
                        item4=y.get('item4'),
                        item5=y.get('item5'),
                        item6=y.get('item6'),
                        kills=y.get('kills'),
                        deaths=y.get('deaths'),
                        assists=y.get('assists'),
                        totalDamageDealtToChampions=y.get('totalDamageDealtToChampions'),
                        damageDealtToTurrets=y.get('damageDealtToTurrets'),
                        visionScore=y.get('visionScore'),
                        totalDamageTaken=y.get('totalDamageTaken'),
                        visionWardsBoughtInGame=y.get('visionWardsBoughtInGame'),
                        _game  = g,
                    )
                    p.save()
        else:
            continue
        
    return True

