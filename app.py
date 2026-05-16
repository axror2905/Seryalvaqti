from flask import Flask, render_template, send_from_directory, request, redirect, session

app = Flask(__name__)

app.secret_key = "nevdub_secret_key"

SECRET_PATH = "axror_secret_2026"

ALLOWED_USERS = [
    6149468647
]

def is_logged_in():

    return session.get("user_id") in ALLOWED_USERS

def login():
    return render_template("index.html")


@app.route("/auth")
def auth():
    user_id = request.args.get("id")

    if not user_id:
        return "❌ Login xato"

    user_id = int(user_id)

    if user_id not in ALLOWED_USERS:
        return "❌ VIP emas"

    session["user_id"] = user_id

    return redirect("/movies")

@app.route(f"/{SECRET_PATH}")
def home_page():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/subscription")
def subscription():
    return render_template("subscription.html")

@app.route("/watch/<int:msg_id>")
def watch(msg_id):
    if not is_logged_in():
        return "❌ Ruxsat yo‘q"

    video = "downloads/movie.mp4"

    return render_template("watch.html", video=video)

@app.route("/movies")

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

    return render_template("movies.html", movies=movies)

@app.route('/downloads/<path:filename>')
def download_file(filename):
    return send_from_directory('downloads', filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
