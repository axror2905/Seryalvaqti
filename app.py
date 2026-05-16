from flask import Flask, render_template, send_from_directory, request
from telethon import TelegramClient
import asyncio

app = Flask(__name__)

api_id = 21300715
api_hash = "cb468aebfc14cc75a36ac500bbb59988"

VIP_GROUP = "@newdubtest"

SECRET_PATH = "axror_secret_2026"

client = TelegramClient("session", api_id, api_hash)
client.start()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

async def check_user(user_id):
    try:
        member = await client.get_permissions(VIP_GROUP, user_id)
        return member is not None
    except:
        return False


@app.route(f"/{SECRET_PATH}")
def home():

    user_id = request.args.get("id")

    if not user_id:
        return "❌ Ruxsat yo‘q"

    user_id = int(user_id)

    allowed = loop.run_until_complete(check_user(user_id))

    if not allowed:
        return "❌ VIP guruhda emassiz"

    return render_template("home.html")


@app.route("/movies")
def movies():

    user_id = request.args.get("id")

    if not user_id:
        return "❌ Ruxsat yo‘q"

    user_id = int(user_id)

    allowed = loop.run_until_complete(check_user(user_id))

    if not allowed:
        return "❌ VIP guruhda emassiz"

    movies = [
        {
            "text": "🎬 Test Kino",
            "link": f"/watch/1?id={user_id}"
        }
    ]

    return render_template("movies.html", movies=movies)


@app.route("/watch/<int:msg_id>")
def watch(msg_id):

    user_id = request.args.get("id")

    if not user_id:
        return "❌ Ruxsat yo‘q"

    user_id = int(user_id)

    allowed = loop.run_until_complete(check_user(user_id))

    if not allowed:
        return "❌ VIP guruhda emassiz"

    video = "downloads/movie.mp4"

    return render_template("watch.html", video=video)


@app.route('/downloads/<path:filename>')
def download_file(filename):
    return send_from_directory('downloads', filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
