from typing import Dict, Any, List, Optional
from .array_parser import *

class TelegramObject:
    pass

class Update(TelegramObject):
    __slots__ = ('update_id', 'message', 'edited_message', 'channel_post', 'edited_channel_post', 'inline_query', 'chosen_inline_result', 'callback_query', 'shipping_query', 'pre_checkout_query')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.update_id: Optional[int] = params.get('update_id') if 'update_id' in params else None
        self.message: Optional[Message] = Message(params.get('message')) if 'message' in params else None
        self.edited_message: Optional[Message] = Message(params.get('edited_message')) if 'edited_message' in params else None
        self.channel_post: Optional[Message] = Message(params.get('channel_post')) if 'channel_post' in params else None
        self.edited_channel_post: Optional[Message] = Message(params.get('edited_channel_post')) if 'edited_channel_post' in params else None
        self.inline_query: Optional[InlineQuery] = InlineQuery(params.get('inline_query')) if 'inline_query' in params else None
        self.chosen_inline_result: Optional[ChosenInlineResult] = ChosenInlineResult(params.get('chosen_inline_result')) if 'chosen_inline_result' in params else None
        self.callback_query: Optional[CallbackQuery] = CallbackQuery(params.get('callback_query')) if 'callback_query' in params else None
        self.shipping_query: Optional[ShippingQuery] = ShippingQuery(params.get('shipping_query')) if 'shipping_query' in params else None
        self.pre_checkout_query: Optional[PreCheckoutQuery] = PreCheckoutQuery(params.get('pre_checkout_query')) if 'pre_checkout_query' in params else None

class WebhookInfo(TelegramObject):
    __slots__ = ('url', 'has_custom_certificate', 'pending_update_count', 'last_error_date', 'last_error_message', 'max_connections', 'allowed_updates')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.url: Optional[str] = params.get('url') if 'url' in params else None
        self.has_custom_certificate: Optional[bool] = params.get('has_custom_certificate') if 'has_custom_certificate' in params else None
        self.pending_update_count: Optional[int] = params.get('pending_update_count') if 'pending_update_count' in params else None
        self.last_error_date: Optional[int] = params.get('last_error_date') if 'last_error_date' in params else None
        self.last_error_message: Optional[str] = params.get('last_error_message') if 'last_error_message' in params else None
        self.max_connections: Optional[int] = params.get('max_connections') if 'max_connections' in params else None
        self.allowed_updates: Optional[List[str]] = params.get('allowed_updates') if 'allowed_updates' in params else None

class User(TelegramObject):
    __slots__ = ('id', 'is_bot', 'first_name', 'last_name', 'username', 'language_code')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.id: Optional[int] = params.get('id') if 'id' in params else None
        self.is_bot: Optional[bool] = params.get('is_bot') if 'is_bot' in params else None
        self.first_name: Optional[str] = params.get('first_name') if 'first_name' in params else None
        self.last_name: Optional[str] = params.get('last_name') if 'last_name' in params else None
        self.username: Optional[str] = params.get('username') if 'username' in params else None
        self.language_code: Optional[str] = params.get('language_code') if 'language_code' in params else None

class Chat(TelegramObject):
    __slots__ = ('id', 'type', 'title', 'username', 'first_name', 'last_name', 'all_members_are_administrators', 'photo', 'description', 'invite_link', 'pinned_message', 'sticker_set_name', 'can_set_sticker_set')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.id: Optional[int] = params.get('id') if 'id' in params else None
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.title: Optional[str] = params.get('title') if 'title' in params else None
        self.username: Optional[str] = params.get('username') if 'username' in params else None
        self.first_name: Optional[str] = params.get('first_name') if 'first_name' in params else None
        self.last_name: Optional[str] = params.get('last_name') if 'last_name' in params else None
        self.all_members_are_administrators: Optional[bool] = params.get('all_members_are_administrators') if 'all_members_are_administrators' in params else None
        self.photo: Optional[ChatPhoto] = ChatPhoto(params.get('photo')) if 'photo' in params else None
        self.description: Optional[str] = params.get('description') if 'description' in params else None
        self.invite_link: Optional[str] = params.get('invite_link') if 'invite_link' in params else None
        self.pinned_message: Optional[Message] = Message(params.get('pinned_message')) if 'pinned_message' in params else None
        self.sticker_set_name: Optional[str] = params.get('sticker_set_name') if 'sticker_set_name' in params else None
        self.can_set_sticker_set: Optional[bool] = params.get('can_set_sticker_set') if 'can_set_sticker_set' in params else None

class Message(TelegramObject):
    __slots__ = ('message_id', 'from_user', 'date', 'chat', 'forward_from', 'forward_from_chat', 'forward_from_message_id', 'forward_signature', 'forward_date', 'reply_to_message', 'edit_date', 'media_group_id', 'author_signature', 'text', 'entities', 'caption_entities', 'audio', 'document', 'animation', 'game', 'photo', 'sticker', 'video', 'voice', 'video_note', 'caption', 'contact', 'location', 'venue', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id', 'pinned_message', 'invoice', 'successful_payment', 'connected_website', 'passport_data')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.message_id: Optional[int] = params.get('message_id') if 'message_id' in params else None
        self.from_user: Optional[User] = User(params.get('from')) if 'from' in params else None
        self.date: Optional[int] = params.get('date') if 'date' in params else None
        self.chat: Optional[Chat] = Chat(params.get('chat')) if 'chat' in params else None
        self.forward_from: Optional[User] = User(params.get('forward_from')) if 'forward_from' in params else None
        self.forward_from_chat: Optional[Chat] = Chat(params.get('forward_from_chat')) if 'forward_from_chat' in params else None
        self.forward_from_message_id: Optional[int] = params.get('forward_from_message_id') if 'forward_from_message_id' in params else None
        self.forward_signature: Optional[str] = params.get('forward_signature') if 'forward_signature' in params else None
        self.forward_date: Optional[int] = params.get('forward_date') if 'forward_date' in params else None
        self.reply_to_message: Optional[Message] = Message(params.get('reply_to_message')) if 'reply_to_message' in params else None
        self.edit_date: Optional[int] = params.get('edit_date') if 'edit_date' in params else None
        self.media_group_id: Optional[str] = params.get('media_group_id') if 'media_group_id' in params else None
        self.author_signature: Optional[str] = params.get('author_signature') if 'author_signature' in params else None
        self.text: Optional[str] = params.get('text') if 'text' in params else None
        self.entities: Optional[List[MessageEntity]] = array_of(MessageEntity, params.get('entities')) if 'entities' in params else None
        self.caption_entities: Optional[List[MessageEntity]] = array_of(MessageEntity, params.get('caption_entities')) if 'caption_entities' in params else None
        self.audio: Optional[Audio] = Audio(params.get('audio')) if 'audio' in params else None
        self.document: Optional[Document] = Document(params.get('document')) if 'document' in params else None
        self.animation: Optional[Animation] = Animation(params.get('animation')) if 'animation' in params else None
        self.game: Optional[Game] = Game(params.get('game')) if 'game' in params else None
        self.photo: Optional[List[PhotoSize]] = array_of(PhotoSize, params.get('photo')) if 'photo' in params else None
        self.sticker: Optional[Sticker] = Sticker(params.get('sticker')) if 'sticker' in params else None
        self.video: Optional[Video] = Video(params.get('video')) if 'video' in params else None
        self.voice: Optional[Voice] = Voice(params.get('voice')) if 'voice' in params else None
        self.video_note: Optional[VideoNote] = VideoNote(params.get('video_note')) if 'video_note' in params else None
        self.caption: Optional[str] = params.get('caption') if 'caption' in params else None
        self.contact: Optional[Contact] = Contact(params.get('contact')) if 'contact' in params else None
        self.location: Optional[Location] = Location(params.get('location')) if 'location' in params else None
        self.venue: Optional[Venue] = Venue(params.get('venue')) if 'venue' in params else None
        self.new_chat_members: Optional[List[User]] = array_of(User, params.get('new_chat_members')) if 'new_chat_members' in params else None
        self.left_chat_member: Optional[User] = User(params.get('left_chat_member')) if 'left_chat_member' in params else None
        self.new_chat_title: Optional[str] = params.get('new_chat_title') if 'new_chat_title' in params else None
        self.new_chat_photo: Optional[List[PhotoSize]] = array_of(PhotoSize, params.get('new_chat_photo')) if 'new_chat_photo' in params else None
        self.delete_chat_photo: Optional[bool] = params.get('delete_chat_photo') if 'delete_chat_photo' in params else None
        self.group_chat_created: Optional[bool] = params.get('group_chat_created') if 'group_chat_created' in params else None
        self.supergroup_chat_created: Optional[bool] = params.get('supergroup_chat_created') if 'supergroup_chat_created' in params else None
        self.channel_chat_created: Optional[bool] = params.get('channel_chat_created') if 'channel_chat_created' in params else None
        self.migrate_to_chat_id: Optional[int] = params.get('migrate_to_chat_id') if 'migrate_to_chat_id' in params else None
        self.migrate_from_chat_id: Optional[int] = params.get('migrate_from_chat_id') if 'migrate_from_chat_id' in params else None
        self.pinned_message: Optional[Message] = Message(params.get('pinned_message')) if 'pinned_message' in params else None
        self.invoice: Optional[Invoice] = Invoice(params.get('invoice')) if 'invoice' in params else None
        self.successful_payment: Optional[SuccessfulPayment] = SuccessfulPayment(params.get('successful_payment')) if 'successful_payment' in params else None
        self.connected_website: Optional[str] = params.get('connected_website') if 'connected_website' in params else None
        self.passport_data: Optional[PassportData] = PassportData(params.get('passport_data')) if 'passport_data' in params else None

class MessageEntity(TelegramObject):
    __slots__ = ('type', 'offset', 'length', 'url', 'user')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.offset: Optional[int] = params.get('offset') if 'offset' in params else None
        self.length: Optional[int] = params.get('length') if 'length' in params else None
        self.url: Optional[str] = params.get('url') if 'url' in params else None
        self.user: Optional[User] = User(params.get('user')) if 'user' in params else None

class PhotoSize(TelegramObject):
    __slots__ = ('file_id', 'width', 'height', 'file_size')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.file_id: Optional[str] = params.get('file_id') if 'file_id' in params else None
        self.width: Optional[int] = params.get('width') if 'width' in params else None
        self.height: Optional[int] = params.get('height') if 'height' in params else None
        self.file_size: Optional[int] = params.get('file_size') if 'file_size' in params else None

class Audio(TelegramObject):
    __slots__ = ('file_id', 'duration', 'performer', 'title', 'mime_type', 'file_size', 'thumb')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.file_id: Optional[str] = params.get('file_id') if 'file_id' in params else None
        self.duration: Optional[int] = params.get('duration') if 'duration' in params else None
        self.performer: Optional[str] = params.get('performer') if 'performer' in params else None
        self.title: Optional[str] = params.get('title') if 'title' in params else None
        self.mime_type: Optional[str] = params.get('mime_type') if 'mime_type' in params else None
        self.file_size: Optional[int] = params.get('file_size') if 'file_size' in params else None
        self.thumb: Optional[PhotoSize] = PhotoSize(params.get('thumb')) if 'thumb' in params else None

class Document(TelegramObject):
    __slots__ = ('file_id', 'thumb', 'file_name', 'mime_type', 'file_size')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.file_id: Optional[str] = params.get('file_id') if 'file_id' in params else None
        self.thumb: Optional[PhotoSize] = PhotoSize(params.get('thumb')) if 'thumb' in params else None
        self.file_name: Optional[str] = params.get('file_name') if 'file_name' in params else None
        self.mime_type: Optional[str] = params.get('mime_type') if 'mime_type' in params else None
        self.file_size: Optional[int] = params.get('file_size') if 'file_size' in params else None

class Video(TelegramObject):
    __slots__ = ('file_id', 'width', 'height', 'duration', 'thumb', 'mime_type', 'file_size')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.file_id: Optional[str] = params.get('file_id') if 'file_id' in params else None
        self.width: Optional[int] = params.get('width') if 'width' in params else None
        self.height: Optional[int] = params.get('height') if 'height' in params else None
        self.duration: Optional[int] = params.get('duration') if 'duration' in params else None
        self.thumb: Optional[PhotoSize] = PhotoSize(params.get('thumb')) if 'thumb' in params else None
        self.mime_type: Optional[str] = params.get('mime_type') if 'mime_type' in params else None
        self.file_size: Optional[int] = params.get('file_size') if 'file_size' in params else None

class Animation(TelegramObject):
    __slots__ = ('file_id', 'width', 'height', 'duration', 'thumb', 'file_name', 'mime_type', 'file_size')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.file_id: Optional[str] = params.get('file_id') if 'file_id' in params else None
        self.width: Optional[int] = params.get('width') if 'width' in params else None
        self.height: Optional[int] = params.get('height') if 'height' in params else None
        self.duration: Optional[int] = params.get('duration') if 'duration' in params else None
        self.thumb: Optional[PhotoSize] = PhotoSize(params.get('thumb')) if 'thumb' in params else None
        self.file_name: Optional[str] = params.get('file_name') if 'file_name' in params else None
        self.mime_type: Optional[str] = params.get('mime_type') if 'mime_type' in params else None
        self.file_size: Optional[int] = params.get('file_size') if 'file_size' in params else None

class Voice(TelegramObject):
    __slots__ = ('file_id', 'duration', 'mime_type', 'file_size')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.file_id: Optional[str] = params.get('file_id') if 'file_id' in params else None
        self.duration: Optional[int] = params.get('duration') if 'duration' in params else None
        self.mime_type: Optional[str] = params.get('mime_type') if 'mime_type' in params else None
        self.file_size: Optional[int] = params.get('file_size') if 'file_size' in params else None

class VideoNote(TelegramObject):
    __slots__ = ('file_id', 'length', 'duration', 'thumb', 'file_size')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.file_id: Optional[str] = params.get('file_id') if 'file_id' in params else None
        self.length: Optional[int] = params.get('length') if 'length' in params else None
        self.duration: Optional[int] = params.get('duration') if 'duration' in params else None
        self.thumb: Optional[PhotoSize] = PhotoSize(params.get('thumb')) if 'thumb' in params else None
        self.file_size: Optional[int] = params.get('file_size') if 'file_size' in params else None

class Contact(TelegramObject):
    __slots__ = ('phone_number', 'first_name', 'last_name', 'user_id', 'vcard')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.phone_number: Optional[str] = params.get('phone_number') if 'phone_number' in params else None
        self.first_name: Optional[str] = params.get('first_name') if 'first_name' in params else None
        self.last_name: Optional[str] = params.get('last_name') if 'last_name' in params else None
        self.user_id: Optional[int] = params.get('user_id') if 'user_id' in params else None
        self.vcard: Optional[str] = params.get('vcard') if 'vcard' in params else None

class Location(TelegramObject):
    __slots__ = ('longitude', 'latitude')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.longitude: Optional[float] = params.get('longitude') if 'longitude' in params else None
        self.latitude: Optional[float] = params.get('latitude') if 'latitude' in params else None

class Venue(TelegramObject):
    __slots__ = ('location', 'title', 'address', 'foursquare_id', 'foursquare_type')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.location: Optional[Location] = Location(params.get('location')) if 'location' in params else None
        self.title: Optional[str] = params.get('title') if 'title' in params else None
        self.address: Optional[str] = params.get('address') if 'address' in params else None
        self.foursquare_id: Optional[str] = params.get('foursquare_id') if 'foursquare_id' in params else None
        self.foursquare_type: Optional[str] = params.get('foursquare_type') if 'foursquare_type' in params else None

class UserProfilePhotos(TelegramObject):
    __slots__ = ('total_count', 'photos')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.total_count: Optional[int] = params.get('total_count') if 'total_count' in params else None
        self.photos: Optional[List[List[PhotoSize]]] = array_of_array_of(PhotoSize, params.get('photos')) if 'photos' in params else None

class File(TelegramObject):
    __slots__ = ('file_id', 'file_size', 'file_path')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.file_id: Optional[str] = params.get('file_id') if 'file_id' in params else None
        self.file_size: Optional[int] = params.get('file_size') if 'file_size' in params else None
        self.file_path: Optional[str] = params.get('file_path') if 'file_path' in params else None

class ReplyKeyboardMarkup(TelegramObject):
    __slots__ = ('keyboard', 'resize_keyboard', 'one_time_keyboard', 'selective')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.keyboard: Optional[List[List[KeyboardButton]]] = array_of_array_of(KeyboardButton, params.get('keyboard')) if 'keyboard' in params else None
        self.resize_keyboard: Optional[bool] = params.get('resize_keyboard') if 'resize_keyboard' in params else None
        self.one_time_keyboard: Optional[bool] = params.get('one_time_keyboard') if 'one_time_keyboard' in params else None
        self.selective: Optional[bool] = params.get('selective') if 'selective' in params else None

class KeyboardButton(TelegramObject):
    __slots__ = ('text', 'request_contact', 'request_location')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.text: Optional[str] = params.get('text') if 'text' in params else None
        self.request_contact: Optional[bool] = params.get('request_contact') if 'request_contact' in params else None
        self.request_location: Optional[bool] = params.get('request_location') if 'request_location' in params else None

class ReplyKeyboardRemove(TelegramObject):
    __slots__ = ('remove_keyboard', 'selective')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.remove_keyboard: Optional[bool] = params.get('remove_keyboard') if 'remove_keyboard' in params else None
        self.selective: Optional[bool] = params.get('selective') if 'selective' in params else None

class CallbackQuery(TelegramObject):
    __slots__ = ('id', 'from_user', 'message', 'inline_message_id', 'chat_instance', 'data', 'game_short_name')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.id: Optional[str] = params.get('id') if 'id' in params else None
        self.from_user: Optional[User] = User(params.get('from')) if 'from' in params else None
        self.message: Optional[Message] = Message(params.get('message')) if 'message' in params else None
        self.inline_message_id: Optional[str] = params.get('inline_message_id') if 'inline_message_id' in params else None
        self.chat_instance: Optional[str] = params.get('chat_instance') if 'chat_instance' in params else None
        self.data: Optional[str] = params.get('data') if 'data' in params else None
        self.game_short_name: Optional[str] = params.get('game_short_name') if 'game_short_name' in params else None

class ForceReply(TelegramObject):
    __slots__ = ('force_reply', 'selective')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.force_reply: Optional[bool] = params.get('force_reply') if 'force_reply' in params else None
        self.selective: Optional[bool] = params.get('selective') if 'selective' in params else None

class ChatPhoto(TelegramObject):
    __slots__ = ('small_file_id', 'big_file_id')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.small_file_id: Optional[str] = params.get('small_file_id') if 'small_file_id' in params else None
        self.big_file_id: Optional[str] = params.get('big_file_id') if 'big_file_id' in params else None

class ChatMember(TelegramObject):
    __slots__ = ('user', 'status', 'until_date', 'can_be_edited', 'can_change_info', 'can_post_messages', 'can_edit_messages', 'can_delete_messages', 'can_invite_users', 'can_restrict_members', 'can_pin_messages', 'can_promote_members', 'can_send_messages', 'can_send_media_messages', 'can_send_other_messages', 'can_add_web_page_previews')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.user: Optional[User] = User(params.get('user')) if 'user' in params else None
        self.status: Optional[str] = params.get('status') if 'status' in params else None
        self.until_date: Optional[int] = params.get('until_date') if 'until_date' in params else None
        self.can_be_edited: Optional[bool] = params.get('can_be_edited') if 'can_be_edited' in params else None
        self.can_change_info: Optional[bool] = params.get('can_change_info') if 'can_change_info' in params else None
        self.can_post_messages: Optional[bool] = params.get('can_post_messages') if 'can_post_messages' in params else None
        self.can_edit_messages: Optional[bool] = params.get('can_edit_messages') if 'can_edit_messages' in params else None
        self.can_delete_messages: Optional[bool] = params.get('can_delete_messages') if 'can_delete_messages' in params else None
        self.can_invite_users: Optional[bool] = params.get('can_invite_users') if 'can_invite_users' in params else None
        self.can_restrict_members: Optional[bool] = params.get('can_restrict_members') if 'can_restrict_members' in params else None
        self.can_pin_messages: Optional[bool] = params.get('can_pin_messages') if 'can_pin_messages' in params else None
        self.can_promote_members: Optional[bool] = params.get('can_promote_members') if 'can_promote_members' in params else None
        self.can_send_messages: Optional[bool] = params.get('can_send_messages') if 'can_send_messages' in params else None
        self.can_send_media_messages: Optional[bool] = params.get('can_send_media_messages') if 'can_send_media_messages' in params else None
        self.can_send_other_messages: Optional[bool] = params.get('can_send_other_messages') if 'can_send_other_messages' in params else None
        self.can_add_web_page_previews: Optional[bool] = params.get('can_add_web_page_previews') if 'can_add_web_page_previews' in params else None

class ResponseParameters(TelegramObject):
    __slots__ = ('migrate_to_chat_id', 'retry_after')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.migrate_to_chat_id: Optional[int] = params.get('migrate_to_chat_id') if 'migrate_to_chat_id' in params else None
        self.retry_after: Optional[int] = params.get('retry_after') if 'retry_after' in params else None

class InputMediaPhoto(TelegramObject):
    __slots__ = ('type', 'media', 'caption', 'parse_mode')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.media: Optional[str] = params.get('media') if 'media' in params else None
        self.caption: Optional[str] = params.get('caption') if 'caption' in params else None
        self.parse_mode: Optional[str] = params.get('parse_mode') if 'parse_mode' in params else None

class InputMediaVideo(TelegramObject):
    __slots__ = ('type', 'media', 'thumb', 'caption', 'parse_mode', 'width', 'height', 'duration', 'supports_streaming')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.media: Optional[str] = params.get('media') if 'media' in params else None
        self.thumb: Optional[str] = params.get('thumb') if 'thumb' in params else None
        self.caption: Optional[str] = params.get('caption') if 'caption' in params else None
        self.parse_mode: Optional[str] = params.get('parse_mode') if 'parse_mode' in params else None
        self.width: Optional[int] = params.get('width') if 'width' in params else None
        self.height: Optional[int] = params.get('height') if 'height' in params else None
        self.duration: Optional[int] = params.get('duration') if 'duration' in params else None
        self.supports_streaming: Optional[bool] = params.get('supports_streaming') if 'supports_streaming' in params else None

class InputMediaAnimation(TelegramObject):
    __slots__ = ('type', 'media', 'thumb', 'caption', 'parse_mode', 'width', 'height', 'duration')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.media: Optional[str] = params.get('media') if 'media' in params else None
        self.thumb: Optional[str] = params.get('thumb') if 'thumb' in params else None
        self.caption: Optional[str] = params.get('caption') if 'caption' in params else None
        self.parse_mode: Optional[str] = params.get('parse_mode') if 'parse_mode' in params else None
        self.width: Optional[int] = params.get('width') if 'width' in params else None
        self.height: Optional[int] = params.get('height') if 'height' in params else None
        self.duration: Optional[int] = params.get('duration') if 'duration' in params else None

class InputMediaAudio(TelegramObject):
    __slots__ = ('type', 'media', 'thumb', 'caption', 'parse_mode', 'duration', 'performer', 'title')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.media: Optional[str] = params.get('media') if 'media' in params else None
        self.thumb: Optional[str] = params.get('thumb') if 'thumb' in params else None
        self.caption: Optional[str] = params.get('caption') if 'caption' in params else None
        self.parse_mode: Optional[str] = params.get('parse_mode') if 'parse_mode' in params else None
        self.duration: Optional[int] = params.get('duration') if 'duration' in params else None
        self.performer: Optional[str] = params.get('performer') if 'performer' in params else None
        self.title: Optional[str] = params.get('title') if 'title' in params else None

class InputMediaDocument(TelegramObject):
    __slots__ = ('type', 'media', 'thumb', 'caption', 'parse_mode')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.media: Optional[str] = params.get('media') if 'media' in params else None
        self.thumb: Optional[str] = params.get('thumb') if 'thumb' in params else None
        self.caption: Optional[str] = params.get('caption') if 'caption' in params else None
        self.parse_mode: Optional[str] = params.get('parse_mode') if 'parse_mode' in params else None

class Sticker(TelegramObject):
    __slots__ = ('file_id', 'width', 'height', 'thumb', 'emoji', 'set_name', 'mask_position', 'file_size')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.file_id: Optional[str] = params.get('file_id') if 'file_id' in params else None
        self.width: Optional[int] = params.get('width') if 'width' in params else None
        self.height: Optional[int] = params.get('height') if 'height' in params else None
        self.thumb: Optional[PhotoSize] = PhotoSize(params.get('thumb')) if 'thumb' in params else None
        self.emoji: Optional[str] = params.get('emoji') if 'emoji' in params else None
        self.set_name: Optional[str] = params.get('set_name') if 'set_name' in params else None
        self.mask_position: Optional[MaskPosition] = MaskPosition(params.get('mask_position')) if 'mask_position' in params else None
        self.file_size: Optional[int] = params.get('file_size') if 'file_size' in params else None

class StickerSet(TelegramObject):
    __slots__ = ('name', 'title', 'contains_masks', 'stickers')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.name: Optional[str] = params.get('name') if 'name' in params else None
        self.title: Optional[str] = params.get('title') if 'title' in params else None
        self.contains_masks: Optional[bool] = params.get('contains_masks') if 'contains_masks' in params else None
        self.stickers: Optional[List[Sticker]] = array_of(Sticker, params.get('stickers')) if 'stickers' in params else None

class MaskPosition(TelegramObject):
    __slots__ = ('point', 'x_shift', 'y_shift', 'scale')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.point: Optional[str] = params.get('point') if 'point' in params else None
        self.x_shift: Optional[float] = params.get('x_shift') if 'x_shift' in params else None
        self.y_shift: Optional[float] = params.get('y_shift') if 'y_shift' in params else None
        self.scale: Optional[float] = params.get('scale') if 'scale' in params else None

class InlineQuery(TelegramObject):
    __slots__ = ('id', 'from_user', 'location', 'query', 'offset')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.id: Optional[str] = params.get('id') if 'id' in params else None
        self.from_user: Optional[User] = User(params.get('from')) if 'from' in params else None
        self.location: Optional[Location] = Location(params.get('location')) if 'location' in params else None
        self.query: Optional[str] = params.get('query') if 'query' in params else None
        self.offset: Optional[str] = params.get('offset') if 'offset' in params else None

class InputTextMessageContent(TelegramObject):
    __slots__ = ('message_text', 'parse_mode', 'disable_web_page_preview')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.message_text: Optional[str] = params.get('message_text') if 'message_text' in params else None
        self.parse_mode: Optional[str] = params.get('parse_mode') if 'parse_mode' in params else None
        self.disable_web_page_preview: Optional[bool] = params.get('disable_web_page_preview') if 'disable_web_page_preview' in params else None

class InputLocationMessageContent(TelegramObject):
    __slots__ = ('latitude', 'longitude', 'live_period')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.latitude: Optional[float] = params.get('latitude') if 'latitude' in params else None
        self.longitude: Optional[float] = params.get('longitude') if 'longitude' in params else None
        self.live_period: Optional[int] = params.get('live_period') if 'live_period' in params else None

class InputVenueMessageContent(TelegramObject):
    __slots__ = ('latitude', 'longitude', 'title', 'address', 'foursquare_id', 'foursquare_type')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.latitude: Optional[float] = params.get('latitude') if 'latitude' in params else None
        self.longitude: Optional[float] = params.get('longitude') if 'longitude' in params else None
        self.title: Optional[str] = params.get('title') if 'title' in params else None
        self.address: Optional[str] = params.get('address') if 'address' in params else None
        self.foursquare_id: Optional[str] = params.get('foursquare_id') if 'foursquare_id' in params else None
        self.foursquare_type: Optional[str] = params.get('foursquare_type') if 'foursquare_type' in params else None

class InputContactMessageContent(TelegramObject):
    __slots__ = ('phone_number', 'first_name', 'last_name', 'vcard')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.phone_number: Optional[str] = params.get('phone_number') if 'phone_number' in params else None
        self.first_name: Optional[str] = params.get('first_name') if 'first_name' in params else None
        self.last_name: Optional[str] = params.get('last_name') if 'last_name' in params else None
        self.vcard: Optional[str] = params.get('vcard') if 'vcard' in params else None

class ChosenInlineResult(TelegramObject):
    __slots__ = ('result_id', 'from_user', 'location', 'inline_message_id', 'query')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.result_id: Optional[str] = params.get('result_id') if 'result_id' in params else None
        self.from_user: Optional[User] = User(params.get('from')) if 'from' in params else None
        self.location: Optional[Location] = Location(params.get('location')) if 'location' in params else None
        self.inline_message_id: Optional[str] = params.get('inline_message_id') if 'inline_message_id' in params else None
        self.query: Optional[str] = params.get('query') if 'query' in params else None

class LabeledPrice(TelegramObject):
    __slots__ = ('label', 'amount')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.label: Optional[str] = params.get('label') if 'label' in params else None
        self.amount: Optional[int] = params.get('amount') if 'amount' in params else None

class Invoice(TelegramObject):
    __slots__ = ('title', 'description', 'start_parameter', 'currency', 'total_amount')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.title: Optional[str] = params.get('title') if 'title' in params else None
        self.description: Optional[str] = params.get('description') if 'description' in params else None
        self.start_parameter: Optional[str] = params.get('start_parameter') if 'start_parameter' in params else None
        self.currency: Optional[str] = params.get('currency') if 'currency' in params else None
        self.total_amount: Optional[int] = params.get('total_amount') if 'total_amount' in params else None

class ShippingAddress(TelegramObject):
    __slots__ = ('country_code', 'state', 'city', 'street_line1', 'street_line2', 'post_code')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.country_code: Optional[str] = params.get('country_code') if 'country_code' in params else None
        self.state: Optional[str] = params.get('state') if 'state' in params else None
        self.city: Optional[str] = params.get('city') if 'city' in params else None
        self.street_line1: Optional[str] = params.get('street_line1') if 'street_line1' in params else None
        self.street_line2: Optional[str] = params.get('street_line2') if 'street_line2' in params else None
        self.post_code: Optional[str] = params.get('post_code') if 'post_code' in params else None

class OrderInfo(TelegramObject):
    __slots__ = ('name', 'phone_number', 'email', 'shipping_address')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.name: Optional[str] = params.get('name') if 'name' in params else None
        self.phone_number: Optional[str] = params.get('phone_number') if 'phone_number' in params else None
        self.email: Optional[str] = params.get('email') if 'email' in params else None
        self.shipping_address: Optional[ShippingAddress] = ShippingAddress(params.get('shipping_address')) if 'shipping_address' in params else None

class ShippingOption(TelegramObject):
    __slots__ = ('id', 'title', 'prices')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.id: Optional[str] = params.get('id') if 'id' in params else None
        self.title: Optional[str] = params.get('title') if 'title' in params else None
        self.prices: Optional[List[LabeledPrice]] = array_of(LabeledPrice, params.get('prices')) if 'prices' in params else None

class SuccessfulPayment(TelegramObject):
    __slots__ = ('currency', 'total_amount', 'invoice_payload', 'shipping_option_id', 'order_info', 'telegram_payment_charge_id', 'provider_payment_charge_id')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.currency: Optional[str] = params.get('currency') if 'currency' in params else None
        self.total_amount: Optional[int] = params.get('total_amount') if 'total_amount' in params else None
        self.invoice_payload: Optional[str] = params.get('invoice_payload') if 'invoice_payload' in params else None
        self.shipping_option_id: Optional[str] = params.get('shipping_option_id') if 'shipping_option_id' in params else None
        self.order_info: Optional[OrderInfo] = OrderInfo(params.get('order_info')) if 'order_info' in params else None
        self.telegram_payment_charge_id: Optional[str] = params.get('telegram_payment_charge_id') if 'telegram_payment_charge_id' in params else None
        self.provider_payment_charge_id: Optional[str] = params.get('provider_payment_charge_id') if 'provider_payment_charge_id' in params else None

class ShippingQuery(TelegramObject):
    __slots__ = ('id', 'from_user', 'invoice_payload', 'shipping_address')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.id: Optional[str] = params.get('id') if 'id' in params else None
        self.from_user: Optional[User] = User(params.get('from')) if 'from' in params else None
        self.invoice_payload: Optional[str] = params.get('invoice_payload') if 'invoice_payload' in params else None
        self.shipping_address: Optional[ShippingAddress] = ShippingAddress(params.get('shipping_address')) if 'shipping_address' in params else None

class PreCheckoutQuery(TelegramObject):
    __slots__ = ('id', 'from_user', 'currency', 'total_amount', 'invoice_payload', 'shipping_option_id', 'order_info')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.id: Optional[str] = params.get('id') if 'id' in params else None
        self.from_user: Optional[User] = User(params.get('from')) if 'from' in params else None
        self.currency: Optional[str] = params.get('currency') if 'currency' in params else None
        self.total_amount: Optional[int] = params.get('total_amount') if 'total_amount' in params else None
        self.invoice_payload: Optional[str] = params.get('invoice_payload') if 'invoice_payload' in params else None
        self.shipping_option_id: Optional[str] = params.get('shipping_option_id') if 'shipping_option_id' in params else None
        self.order_info: Optional[OrderInfo] = OrderInfo(params.get('order_info')) if 'order_info' in params else None

class PassportData(TelegramObject):
    __slots__ = ('data', 'credentials')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.data: Optional[List[EncryptedPassportElement]] = array_of(EncryptedPassportElement, params.get('data')) if 'data' in params else None
        self.credentials: Optional[EncryptedCredentials] = EncryptedCredentials(params.get('credentials')) if 'credentials' in params else None

class PassportFile(TelegramObject):
    __slots__ = ('file_id', 'file_size', 'file_date')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.file_id: Optional[str] = params.get('file_id') if 'file_id' in params else None
        self.file_size: Optional[int] = params.get('file_size') if 'file_size' in params else None
        self.file_date: Optional[int] = params.get('file_date') if 'file_date' in params else None

class EncryptedPassportElement(TelegramObject):
    __slots__ = ('type', 'data', 'phone_number', 'email', 'files', 'front_side', 'reverse_side', 'selfie', 'translation', 'hash')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.data: Optional[str] = params.get('data') if 'data' in params else None
        self.phone_number: Optional[str] = params.get('phone_number') if 'phone_number' in params else None
        self.email: Optional[str] = params.get('email') if 'email' in params else None
        self.files: Optional[List[PassportFile]] = array_of(PassportFile, params.get('files')) if 'files' in params else None
        self.front_side: Optional[PassportFile] = PassportFile(params.get('front_side')) if 'front_side' in params else None
        self.reverse_side: Optional[PassportFile] = PassportFile(params.get('reverse_side')) if 'reverse_side' in params else None
        self.selfie: Optional[PassportFile] = PassportFile(params.get('selfie')) if 'selfie' in params else None
        self.translation: Optional[List[PassportFile]] = array_of(PassportFile, params.get('translation')) if 'translation' in params else None
        self.hash: Optional[str] = params.get('hash') if 'hash' in params else None

class EncryptedCredentials(TelegramObject):
    __slots__ = ('data', 'hash', 'secret')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.data: Optional[str] = params.get('data') if 'data' in params else None
        self.hash: Optional[str] = params.get('hash') if 'hash' in params else None
        self.secret: Optional[str] = params.get('secret') if 'secret' in params else None

class PassportElementErrorDataField(TelegramObject):
    __slots__ = ('source', 'type', 'field_name', 'data_hash', 'message')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.source: Optional[str] = params.get('source') if 'source' in params else None
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.field_name: Optional[str] = params.get('field_name') if 'field_name' in params else None
        self.data_hash: Optional[str] = params.get('data_hash') if 'data_hash' in params else None
        self.message: Optional[str] = params.get('message') if 'message' in params else None

class PassportElementErrorFrontSide(TelegramObject):
    __slots__ = ('source', 'type', 'file_hash', 'message')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.source: Optional[str] = params.get('source') if 'source' in params else None
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.file_hash: Optional[str] = params.get('file_hash') if 'file_hash' in params else None
        self.message: Optional[str] = params.get('message') if 'message' in params else None

class PassportElementErrorReverseSide(TelegramObject):
    __slots__ = ('source', 'type', 'file_hash', 'message')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.source: Optional[str] = params.get('source') if 'source' in params else None
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.file_hash: Optional[str] = params.get('file_hash') if 'file_hash' in params else None
        self.message: Optional[str] = params.get('message') if 'message' in params else None

class PassportElementErrorSelfie(TelegramObject):
    __slots__ = ('source', 'type', 'file_hash', 'message')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.source: Optional[str] = params.get('source') if 'source' in params else None
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.file_hash: Optional[str] = params.get('file_hash') if 'file_hash' in params else None
        self.message: Optional[str] = params.get('message') if 'message' in params else None

class PassportElementErrorFile(TelegramObject):
    __slots__ = ('source', 'type', 'file_hash', 'message')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.source: Optional[str] = params.get('source') if 'source' in params else None
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.file_hash: Optional[str] = params.get('file_hash') if 'file_hash' in params else None
        self.message: Optional[str] = params.get('message') if 'message' in params else None

class PassportElementErrorFiles(TelegramObject):
    __slots__ = ('source', 'type', 'file_hashes', 'message')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.source: Optional[str] = params.get('source') if 'source' in params else None
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.file_hashes: Optional[List[str]] = params.get('file_hashes') if 'file_hashes' in params else None
        self.message: Optional[str] = params.get('message') if 'message' in params else None

class PassportElementErrorTranslationFile(TelegramObject):
    __slots__ = ('source', 'type', 'file_hash', 'message')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.source: Optional[str] = params.get('source') if 'source' in params else None
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.file_hash: Optional[str] = params.get('file_hash') if 'file_hash' in params else None
        self.message: Optional[str] = params.get('message') if 'message' in params else None

class PassportElementErrorTranslationFiles(TelegramObject):
    __slots__ = ('source', 'type', 'file_hashes', 'message')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.source: Optional[str] = params.get('source') if 'source' in params else None
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.file_hashes: Optional[List[str]] = params.get('file_hashes') if 'file_hashes' in params else None
        self.message: Optional[str] = params.get('message') if 'message' in params else None

class PassportElementErrorUnspecified(TelegramObject):
    __slots__ = ('source', 'type', 'element_hash', 'message')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.source: Optional[str] = params.get('source') if 'source' in params else None
        self.type: Optional[str] = params.get('type') if 'type' in params else None
        self.element_hash: Optional[str] = params.get('element_hash') if 'element_hash' in params else None
        self.message: Optional[str] = params.get('message') if 'message' in params else None

class Game(TelegramObject):
    __slots__ = ('title', 'description', 'photo', 'text', 'text_entities', 'animation')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.title: Optional[str] = params.get('title') if 'title' in params else None
        self.description: Optional[str] = params.get('description') if 'description' in params else None
        self.photo: Optional[List[PhotoSize]] = array_of(PhotoSize, params.get('photo')) if 'photo' in params else None
        self.text: Optional[str] = params.get('text') if 'text' in params else None
        self.text_entities: Optional[List[MessageEntity]] = array_of(MessageEntity, params.get('text_entities')) if 'text_entities' in params else None
        self.animation: Optional[Animation] = Animation(params.get('animation')) if 'animation' in params else None

class GameHighScore(TelegramObject):
    __slots__ = ('position', 'user', 'score')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.position: Optional[int] = params.get('position') if 'position' in params else None
        self.user: Optional[User] = User(params.get('user')) if 'user' in params else None
        self.score: Optional[int] = params.get('score') if 'score' in params else None

class InlineKeyboardButton(TelegramObject):
    __slots__ = ('text', 'url', 'callback_data', 'switch_inline_query', 'switch_inline_query_current_chat', 'pay')

    def __init__(self, params: Dict[str, Any]) -> None:
        self.text: Optional[str] = params.get('text') if 'text' in params else None
        self.url: Optional[str] = params.get('url') if 'url' in params else None
        self.callback_data: Optional[str] = params.get('callback_data') if 'callback_data' in params else None
        self.switch_inline_query: Optional[str] = params.get('switch_inline_query') if 'switch_inline_query' in params else None
        self.switch_inline_query_current_chat: Optional[str] = params.get('switch_inline_query_current_chat') if 'switch_inline_query_current_chat' in params else None
        self.pay: Optional[bool] = params.get('pay') if 'pay' in params else None

class InlineKeyboardMarkup(TelegramObject):
    __slots__ = ('inline_keyboard',)

    def __init__(self, params: Dict[str, Any]) -> None:
        self.inline_keyboard: Optional[List[List[InlineKeyboardButton]]] = array_of_array_of(InlineKeyboardButton, params.get('inline_keyboard')) if 'inline_keyboard' in params else None

