from telegram import (ReplyKeyboardMarkup,
                      Update,
                      KeyboardButton,
                      ChatAction,
                      InputMediaPhoto,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup)
from telegram.ext import CallbackContext
from bot.src.text import t, b
from bot.utils.language import lang
import logging


class Menu:
    
    def display(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        state = "MENU_DISPLAYED"
        menu_buttons = [
            [KeyboardButton(b("quran_recitation", language)),
                KeyboardButton(b("hadith", language))],
            [KeyboardButton(b("support", language)),
                KeyboardButton(b("info", language))]
        ]

        context.bot.send_message(chat_id,
                                    "Main Menu",
                                    reply_markup=ReplyKeyboardMarkup(
                                        menu_buttons, resize_keyboard=True, input_field_placeholder='menu'),
                                    parse_mode='HTML')
        logging.info(
            f"{chat_id} - opened main menu. Returned state: {state}")
        return state
    
    
    def quran_recitation(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        state = "QURAN"
        context.bot.send_message(chat_id,
                                 t("choose_surah", language))