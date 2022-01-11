from telegram import Update
from telegram.ext import CallbackContext
from bot.utils.language import lang
from bot.src.text import t, b
from app.models import Surah

class Audio():

    def display(self, update: Update, context: CallbackContext):
        try:
            chat_id = update.effective_chat.id
            language = lang(chat_id)
            response = update.effective_message.text
            audio = Surah.objects.get(name=response)
            number = audio.number
            name = audio.name
            mp3 = audio.audio
            
            context.bot.send_audio(chat_id, mp3, 
                                   filename=f'{number}_{name}', 
                                   caption=f'<b>{audio.name}</b>', 
                                   parse_mode='HTML')
        except:
            context.bot.send_message(chat_id,
                                     t('raise_no_surah', language))