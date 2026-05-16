from flask import Flask, render_template, send_from_directory, request
from telethon.sync import TelegramClient
import os

app = Flask(__name__)

api_id = 21300715
api_hash = "cb468aebfc14cc75a36ac500bbb59988"

CHANNEL = "@Newdub_vip"

SECRET_PATH = "axror_secret_2026"

client = TelegramClient(
    "newsession",
    api_id,
    api_hash
).start()


@app.route(f"/{SECRET_PATH}")
def home():

    user_id = request.args.get("id")

    return render_template(
        "home.html",
        user_id=user_id
    )


@app.route("/movies")
def movies():

    user_id = request.args.get("id")

    messages = client.get_messages(CHANNEL, limit=100)

    movie_list = []

    for msg in messages:

        if msg.video and msg.text:

            if "#kino" in msg.text:

                title = msg.text.split("\n")[0]

                movie_list.append({
                    "text": title,
                    "link": f"/watch/{msg.id}?id={user_id}"
                })

    return render_template(
        "movies.html",
        movies=movie_list,
        user_id=user_id
    )


@app.route("/serials")
def serials():

    user_id = request.args.get("id")

    messages = client.get_messages(CHANNEL, limit=100)

    serials_dict = {}

    for msg in messages:

        if msg.text and "#serial" in msg.text:

            words = msg.text.split()

            tag = None

            for word in words:

                if word.startswith("#") and word != "#serial":

                    tag = word.replace("#", "")

                    break

            if tag:

                serials_dict[tag] = {
                    "name": tag.replace("_", " ").title(),
                    "link": f"/serial/{tag}?id={user_id}"
                }

    return render_template(
        "serials.html",
        serials=list(serials_dict.values()),
        user_id=user_id
    )


@app.route("/serial/<serial_name>")
def serial_detail(serial_name):

    user_id = request.args.get("id")

    messages = client.get_messages(CHANNEL, limit=100)

    episodes = []

    for msg in messages:

        if msg.video and msg.text:

            if f"#{serial_name}" in msg.text:

                title = msg.text.split("\n")[0]

                episodes.append({
                    "text": title,
                    "link": f"/watch/{msg.id}?id={user_id}"
                })

    return render_template(
        "serial_detail.html",
        episodes=episodes,
        serial_name=serial_name.replace("_", " ").title(),
        user_id=user_id
    )


@app.route("/watch/<int:msg_id>")
def watch(msg_id):

    msg = client.get_messages(CHANNEL, ids=msg_id)

    if not msg:
        return "❌ Video topilmadi"

    file_path = client.download_media(
        msg,
        file="downloads/"
    )

    video = os.path.basename(file_path)

    return render_template(
        "watch.html",
        video=video
    )


@app.route('/downloads/<path:filename>')
def download_file(filename):

    return send_from_directory(
        'downloads',
        filename
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
