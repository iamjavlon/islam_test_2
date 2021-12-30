from telegram import Update
from telegram.ext import CallbackContext
from bot.utils.language import lang
from bot.utils.request import get, get_target_id_by_name
from app.models import Surah

class Audio():

    def display(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        response = update.effective_message.text
        audio = Surah.objects.get(name='response')
        mp3 = audio.audio

        context.bot.send_message(chat_id,
                                 f'<b>{audio.name}</b>')
        
        context.bot.send_audio(chat_id, mp3)