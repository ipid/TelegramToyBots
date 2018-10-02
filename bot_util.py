from bot_api import BotClient
from typing import Callable
from bot_api_objects import Update
import logging

class BotBackend:
    def __init__(self, bot: BotClient):
        self.bot: BotClient = bot

    def poll_message(self):
        bot = self.bot

        logger = logging.getLogger('botLogger')
        offset: int = 0

        while True:
            if offset == 0:
                r = bot.getUpdates(timeout=10)
            else:
                r = bot.getUpdates(timeout=10, offset=offset)

            for update in r:
                try:
                    self.handler(update)
                except KeyboardInterrupt:
                    print("Ctrl+C pressed. The program will exit.")
                    return
                except:
                    logger.exception("Exception when handling update")

                offset = update.update_id + 1

    def handler(self, update: Update):
        pass
