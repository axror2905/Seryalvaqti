import telebot

TOKEN = "7249392069:AAFyzUBMlRxBdhInRhW87dVp56NUTdv4j8o"  # Bu yerga o'zingizning bot tokeningizni yozing
bot = telebot.TeleBot(TOKEN)

# Botga start buyrug'i berilganda ishlaydi
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Seryalvaqti botiga xush kelibsiz.")

# Hozircha bot faqat buyruqlarga javob beradi
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Seryalvaqti boti hali ishga tushmagan.")

# Botni doimiy ravishda ishlatish
bot.polling()
