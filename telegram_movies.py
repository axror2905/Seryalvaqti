from telethon import TelegramClient

api_id = 21300715
api_hash = "cb468aebfc14cc75a36ac500bbb59988"

channel = "premyera_k1nolar_01"

client = TelegramClient("session", api_id, api_hash)

async def main():

    messages = await client.get_messages(channel, limit=10)

    for message in messages:

        if message.text:
            print(message.text)

with client:
    client.loop.run_until_complete(main())
