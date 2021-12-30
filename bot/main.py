from telegram.ext import (Updater, 
                            CommandHandler,                             
                            ConversationHandler,
                            CallbackQueryHandler,    
                            Filters, 
                            MessageHandler,
                            PicklePersistence, dispatcher)
from bot.src.registration import Registration
from bot.src.menu import Menu
from bot.src.reciter import Reciter
from bot.src.audio import Audio
from bot.utils.filter import buttons
import dotenv
import logging
import os

dotenv.load_dotenv()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

registration=Registration()
menu=Menu()
reciter=Reciter()
audio=Audio()

def main():
    updater = Updater(token=os.getenv("BOT_TOKEN"))
    dispatcher=updater.dispatcher
    
    
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
                        buttons('quran_recitation')), menu.choose_reciter),
                    MessageHandler(Filters.regex(
                        buttons('hadith')), menu.display),
                    MessageHandler(Filters.regex(buttons('support')),
                                menu.display),
                    MessageHandler(Filters.regex(
                        buttons('info')), menu.display),
            ],
            "RECITER": [
                MessageHandler(Filters.regex(buttons('back')), menu.display)
                MessageHandler(FilterButtonReciter('reciter'),
                                reciter.display)
            ],
            "AUDIO_DISPLAYED": [
                MessageHandler(Filters.regex(buttons('back')), reciter.display)
                MessageHandler(FilterButton('surah'),
                                audio.display)
            ]
            },
        fallbacks=[
            CommandHandler('start', menu.display)],
        per_chat=False,
        name="main_conversation"
    )
    
    dispatcher.add_handler(main_conversation)

    updater.start_polling()
    updater.idle()