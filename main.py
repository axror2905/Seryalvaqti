from telethon import TelegramClient

api_id = 21300715
api_hash = 'cb468aebfc14cc75a36ac500bbb59988'

client = TelegramClient('axror_session', api_id, api_hash)

client.start()

print("Telegramga muvaffaqiyatli kirdi!")

client.run_until_disconnected()
