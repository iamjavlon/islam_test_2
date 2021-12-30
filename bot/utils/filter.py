from telegram import Update
from telegram.ext import CallbackContext
from bot.src.text import t, b
from bot.utils.language import lang
from telegram.ext import MessageFilter
from bot.src.text import b
from app.models import Reciter
from bot.utils.request import parser_reciter
import json

j = json.load(open("bot/assets/text.json", "r", encoding="utf-8"))


# class FilterButton(MessageFilter):
#     def __init__(self, section_key: str):
#         self.section_key = section_key

    # def filter(self, message):
    #     return message.text in parser_filter(f"{self.section_key}/", key="name")

class FilterButtonReciter(MessageFilter):
    def filter(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        response = update.effective_message.text

        reciter = Reciter.objects.get(name='response')
        return reciter

def buttons(key: str):
    button = j["buttons"][key]
    __buttons = []
    for i in button:
        __buttons.append(button[i])
    return '|'.join(j for j in __buttons)