from requests import Session
import datetime

import environ

# class ConnectorHelper(object):
#     def __init__(self):
#         env = environ.Env()
#         environ.Env.read_env()
#         self.key = env('RIOT_API_KEY')


class SummonerConnector(object):
    def __init__(self, session, summoner_name):
        env = environ.Env()
        environ.Env.read_env()
        self.key = env('RIOT_API_KEY')
        self.name =  summoner_name #'pyiV18OSLznLgZg4Uh7gjjrRWc1_YuINJ3IW0hk4fgsEqw'
        self.url = f'https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.name}'
        self.session = session
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9,el;q=0.8",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://developer.riotgames.com",
            "X-Riot-Token": self.key
        }
        self.params = {
            "api_key": self.key,
        }


    def connect(self):
        response = self.session.get(self.url, headers = self.headers, params=self.params, )
        if not response.ok:
            return False
        
        info = response.json()        

        return info