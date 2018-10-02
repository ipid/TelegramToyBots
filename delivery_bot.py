from bot_api import BotClient
from bot_util import BotBackend
from bot_api_objects import *
from typing import Generator
import sqlite3

def initialize_database():
    sql = sqlite3.connect('delivery.sqlite')
    c = sql.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users(
        user integer no/t null default 0,
        chat integer not null default 0,
        state integer not null default 0
    )''')

def user_session():


class DeliveryBot(BotBackend):
    def __init__(self, bot: BotClient):
        self.bot: BotClient = bot
        self.sql = sqlite3.connect('delivery.sqlite')

    def load_user_state(self, user: User) -> int:
        pass

    def store_user_state(self, user: User, state: int):
        pass

    def register_user(self, user: User, chat: Chat):
        pass

    def handler(self, update: Update):
        pass

if __name__ == '__main__':
    initialize_database()

