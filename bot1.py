import telebot
import os

TOKEN = os.getenv("TOKEN = "7249392069:AAFyzUBMlRxBdhInRhW87dVp56NUTdv4j8o")  # Tokenni environment variables dan olish

if TOKEN is None:
    raise ValueError("TOKEN o'zgaruvchisi topilmadi! Render'dagi Environment Variables bo‘limida uni qo‘shganingizni tekshiring.")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Seryalvaqti botiga xush kelibsiz.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Seryalvaqti boti hali ishga tushmagan.")

bot.polling()
