
#   First, a few handler functions are defined. Then, those functions are passed to
#   the Dispatcher and registered at their respective places.
#   Press Ctrl-C on the command line or send a signal to the process to stop the
#   bot.


import logging
from datetime import date
import calendar
from os import getpriority

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.filters import MergedFilter

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
my_date = date.today()
TOKEN_FILE = open("TOKEN_FILE.txt")
TOKEN = TOKEN_FILE.read()
print("Bot Token is:",TOKEN)
Lun = """Lunedì:
    Diritto: Monteforte
    Fisica Laboratorio: Montinaro - Tomasi
    Disegno Tecnico: Capone
    Scienze della Terra: Lopalco
    Antologia: Urso
    Grammatica: Urso"""
Mar = """Martedì:
    Inglese: Dima
    Aritmetica: Guida
    Storia: Martiriggiano
    Educazione Fisica: De Giorgi M.
    Chimica Laboratorio: Dell'Avvocata - Ciardo"""
Mer = """Mercoledì:
    Diritto: Monteforte
    Tecnologia Laboratorio: Licchetta - Capone
    Scienze della Terra: Lopalco
    Religione: Varraso
    Fisica: Montinaro"""
Gio = """Giovedì:
    Chimica: Ciardo
    Chimica: Ciardo
    Fisica: Montinaro
    Antologia: Urso
    Grammatica: Urso"""
Ven = """Venerdì: 
        Geometria: Guida
        Disegno Tecnico: Capone
        Informatica Laboratorio: De Giorgi G. - Poto
        Informatica: Poto
        Inglese: Dima"""
Sab = """Sabato:
    Educazione Fisica: De Giorgi M.
    Aritmetica: Guida
    Aritmetica: Guida
    Inglese Classico: Dima
    Informatica Laboratorio: De Giorgi G. - Poto"""
Dom = """Cosa cazzo pensi di fare? É domenica."""
#   Define a few command handlers. These usually take the two arguments update and
#   context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    #   Send a message when the command /start is issued.
    update.message.reply_text('Bot Del Popping: Acceso')


def help(update, context):
    #   Send a message when the command /help is issued.
    update.message.reply_text("""Lista dei Comandi:
    !! Work In Progress !!
    /start - Avvia il Bot del Popping
    /help - Lista dei comandi
    /orario - Orario di oggi
    /echo - Rimanda il tuo messaggio
    """)

def orario(update, context):
    if calendar.day_name[my_date.weekday()] == "Monday":
        update.message.reply_text(Lun)
    
    elif calendar.day_name[my_date.weekday()] == "Tuesday":
        update.message.reply_text(Mar)
    
    elif calendar.day_name[my_date.weekday()] == "Wednesday":
        update.message.reply_text(Mer)
    
    elif calendar.day_name[my_date.weekday()] == "Thursday":
        update.message.reply_text(Gio)
    
    elif  calendar.day_name[my_date.weekday()] == "Friday":
        update.message.reply_text(Ven)
    elif calendar.day_name[my_date.weekday()] == "Saturday":
        update.message.reply_text(Sab)
    elif calendar.day_name[my_date.weekday()] == "Sunday":
        update.message.reply_text(Dom)

def echo(update, context):
    #   Echo the user message.
    computedReply = update.message.text.replace('/echo', '')
    update.message.reply_text(computedReply.replace('@BossDelPopping_Bot', ''))

def lun(update, context):
    #   Send a message when the command /help is issued.
    update.message.reply_text(Lun)

def mar(update, context):
    #   Send a message when the command /help is issued.
    update.message.reply_text(Mar)

def mer(update, context):
    #   Send a message when the command /help is issued.
    update.message.reply_text(Mer)

def gio(update, context):
    #   Send a message when the command /help is issued.
    update.message.reply_text(Gio)

def ven(update, context):
    #   Send a message when the command /help is issued.
    update.message.reply_text(Ven)

def sab(update, context):
    #   Send a message when the command /help is issued.
    update.message.reply_text(Sab)

def dom(update, context):
    #   Send a message when the command /help is issued.
    update.message.reply_text(Dom)

def error(update, context):
    #   Log Errors caused by Updates.
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    #   Start the bot.
    #   Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN.replace(' ',''), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("orario", orario))
    dp.add_handler(CommandHandler("echo", echo))
    dp.add_handler(CommandHandler("lun", lun))
    dp.add_handler(CommandHandler("mar", mar))
    dp.add_handler(CommandHandler("mer", mer))
    dp.add_handler(CommandHandler("gio", gio))
    dp.add_handler(CommandHandler("ven", ven))
    dp.add_handler(CommandHandler("sab", sab))
    dp.add_handler(CommandHandler("dom", dom))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()