from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, LabeledPrice, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, chat
from bot.src.menu import Menu
from app.models import User
from bot.src.text import t, b
from bot.utils.language import lang
import datetime
import locale
import logging


class Profile():
    def my_info(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        user = User.objects.get(id=chat_id)
        first_name = user.first_name
        last_name = user.last_name
        phone = user.phone_number

        context.bot.send_message(chat_id,
                                 f"{t('my_info', language)}"
                                 .format(
                                     user_id=chat_id,
                                     first_name=first_name,
                                     last_name=last_name,
                                     phone=phone
                                 ), parse_mode='HTML')
