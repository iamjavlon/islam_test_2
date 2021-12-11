from telegram import (ReplyKeyboardMarkup,
                      Update,
                      KeyboardButton,
                      ChatAction,
                      InputMediaPhoto,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup)
from telegram.ext import CallbackContext
from bot.src.text import t, b
# from bot.utils.language import lang
import logging


class Menu:
    
    def display(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        state = "MENU_DISPLAYED"
        menu_buttons = [
            [KeyboardButton("Quran Recitation"),
                KeyboardButton("Hadith")],
            [KeyboardButton("support"),
                KeyboardButton("Info")]
        ]

        context.bot.send_message(chat_id,
                                    "Main Menu",
                                    reply_markup=ReplyKeyboardMarkup(
                                        menu_buttons, resize_keyboard=True, input_field_placeholder='menu'),
                                    parse_mode='HTML')
        logging.info(
            f"{chat_id} - opened main menu. Returned state: {state}")
        return state