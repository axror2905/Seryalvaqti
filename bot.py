import telebot

TOKEN = "7249392069:AAGCLdFFMBdG3Sbul5xo1t1NpA-Y5rAZYK8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    text = """
🎬 NevDub

Saytga kirish uchun pastdagi tugmani bosing.
"""

    markup = telebot.types.InlineKeyboardMarkup()

    button = telebot.types.InlineKeyboardButton(
        "🎬 Saytga kirish",
        url="http://127.0.0.1:5000"
    )

    markup.add(button)

    bot.send_message(message.chat.id, text, reply_markup=markup)

print("Bot ishlayapti 🔥")

bot.infinity_polling()
