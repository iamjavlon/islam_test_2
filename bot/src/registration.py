from telegram import (ReplyKeyboardMarkup,
                      Update,
                      KeyboardButton,
                      ChatAction,
                      InputMediaPhoto,
                      ReplyKeyboardMarkup,
                      ReplyKeyboardRemove,
                      InlineKeyboardButton,
                      InlineKeyboardMarkup)
from telegram.ext import CallbackContext
from bot.src.text import t, b
from bot.utils.language import lang
import logging

class Registration:
    """
    Base class for registration
    """

    def is_private_chat(self, chat_id: int):
        if chat_id > 0:
            return True
        else:
            return False
    
    
    def start(self, update:Update, context: CallbackContext):
        chat_id=update.effective_chat.id
        first_name=update.effective_chat.first_name
        last_name=update.effective_chat.last_name
        username = (
            "@" + update.effective_user.username) if update.effective_user.username is not None else None
        if self.is_private_chat(chat_id):
            context.bot.send_message(chat_id,
                                            f"{t('greeting', lang='ru')}\n{t('greeting', lang='en')}",
                                            parse_mode='HTML')
            return self.request_language(update, context)
        else:
            return  # The bot is working in the group.

        
    def request_language(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        markup = [
            [InlineKeyboardButton(b('language', lang='uz'), callback_data='uz'),
            InlineKeyboardButton(b('language', lang='ru'), callback_data='ru'),
            InlineKeyboardButton(b('language', lang='en'), callback_data='en')]
        ]
        state = "LANGUAGE"

        context.bot.send_message(chat_id,
                                f"{t('choose_language', lang='uz')}\n{t('choose_language', lang='ru')}\n{t('choose_language', lang='en')}",
                                reply_markup=InlineKeyboardMarkup(markup))

        logging.info(
            f'{chat_id} - choosing a language. Returned state: {state}')
        return state
    
    
    def get_language(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        query = update.callback_query
        query.answer()
        query.delete_message()

        if query.data == 'uz' or query.data == 'ru':
            context.bot.send_message(chat_id,
                                     t("uzbek_soon", lang="uz"), t("russian_soon", lang="ru"),
                                     parse_mode='HTML')
            return self.request_language(update, context)

        return self.request_name(update, context)
    
    def request_name(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        state = "NAME"
        context.bot.send_message(chat_id,
                                 t("request_name", language),
                                 reply_markup=ReplyKeyboardRemove())
        logging.info(
            f"{chat_id} - has accepted terms and conditions and now is being requested for his name. Returning state {state}")
        return state
    
    
    def get_name(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        name_input = update.effective_message.text
        full_name = name_input.split(" ")

        # if len(full_name) == 2:
        #     payload = {
        #         "id": chat_id,
        #         "first_name": full_name[0],
        #         "last_name": full_name[1]
        #     }
        # else:
        #     payload = {
        #         "id": chat_id,
        #         "first_name": name_input,
        #         "last_name": None
        #     }
        # put(f"users/{chat_id}/", payload)
        context.bot.send_message(chat_id,
                                 t("name_accepted", language))
        return self.request_phone(update, context)
    
    def request_phone(self, update: Update, context: CallbackContext):
        
