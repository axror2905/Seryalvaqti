from flask import Flask, request, send_file
from telethon import TelegramClient
import asyncio
import os

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
    api_hash
)

loop.run_until_complete(client.connect())


@app.route(f"/{SECRET_PATH}")
def home():

    user_id = request.args.get("id")

    return f"""
    <html>

    <head>
        <meta name="viewport"
        content="width=device-width, initial-scale=1.0">

        <title>NevDub</title>
    </head>

    <body style="
        background:#111;
        color:white;
        text-align:center;
        padding-top:100px;
        font-family:sans-serif;
    ">

        <h1>NevDub</h1>

        <a href="/movies" style="
            display:block;
            width:220px;
            margin:20px auto;
            padding:15px;
            background:red;
            color:white;
            text-decoration:none;
            border-radius:10px;
            font-size:20px;
        ">
            🎬 Kinolar
        </a>

        <a href="/serials" style="
            display:block;
            width:220px;
            margin:20px auto;
            padding:15px;
            background:blue;
            color:white;
            text-decoration:none;
            border-radius:10px;
            font-size:20px;
        ">
            📺 Seriallar
        </a>

        <p>ID: {user_id}</p>

    </body>
    </html>
    """


@app.route("/stream/<int:msg_id>")
def stream(msg_id):

    message = loop.run_until_complete(
        client.get_messages(CHANNEL, ids=msg_id)
    )

    file_path = loop.run_until_complete(
        message.download_media(file=f"temp_{msg_id}.mp4")
    )

    absolute_path = os.path.abspath(file_path)

    return send_file(
        absolute_path,
        mimetype="video/mp4",
        conditional=True
    )


@app.route("/movies")
def movies():

    messages = loop.run_until_complete(
        client.get_messages(CHANNEL, limit=100)
    )

    html = """
    <html>

    <head>
        <meta name="viewport"
        content="width=device-width, initial-scale=1.0">

        <title>NevDub Kinolar</title>
    </head>

    <body style="
        background:#111;
        color:white;
        font-family:sans-serif;
        margin:0;
        padding:10px;
    ">

    <h1 style="text-align:center">
        Kinolar
    </h1>
    """

    for msg in messages:

        if msg.file and msg.file.mime_type:

            if "video" in msg.file.mime_type:

                if "#kino" in (msg.message or "").lower():

                    html += f"""

                    <div style="
                        background:#222;
                        padding:15px;
                        margin-bottom:20px;
                        border-radius:15px;
                    ">

                    <h3 style="margin-bottom:10px">
                        {msg.message or "Kino"}
                    </h3>

                    <video
                        width="100%"
                        controls
                        playsinline
                        webkit-playsinline
                        preload="auto"
                        controlsList="nodownload"
                        x5-video-player-type="h5"
                        x5-video-player-fullscreen="true"
                        style="
                            border-radius:12px;
                            background:black;
                            max-height:80vh;
                        "
                    >
                        <source
                        src="/stream/{msg.id}"
                        type="video/mp4">
                    </video>

                    </div>
                    """

    html += "</body></html>"

    return html


@app.route("/serials")
def serials():

    messages = loop.run_until_complete(
        client.get_messages(CHANNEL, limit=100)
    )

    html = """
    <html>

    <head>
        <meta name="viewport"
        content="width=device-width, initial-scale=1.0">

        <title>NevDub Seriallar</title>
    </head>

    <body style="
        background:#111;
        color:white;
        font-family:sans-serif;
        margin:0;
        padding:10px;
    ">

    <h1 style="text-align:center">
        Seriallar
    </h1>
    """

    for msg in messages:

        if msg.file and msg.file.mime_type:

            if "video" in msg.file.mime_type:

                if "#serial" in (msg.message or "").lower():

                    html += f"""

                    <div style="
                        background:#222;
                        padding:15px;
                        margin-bottom:20px;
                        border-radius:15px;
                    ">

                    <h3 style="margin-bottom:10px">
                        {msg.message or "Serial"}
                    </h3>

                    <video
                        width="100%"
                        controls
                        playsinline
                        webkit-playsinline
                        preload="auto"
                        controlsList="nodownload"
                        x5-video-player-type="h5"
                        x5-video-player-fullscreen="true"
                        style="
                            border-radius:12px;
                            background:black;
                            max-height:80vh;
                        "
                    >
                        <source
                        src="/stream/{msg.id}"
                        type="video/mp4">
                    </video>

                    </div>
                    """

    html += "</body></html>"

    return html


if __name__ == "__main__":
    app.run(debug=True)
