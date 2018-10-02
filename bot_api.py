from bot_api_objects import *
from bot_api_objects.array_parser import *

from requests import session
from typing import Dict, Any, Union
import json

class BotAPIError(Exception):
    pass

class BaseClient:
    __slots__ = ('token', 'proxy', 'session')

    def __init__(self, token: str, proxy: str) -> None:
        self.token: str = token
        self.proxy: Dict[str, str] = None if proxy == '' else {
            'http': 'http://' + proxy,
            'https': 'http://' + proxy
        }
        self.session = session()

    def call(self, method: str, param: Dict[str, Any]) -> Dict[str, Any]:
        try:
            r = self.session.post(
                f'https://api.telegram.org/bot{self.token}/{method}',
                headers={
                    'Content-Type': 'application/json'
                }, proxies=self.proxy, data=json.dumps(param)
            )
            res = r.json()
        except ValueError:
            raise BotAPIError()

        if res['ok']:
            return res['result']
        else:
            raise BotAPIError()

    # def __getattr__(self, item):
    #     def call_helper(**kwargs):
    #         return self.__call(item, kwargs)
    #
    #     return call_helper

def method_entity(name, cls):
    def call_helper(self, **param):
        return cls(self.call(name, param))

    return call_helper

def method_raw(name):
    def call_helper(self, **param):
        return self.call(name, param)

    return call_helper

def method_array_of_entity(name, cls):
    def call_helper(self, **param):
        return array_of(cls, self.call(name, param))

    return call_helper

class BotClient(BaseClient):
    getUpdates = method_array_of_entity('getUpdates', Update)
    getMe = method_entity('getMe', User)
    sendMessage = method_entity('sendMessage', Message)
    forwardMessage = method_entity('forwardMessage', Message)
    sendPhoto = method_entity('sendPhoto', Message)
    sendAudio = method_entity('sendAudio', Message)
    sendDocument = method_entity('sendDocument', Message)
    sendVideo = method_entity('sendVideo', Message)
    sendAnimation = method_entity('sendAnimation', Message)
    sendVoice = method_entity('sendVoice', Message)
    sendVideoNote = method_entity('sendVideoNote', Message)
    sendMediaGroup = method_array_of_entity('sendMediaGroup', Message)
    sendLocation = method_entity('sendLocation', Message)
    editMessageLiveLocation = method_entity('editMessageLiveLocation', Message)
    stopMessageLiveLocation = method_entity('stopMessageLiveLocation', Message)
    sendVenue = method_entity('sendVenue', Message)
    sendContact = method_entity('sendContact', Message)
    sendChatAction = method_raw('sendChatAction')
    getUserProfilePhotos = method_entity('getUserProfilePhotos', UserProfilePhotos)
    getFile = method_entity('getFile', File)
    kickChatMember = method_raw('kickChatMember')
    unbanChatMember = method_raw('unbanChatMember')
    restrictChatMember = method_raw('restrictChatMember')
    promoteChatMember = method_raw('promoteChatMember')
    exportChatInviteLink = method_raw('exportChatInviteLink')
    setChatPhoto = method_raw('setChatPhoto')
    deleteChatPhoto = method_raw('deleteChatPhoto')
    setChatTitle = method_raw('setChatTitle')
    setChatDescription = method_raw('setChatDescription')
    pinChatMessage = method_raw('pinChatMessage')
    unpinChatMessage = method_raw('unpinChatMessage')
    leaveChat = method_raw('leaveChat')
    getChat = method_entity('getChat', Chat)
    getChatAdministrators = method_array_of_entity('getChatAdministrators', ChatMember)
    getChatMembersCount = method_raw('getChatMembersCount')
    getChatMember = method_entity('getChatMember', ChatMember)
    setChatStickerSet = method_raw('setChatStickerSet')
    deleteChatStickerSet = method_raw('deleteChatStickerSet')
    answerCallbackQuery = method_raw('answerCallbackQuery')
    editMessageText = method_raw('editMessageText')
    editMessageCaption = method_raw('editMessageCaption')
    editMessageMedia = method_raw('editMessageMedia')
    editMessageReplyMarkup = method_raw('editMessageReplyMarkup')
    deleteMessage = method_raw('deleteMessage')
    sendSticker = method_entity('sendSticker', Message)
    getStickerSet = method_entity('getStickerSet', StickerSet)
    uploadStickerFile = method_entity('uploadStickerFile', File)
    createNewStickerSet = method_raw('createNewStickerSet')
    addStickerToSet = method_raw('addStickerToSet')
    setStickerPositionInSet = method_raw('setStickerPositionInSet')
    deleteStickerFromSet = method_raw('deleteStickerFromSet')
    answerInlineQuery = method_raw('answerInlineQuery')