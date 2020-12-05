from django.db import models
import uuid
#from django.contrib.auth.models import User

# Create your models here.

class Summoners(models.Model):
    _id = models.CharField(max_length=100, default=None)
    accountId = models.CharField(max_length=100, default=None)
    puuid = models.CharField(max_length=100, default=None)
    name = models.CharField(max_length=30, default=None)
    profileIconId = models.IntegerField(default=None)
    summonerLevel = models.IntegerField(default=None)


class Games(models.Model):

    riot_game_id = models.IntegerField(default=None)
    platform_id = models.CharField(max_length=10, default=None)
    queue = models.IntegerField(default=0)
    season = models.IntegerField(default=0)
    timestamp = models.IntegerField(default=0)
    game_duration = models.IntegerField(default=0)
    map = models.IntegerField(default=0)
    gamer = models.ManyToManyField(Summoners)

class Participants(models.Model):
    summonerName = models.CharField(max_length=30, default=None)
    accountId = models.CharField(max_length=100, default=None)
    summonerId = models.CharField(max_length=100, default=None)
    profileIcon = models.IntegerField(default=None)
    participantId = models.IntegerField(default=None)
    teamId = models.IntegerField(default=None)
    championId = models.IntegerField(default=None)
    spell1Id = models.IntegerField(default=None)
    spell2Id = models.IntegerField(default=None)
    win = models.IntegerField(default=None)
    item0 = models.IntegerField(default=None)
    item1 = models.IntegerField(default=None)
    item2 = models.IntegerField(default=None)
    item3 = models.IntegerField(default=None)
    item4 = models.IntegerField(default=None)
    item5 = models.IntegerField(default=None)
    item6 = models.IntegerField(default=None)
    kills = models.IntegerField(default=None)
    deaths = models.IntegerField(default=None)
    assists = models.IntegerField(default=None)
    totalDamageDealtToChampions = models.IntegerField(default=None)
    damageDealtToTurrets = models.IntegerField(default=None)
    visionScore = models.IntegerField(default=None)
    totalDamageTaken = models.IntegerField(default=None)
    visionWardsBoughtInGame = models.IntegerField(default=None)
    _game = models.ManyToManyField(Games)







