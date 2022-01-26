from telegram import (ReplyKeyboardMarkup,
                      Update,
                      KeyboardButton)
from telegram.ext import CallbackContext
from bot.src.text import t, b
from bot.utils.language import lang
from app.models import User, Surah
from bot.utils.build_menu import build_menu
from bot.utils.request import parser_reciter, parser_surah
import logging


class Recitation():
    def choose_reciter(self, update: Update, context: CallbackContext):
            chat_id = update.effective_chat.id
            language = lang(chat_id)
            user = User.objects.get(id=chat_id)
            state = "RECITER"
            
            reciter_list = parser_reciter('name')
            
            
            context.bot.send_message(chat_id,
                                    f'<b>{t("choose_reciter", language)}</b>',
                                    reply_markup=ReplyKeyboardMarkup(
                                        build_menu(
                                            buttons=[
                                                KeyboardButton(s) for s in reciter_list
                                            ],
                                            n_cols=1,
                                            footer_buttons=[
                                                KeyboardButton(
                                                    b("back", language))
                                            ]), resize_keyboard=True, input_field_placeholder=t('audio', language)),
                                    parse_mode='HTML')
            logging.info(
                f"{chat_id} - want to listen to one of the audios. Returned state: {state}")
            return state