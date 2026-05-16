from flask import Flask, render_template, request
from telethon import TelegramClient
import asyncio

app = Flask(__name__)

api_id = 21300715
api_hash = "cb468aebfc14cc75a36ac500bbb59988"

CHANNEL = -1003991373252
SECRET_PATH = "axror_secret_2026"

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

client = TelegramClient(
    "newsession",
    api_id,
    api_hash,
    loop=loop
)

client.start()

@app.route(f"/{SECRET_PATH}")
def home():
    user_id = request.args.get("id")

    return f"""
    <html>
    <head>
        <title>NevDub</title>
    </head>
    <body style="background:#111;color:white;text-align:center;padding-top:100px;font-family:sans-serif;">
        <h1>NevDub</h1>

        <a href="/movies" style="
            display:block;
            width:200px;
            margin:20px auto;
            padding:15px;
            background:red;
            color:white;
            text-decoration:none;
            border-radius:10px;
        ">Kinolar</a>

        <a href="/serials" style="
            display:block;
            width:200px;
            margin:20px auto;
            padding:15px;
            background:blue;
            color:white;
            text-decoration:none;
            border-radius:10px;
        ">Seriallar</a>

        <p>ID: {user_id}</p>
    </body>
    </html>
    """


@app.route("/movies")
def movies():
    messages = loop.run_until_complete(
        client.get_messages(CHANNEL, limit=100)
    )

    movies_list = []

    for msg in messages:
        if msg.file and msg.file.mime_type:
            if "video" in msg.file.mime_type:

                text = (msg.message or "").lower()

                if "#kino" not in text:
                    continue

                movies_list.append({
                    "id": msg.id,
                    "title": msg.message or "Kino"
                })

    html = "<h1 style='color:white'>Kinolar</h1>"

    for movie in movies_list:
        html += f"""
        <div style='background:#222;padding:15px;margin:10px;border-radius:10px'>
            <a style='color:white;text-decoration:none'
            href='/watch/{movie["id"]}'>
            {movie["title"]}
            </a>
        </div>
        """

    return f"<body style='background:#111'>{html}</body>"


@app.route("/serials")
def serials():
    messages = loop.run_until_complete(
        client.get_messages(CHANNEL, limit=100)
    )

    serials_list = []

    for msg in messages:
        if msg.file and msg.file.mime_type:
            if "video" in msg.file.mime_type:

                text = (msg.message or "").lower()

                if "#serial" not in text:
                    continue

                serials_list.append({
                    "id": msg.id,
                    "title": msg.message or "Serial"
                })

    html = "<h1 style='color:white'>Seriallar</h1>"

    for serial in serials_list:
        html += f"""
        <div style='background:#222;padding:15px;margin:10px;border-radius:10px'>
            <a style='color:white;text-decoration:none'
            href='/watch/{serial["id"]}'>
            {serial["title"]}
            </a>
        </div>
        """

    return f"<body style='background:#111'>{html}</body>"


@app.route("/watch/<int:msg_id>")
def watch(msg_id):

    link = f"https://t.me/c/{str(CHANNEL)[4:]}/{msg_id}"

    html = f"""
    <body style="background:#111;margin:0">

    <iframe
        src="{link}"
        width="100%"
        height="100%"
        style="border:none;position:fixed;top:0;left:0">
    </iframe>

    </body>
    """

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
