from telegram.ext import (Updater, 
                            CommandHandler,                             
                            ConversationHandler,
                            CallbackQueryHandler,    
                            Filters, 
                            MessageHandler,
                            PicklePersistence, dispatcher)
from bot.src.registration import Registration, Name
from bot.src.menu import Menu
import dotenv
import os
import logging

dotenv.load_dotenv()
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

registration=Registration()
name=Name()
menu=Menu()

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
            "MENU_DISPLAYED": [
                    MessageHandler(Filters.regex(
                        'Quran Recitation'), menu.display),
                    MessageHandler(Filters.regex(
                        'Hadith'), menu.display),
                    MessageHandler(Filters.regex('support'),
                                menu.display),
                    MessageHandler(Filters.regex(
                        'Info'), menu.display),
            ]},
        fallbacks=[
            CommandHandler('start', menu.display)],
        per_chat=False,
        name="main_conversation"
    )
    
    dispatcher.add_handler(main_conversation)

    updater.start_polling()
    updater.idle()