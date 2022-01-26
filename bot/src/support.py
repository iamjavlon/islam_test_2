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


class Support():
    def support_page(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        state = "SUPPORT"
        markup = [
            [KeyboardButton(b("back", language))]
        ]
        
        context.bot.send_message(chat_id,
                                    f'<b>{t("contact_support", language)}</b>',
                                    reply_markup=ReplyKeyboardMarkup(
                                        markup, resize_keyboard=True, input_field_placeholder=t('support', language)),
                                    parse_mode='HTML')
        logging.info(
            f"{chat_id} - wants to write to support or leave feedback. Returned state: {state}")
        return state
    