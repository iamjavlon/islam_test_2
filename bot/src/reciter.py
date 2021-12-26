# from telegram import Update
# from telegram.ext import CallbackContext
# from bot.utils.language import lang
# from bot.utils.request import get, get_target_id_by_name
# from app.models import Reciter
# from bot.src.audio import Audio

# audio = Audio()

# class Reciter():

#     def display(self, update: Update, context: CallbackContext):
#         chat_id = update.effective_chat.id
#         language = lang(chat_id)
#         id = get_target_id_by_name('reciter', update.message.text)
#         reciter = Reciter.objects.get(id=id)
        

#         context.bot.send_message(chat_id,
#                                  f"{reciter.name}")
        
#         return audio.display