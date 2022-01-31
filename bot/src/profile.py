from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, LabeledPrice, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, chat
from bot.src.settings import Settings
from app.models import User
from bot.src.text import t, b
from bot.utils.language import lang
import logging


class Profile():
    def my_info(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        user = User.objects.get(id=chat_id)
        first_name = user.first_name
        last_name = user.last_name
        phone = user.phone_number
        if not last_name == None:
            last_name
        else:
            last_name = '-'
        if not phone == None:
            phone = f'+{phone}'
        else:
            phone = '-'

        context.bot.send_message(chat_id,
                                 f"{t('my_info', language)}"
                                 .format(
                                     user_id=chat_id,
                                     first_name=first_name,
                                     last_name=last_name,
                                     phone=phone,
                                     language=language
                                 ), parse_mode='HTML')


    def change_language(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        
        state = "CHANGE_LANGUAGE"
        markup = [
            [InlineKeyboardButton(b('choose_language', lang='uz'), callback_data='uz'),
             InlineKeyboardButton(
                 b('choose_language', lang='ru'), callback_data='ru'),
             InlineKeyboardButton(b('choose_language', lang='en'), callback_data='en')]
        ]
        
        
        context.bot.send_message(chat_id,
                                 f"{t('change_language', language)}"
                                 .format(
                                     language=language), 
                                 parse_mode='HTML',
                                 reply_markup=InlineKeyboardMarkup(markup))
        logging.info(
            f'{chat_id} - choosing a language. Returned state: {state}')
        return state
        
    def get_language(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        query = update.callback_query
        query.answer()
        query.delete_message()

        if query.data == 'uz':
            context.bot.send_message(chat_id,
                                     t("uzbek_soon", lang="uz"),
                                     parse_mode='HTML')
            return self.change_language(update, context)
        if query.data == 'ru':
            context.bot.send_message(chat_id,
                                     t("russian_soon", lang="ru"),
                                     parse_mode='HTML')
            return self.change_language(update, context)
        user = User.objects.get(id=chat_id)
        user.language = query.data
        user.save()
        return Settings().display(update, context)
        