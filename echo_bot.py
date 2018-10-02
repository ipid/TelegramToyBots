from bot_api import BotClient

def echo_bot(bot: BotClient):
        offset = update.update_id + 1
        if update.message is not None: # It's a message
            msg = update.message
            if msg.text is not None:
                visual_msg = msg.text
                bot.sendMessage(
                    chat_id=msg.chat.id,
                    text=msg.text
                )
            elif msg.audio is not None:
                visual_msg = '[Audio]'
                bot.sendAudio(
                    chat_id=msg.chat.id,
                    audio=msg.audio.file_id
                )
            elif msg.document is not None:
                visual_msg = '[File]'
                bot.sendDocument(
                    chat_id=msg.chat.id,
                    document=msg.document.file_id
                )
            elif msg.animation is not None:
                visual_msg = '[Audio]'
                bot.sendAnimation(
                    chat_id=msg.chat.id,
                    audio=msg.audio.file_id
                )
            elif msg.photo is not None:
                visual_msg = '[Photo]'
                bot.sendPhoto(
                    chat_id=msg.chat.id,
                    photo=msg.photo[-1].file_id
                )
            elif msg.sticker is not None:
                visual_msg = '[Sticker]'
                bot.sendSticker(
                    chat_id=msg.chat.id,
                    sticker=msg.sticker.file_id
                )
            elif msg.voice is not None:
                visual_msg = '[Voice]'
                bot.sendVoice(
                    chat_id=msg.chat.id,
                    voice=msg.voice.file_id
                )
            elif msg.video is not None:
                visual_msg = '[Video]'
                bot.sendVideo(
                    chat_id=msg.chat.id,
                    video=msg.video.file_id
                )
            else:
                visual_msg = '[Unknown]'

            print(f"User <{update.message.from_user.username}>: {visual_msg}")
        elif update.edited_message is not None:
            pass