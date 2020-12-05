import sqlite3
from sqlite3 import Error

class Database(object):
    def __init__(self):
        self.database = r"C:\Users\Johnny786\github\django_blog\db.sqlite3"