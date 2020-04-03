import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from weatherapp import forecast
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
#check for new messages
updater = Updater(token="dummytoken")

#allows to register message handler
dispatcher = updater.dispatcher

#define callback function for command
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, Welcome to TestBot.01")

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, Welcome to TestBot.01")

#create a command handler
start_handler = CommandHandler("start", start)

#add command handler to dispatcher
dispatcher.add_handler(start_handler)

def get_weather(bot, update):
    button = [
        [KeyboardButton("Share Location", request_location=True)]
    ]
    reply_markup=ReplyKeyboardMarkup(button)
    bot.send_message(chat_id=update.message.chat_id, text="Mind Sharing Location?",
                     reply_markup=reply_markup)

get_weather_handler = CommandHandler("weather", get_weather)

dispatcher.add_handler(get_weather_handler)

def location(bot, update):
    
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    
    forecasts = forecast(lat, lon)
    bot.send_message(chat_id=update.message.chat_id, 
                     text=forecasts,
                     reply_markup=ReplyKeyboardRemove())
    

location_handler = MessageHandler(Filters.location, location)
dispatcher.add_handler(location_handler)

def button(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id, 
                          text="Thanks for choosing {}.".format(query.data),
                          message_id=query.message.message_id)

button_handler = CallbackQueryHandler(button)

dispatcher.add_handler(button_handler)

def option(bot, update):
    button = [
        [InlineKeyboardButton("Option 1", callback_data="1"),
        InlineKeyboardButton("Option 2", callback_data="2")],
        [InlineKeyboardButton("Option 3", callback_data="3")]
    ]
    reply_markup = InlineKeyboardMarkup(button)

    bot.send_message(chat_id=update.message.chat_id, text="Choose one option..", reply_markup=reply_markup)

option_handler = CommandHandler("option", option)

dispatcher.add_handler(option_handler)


#send received message
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

# create a text handler
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(echo_handler)

#start polling
updater.start_polling()
