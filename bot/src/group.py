from telegram.ext import CallbackContext
from telegram import Update
from core.settings import GROUP_ID
from bot.src.support import Support
from app.models import User
from bot.src.text import t
from bot.utils.language import lang


support = Support()
class Group:

    def reply_to_user(self, update: Update, context: CallbackContext):
        if not update.message.reply_to_message.forward_date:
            chat_id = support.support.chat_id
            language = lang(chat_id)
            update.effective_message.reply_text(
                t('reply_error', language), parse_mode='HTML')
            return

        try:

            if update.message.reply_to_message:

                response = update.message.text

                reply_id = update.message.reply_to_message.message_id

                user_id = context.bot_data[reply_id]

                language = lang(user_id)

                reply = t("reply_to_user", language)
                
                user = User.objects.get(id=user_id)
                user_username = user.username

                context.bot.send_message(chat_id=user_id,
                                         text=f"{reply}".format(response),
                                         parse_mode='HTML')
                update.effective_message.reply_text(
                    t(f'answer_sent', language).format(username=user_username), parse_mode='HTML')

        except KeyError:
            reply_id = update.message.reply_to_message.message_id

            user_id = context.bot_data[reply_id]

            language = lang(user_id)
            
            update.effective_message.reply_text(
                t('reply_exception', language))