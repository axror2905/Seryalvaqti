from flask import Flask, render_template, request
from telethon import TelegramClient
import asyncio

from flask import Response

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

loop.run_until_complete(client.connect())

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


@app.route("/watch/<int:msg_id>")
def watch(msg_id):

    html = f"""
    <html>
    <head>
        <title>Player</title>
    </head>

    <body style="margin:0;background:black;">

    <video width="100%" height="100%" controls autoplay>
        <source src="/stream/{msg_id}" type="video/mp4">
    </video>

    </body>
    </html>
    """

    return html



@app.route("/stream/<int:msg_id>")
def stream(msg_id):

    message = loop.run_until_complete(
        client.get_messages(CHANNEL, ids=msg_id)
    )

    file_path = loop.run_until_complete(
        message.download_media(file=f"temp_{msg_id}.mp4")
    )

    def generate():
        with open(file_path, "rb") as f:
            while chunk := f.read(1024 * 1024):
                yield chunk

    return Response(
        generate(),
        mimetype="video/mp4"
    )

@app.route("/movies")
def movies():

    messages = loop.run_until_complete(
        client.get_messages(CHANNEL, limit=100)
    )

    html = """
    <body style="background:#111;color:white">
    <h1>Kinolar</h1>
    """

    for msg in messages:

            if msg.file and msg.file.mime_type:

    if "video" in msg.file.mime_type:

        if "#kino" in (msg.message or "").lower():

                html += f"""
                <div style="
                    background:#222;
                    padding:15px;
                    margin:10px;
                    border-radius:10px;
                ">

                <h3>{msg.message or "Kino"}</h3>

                <video width="100%" controls controlsList="nodownload">
                    <source src="/stream/{msg.id}" type="video/mp4">
                </video>

                </div>
                """

    html += "</body>"

    return html


@app.route("/serials")
def serials():

    messages = loop.run_until_complete(
        client.get_messages(CHANNEL, limit=100)
    )

    serials_list = []

    for msg in messages:

        if msg.file and msg.file.mime_type:

            if "video" in msg.file.mime_type:

                if "#serial" in (msg.message or "").lower():

                    serials_list.append({
                        "id": msg.id,
                        "title": msg.message or "Serial"
                    })

    html = """
    <body style='background:#111;color:white;font-family:sans-serif'>
    <h1>Seriallar</h1>
    """

    for serial in serials_list:

        html += f"""

        <div style="
        background:#222;
        padding:15px;
        margin:10px;
        border-radius:10px">

        <h3>{serial['title']}</h3>

        <video width="100%" controls controlsList="nodownload">
            <source src="/stream/{serial['id']}" type="video/mp4">
        </video>

        </div>

        """

    html += "</body>"

    return html
