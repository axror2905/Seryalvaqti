from flask import Flask, render_template, send_from_directory, request, redirect, session
from telethon import TelegramClient

app = Flask(__name__)

app.secret_key = "nevdub_secret_key"

api_id = 21300715
api_hash = "cb468aebfc14cc75a36ac500bbb59988"

VIP_GROUP = "@newdubtest"

SECRET_PATH = "axror_secret_2026"

client = TelegramClient("session", api_id, api_hash)
client.start()

def is_logged_in():
    return session.get("logged_in")

@app.route("/auth")
def auth():

    user_id = request.args.get("id")

    if not user_id:
        return "❌ Login xato"

    user_id = int(user_id)

    try:

        member = client.loop.run_until_complete(
            client.get_permissions(VIP_GROUP, user_id)
        )

        if not member:
            return "❌ VIP emas"

    except:
        return "❌ VIP guruhda emassiz"

    session["logged_in"] = True

    return redirect(f"/{SECRET_PATH}")

@app.route(f"/{SECRET_PATH}")
def home_page():
    return render_template("home.html")

@app.route("/movies")
def movies():

    if not is_logged_in():
        return "❌ Ruxsat yo‘q"

    movies = [
        {
            "text": "🎬 Test Kino",
            "link": "/watch/1"
        }
    ]

    return render_template("movies.html", movies=movies)

@app.route("/watch/<int:msg_id>")
def watch(msg_id):

    if not is_logged_in():
        return "❌ Ruxsat yo‘q"

    video = "downloads/movie.mp4"

    return render_template("watch.html", video=video)

@app.route('/downloads/<path:filename>')
def download_file(filename):
    return send_from_directory('downloads', filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
