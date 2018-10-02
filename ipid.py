from bot_api import BotClient
from echo_bot import echo_bot
from config import *

if __name__ == '__main__':
    bot = BotClient(IPID_MISC_TOKEN, proxy=PROXY)
    echo_bot(bot)