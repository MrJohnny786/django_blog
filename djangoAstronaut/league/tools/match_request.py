#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from requests import Session
import datetime

import environ
# from crontab import CronTab
# cron = CronTab()
# job = cron.new(print('echo hello_world'))
# job.minute.every(1)


class GamesConnector(object):
    def __init__(self, session, account_id):
        env = environ.Env()
        environ.Env.read_env()
        self.key = env('RIOT_API_KEY')
        self.account_id = account_id  # 'pyiV18OSLznLgZg4Uh7gjjrRWc1_YuINJ3IW0hk4fgsEqw'

        self.url = f'https://eun1.api.riotgames.com/lol/match/v4/matchlists/by-account/{self.account_id}'
        self.session = session
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9,el;q=0.8",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token": self.key
        }
        self.params = {
            "key": self.key,
        }
        self.ids = []

    def game_connect(self, game_id):
        self.game_id = game_id
        gameurl = f'https://eun1.api.riotgames.com/lol/match/v4/matches/{self.game_id}'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9,el;q=0.8",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token": self.key
        }
        response = self.session.get(
            gameurl, headers=self.headers, params=self.params, )
        if not response.ok:
            return False

        endgame = {
            'info': [],
            'participants': [],
        }
        one_game = response.json()

        info = {
            'riot_game_id': self.game_id,
            'platform_id': one_game.get('platformId'),
            'queue': one_game.get('queueId'),
            'season': one_game.get('seasonId'),
            'timestamp': one_game.get('gameCreation'),
            'game_duration': one_game.get('gameDuration'),
            '_map': one_game.get('mapId'),
        }
        identities = []
        personalities = []
        for x in one_game.get('participantIdentities'):
            player = {
                '_id': None,
                'name': None,
                'accountId': None
            }
            player['_id'] = x.get('participantId')
            pl = x.get('player')
            player['name'] = pl.get('summonerName')
            player['accountId'] = pl.get('accountId')
            identities.append(player)

        part = one_game.get('participants')
        for k, k2 in zip(part, identities):
            if k.get('stats').get('participantId') == k2.get('_id'):
                stats = k.get('stats')
                participant = {
                    'summonerName': k2.get('name'),
                    'accountId': k2.get('accountId'),
                    'summonerId': 8,
                    'participantId': k2.get('_id'),
                    'teamId': k.get('teamId'),
                    'championId': k.get('championId'),
                    'spell1Id': k.get('spell1Id'),
                    'spell2Id': k.get('spell2Id'),
                    'win': stats.get('win'),
                    'item0': stats.get('item0'),
                    'item1': stats.get('item1'),
                    'item2': stats.get('item2'),
                    'item3': stats.get('item3'),
                    'item4': stats.get('item4'),
                    'item5': stats.get('item5'),
                    'item6': stats.get('item6'),
                    'kills': stats.get('kills'),
                    'deaths': stats.get('deaths'),
                    'assists': stats.get('assists'),
                    'totalDamageDealtToChampions': stats.get('totalDamageDealtToChampions'),
                    'damageDealtToTurrets': stats.get('damageDealtToTurrets'),
                    'visionScore': stats.get('visionScore'),
                    'totalDamageTaken': stats.get('totalDamageTaken'),
                    'visionWardsBoughtInGame': stats.get('visionWardsBoughtInGame'),
                }
                personalities.append(participant)

        endgame['info'].append(info)
        endgame['participants'].append(personalities)

        return endgame

    def connect(self):
        response = self.session.get(
            self.url, headers=self.headers, params=self.params, )
        if not response.ok:
            return False
        matches = response.json().get('matches')
        matches = matches[:5]
        full_info = []

        for match in matches:
            match_id = match.get('gameId')
            gameinfo = self.game_connect(match_id)
            full_info.append(gameinfo)

        return full_info
