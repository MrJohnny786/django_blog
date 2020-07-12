
from datetime import datetime

class Unique_Ids(object):
    def __init__(self):
        self.now = int(datetime.now().timestamp())
        self.gameID = None
    def game_id(self, p1, p2):

        self.gameID = ''.join((str(self.now), p1, p2))
        return self.gameID