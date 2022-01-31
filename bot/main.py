from bot.src.settings import Settings
from telegram.ext import (Updater,
                          CommandHandler,
                          ConversationHandler,
                          CallbackQueryHandler,
                          Filters,
                          MessageHandler)
from core.settings import BOT_ID, DEBUG
from bot.src.registration import Registration
from bot.src.menu import Menu
from bot.src.reciter import ReciterClass
from bot.src.audio import Audio
from bot.src.recitation import Recitation
from bot.src.support import Support
from bot.src.settings import Settings
from bot.src.group import Group
from bot.src.profile import Profile
from bot.utils.filter import buttons, FilterButton
from bot.utils.reply_to_message_filter import ReplyToMessageFilter
import dotenv
import logging
import os

dotenv.load_dotenv()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

registration = Registration()
menu = Menu()
reciter = ReciterClass()
audio = Audio()
recitation = Recitation()
support = Support()
settings = Settings()
group = Group()
profile = Profile()


def main():
    updater = Updater(token=os.getenv("BOT_TOKEN"))
    dispatcher = updater.dispatcher

    main_conversation = ConversationHandler(
        entry_points=[
            CommandHandler('start', registration.start)],
        states={
            "LANGUAGE": [
                CallbackQueryHandler(
                    registration.get_language, pattern='uz|ru|en')
            ],
            "NAME": [
                MessageHandler(Filters.text, registration.get_name)
            ],
            "REQUESTING_PHONE": [
                MessageHandler(Filters.regex(
                    buttons('skip')), menu.display),
                MessageHandler(Filters.text | Filters.contact,
                               registration.get_phone)
            ],
            "MENU_DISPLAYED": [
                MessageHandler(Filters.regex(
                    buttons('quran_recitation')), recitation.choose_reciter),
                MessageHandler(Filters.regex(
                    buttons('hadith')), menu.display),
                MessageHandler(Filters.regex(buttons('support')),
                               support.support),
                MessageHandler(Filters.regex(
                    buttons('settings')), settings.display),
            ],
            "RECITER": [
                MessageHandler(Filters.regex(buttons('back')), menu.display),
                MessageHandler(FilterButton('reciter'),
                               reciter.display)
            ],

            "AUDIO_DISPLAYED": [
                MessageHandler(Filters.regex(buttons('back')),
                               recitation.choose_reciter),
                MessageHandler(FilterButton('surah'),
                               audio.display)
            ],

            "SUPPORT": [
                MessageHandler(Filters.regex(buttons('back')), menu.display),
                MessageHandler(Filters.all, support.accept)
            ],

            "SETTINGS": [
                MessageHandler(Filters.regex(buttons('back')), menu.display),
                MessageHandler(Filters.regex(
                    buttons('my_profile')), profile.my_info),
                MessageHandler(Filters.regex(
                    buttons('language')), settings.display)
            ]
        },
        fallbacks=[
            CommandHandler('start', menu.display)],
        per_chat=False,
        name="main_conversation"
    )

    dispatcher.add_handler(main_conversation)
    dispatcher.add_handler(MessageHandler(
        ReplyToMessageFilter(Filters.user(BOT_ID)), group.reply_to_user
    ))
    updater.start_polling()
    updater.idle()
