from telegram import (ReplyKeyboardMarkup,
                      Update,
                      KeyboardButton)
from telegram.ext import CallbackContext
from bot.src.text import t, b
from bot.utils.language import lang
from bot.src.menu import Menu
from core.settings import GROUP_ID
import logging


class Support():
    def support(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        state = "SUPPORT"
        markup = [
            [KeyboardButton(b("back", language))]
        ]

        context.bot.send_message(chat_id,
                                 t("request_feedback", language),
                                 reply_markup=ReplyKeyboardMarkup(
                                     markup, resize_keyboard=True, input_field_placeholder=t('support', language)),
                                 parse_mode='HTML')

        logging.info(
            f"{chat_id} - is requesting support. Returned state: {state}")
        return state
    
    
    
    def accept(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)
        user_request = update.message

        if user_request.text or user_request.photo or user_request.voice:
            msg = context.bot.forward_message(GROUP_ID,
                                              from_chat_id=chat_id,
                                              message_id=user_request.message_id)

            payload = {
                msg.message_id: chat_id
            }
            context.bot_data.update(payload)
            update.effective_message.reply_text(t("accept_question", language))
            return Menu().display(update, context)
        else:
            return self.format_error(update, context)

    def format_error(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        language = lang(chat_id)

        context.bot.send_message(chat_id,
                                 t('support_format_error', language),
                                 parse_mode='HTML')
    