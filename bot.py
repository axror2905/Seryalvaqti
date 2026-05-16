from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7249392069:AAGCLdFFMBdG3Sbul5xo1t1NpA-Y5rAZYK8"

VIP_GROUP = "@newdubtest"

WEBSITE = "https://nevdun.onrender.com/axror_secret_2026"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    try:

        member = await context.bot.get_chat_member(VIP_GROUP, user_id)

        if member.status in ["member", "administrator", "creator"]:

            keyboard = [
                [
                    InlineKeyboardButton(
                        "🎬 Saytga kirish",
                         web_app=WebAppInfo(url=f"{WEBSITE}?id={user_id}")
                    )
                ]
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)

            await update.message.reply_text(
                "✅ Ruxsat berildi",
                reply_markup=reply_markup
            )

        else:

            await update.message.reply_text(
                "❌ Siz VIP guruhda emassiz"
            )

    except:

        await update.message.reply_text(
            "❌ Sizda ruxsat yo‘q.\nAdmin bilan bog‘laning."
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
