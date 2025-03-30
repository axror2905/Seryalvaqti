import telebot
import os

TOKEN = os.getenv("TOKEN")  # Tokenni environment variable orqali olish
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Seryalvaqti botiga xush kelibsiz.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Seryalvaqti boti hali ishga tushmagan.")

bot.polling()
