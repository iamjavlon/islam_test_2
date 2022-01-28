from telegram.ext import (Updater, 
                            CommandHandler,                             
                            ConversationHandler,
                            CallbackQueryHandler,    
                            Filters, 
                            MessageHandler,
                            PicklePersistence, dispatcher)
from bot.src.registration import Registration
from bot.src.menu import Menu
from bot.src.reciter import ReciterClass
from bot.src.audio import Audio
from bot.src.recitation import Recitation
from bot.src.support import Support
from bot.utils.filter import buttons, FilterButton
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
reciter=ReciterClass()
audio=Audio()
recitation=Recitation()
support=Support()

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
                        buttons('quran_recitation')), recitation.choose_reciter),
                    MessageHandler(Filters.regex(
                        buttons('hadith')), menu.display),
                    MessageHandler(Filters.regex(buttons('support')),
                                support.support),
                    MessageHandler(Filters.regex(
                        buttons('info')), menu.display),
            ],
            "RECITER":[
                MessageHandler(Filters.regex(buttons('back')), menu.display),
                MessageHandler(FilterButton('reciter'),
                                reciter.display)
                ],
                
            "AUDIO_DISPLAYED": [
                MessageHandler(Filters.regex(buttons('back')), recitation.choose_reciter),
                MessageHandler(FilterButton('surah'),
                                audio.display)
            ],
            
            "SUPPORT": [
                MessageHandler(Filters.regex(buttons('back')), menu.display),
                MessageHandler(Filters.all, support.accept)
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