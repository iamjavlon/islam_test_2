from telegram import Update
from telegram.ext import CallbackContext
from bot.utils.language import lang
from bot.src.text import t, b
from bot.utils.build_menu import build_menu
from bot.utils.request import get, get_target_id_by_name
from app.models import User, Reciter
from bot.src.audio import Audio
from bot.utils.request import parser_reciter, parser_surah

audio = Audio()

class Reciter():

    def display(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        response = update.effective_message.text

        state = "AUDIO_DISPLAYED"
        reciter = Reciter.objects.get(name='response')

        custom_list = []
        obj = Surah.objects.all(reciter=reciter)
        for i in obj:
            custom_list.append(i.name)
        return custom_list
        audio_list = custom_list
        
        context.bot.send_message(chat_id,
                                f'<b>{t("choose_surah", language)}</b>',
                                 reply_markup=ReplyKeyboardMarkup(
                                     build_menu(
                                         buttons=[
                                             KeyboardButton(s) for s in audio_list
                                         ],
                                         n_cols=1,
                                         footer_buttons=[
                                             KeyboardButton(
                                                 b("back", language))
                                         ]), resize_keyboard=True, input_field_placeholder=t('audio', language)),
                                 parse_mode='HTML')
        logging.info(
            f"{chat_id} - wantS to listen to one of the audios. Returned state: {state}")
        return state