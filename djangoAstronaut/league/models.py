from django.db import models
from .id_creation import Unique_Ids
import uuid

# Create your models here.
class Game(models.Model):
    
    #new_game_id = Unique_Ids()

    games_types = [
        ('Ranked solo duo', 'ranked_sd'),
        ('Ranked flex','flex'),
        ('Normal', 'normal'),
        ('Draft', 'draft'),
        ('Aram', 'aram'),  
    ]
    date = models.DateTimeField(auto_now_add=True)
    kda_p1 = models.CharField(max_length=30, default='0/0/0')
    kda_p2 = models.CharField(max_length=30, default='0/0/0')
    player1 = models.CharField(max_length=30)
    player2 = models.CharField(max_length=30)
    p1_damage = models.IntegerField()
    p2_damage = models.IntegerField()
    p1_wins = models.IntegerField()
    p2_wins = models.IntegerField()
    champion_name_p1 = models.CharField(max_length=30)
    champion_name_p2 = models.CharField(max_length=30)
    game_type = models.CharField(
        choices=games_types,
        default='Unknown',
        max_length=30
    )
    g_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.game_type
