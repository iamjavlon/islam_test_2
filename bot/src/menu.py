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
from bot.utils.build_menu import build_menu
from app.models import User, Surah
from bot.utils.request import parser_reciter, parser_surah
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
