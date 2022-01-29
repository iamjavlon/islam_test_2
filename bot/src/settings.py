from telegram import (Update, ReplyKeyboardMarkup, KeyboardButton)
from telegram.ext import CallbackContext
from bot.src.text import t, b
from bot.utils.language import lang
import logging


class Settings():
    def display(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        state = "SETTINGS"

        markup = [
            [KeyboardButton(b("my_profile", language)),
                KeyboardButton(b("language", language))],
            [KeyboardButton(b("back", language))]
        ]

        context.bot.send_message(chat_id,
                                 t("settings", language),
                                 reply_markup=ReplyKeyboardMarkup(
                                     markup, resize_keyboard=True,
                                     input_field_placeholder=t('settings_placeholder', language)),
                                 parse_mode='HTML')

        logging.info(
            f"{chat_id} - opened settings. Returned state: {state}")
        return state
