from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/subscription")
def subscription():
    return render_template("subscription.html")

@app.route("/watch/<int:msg_id>")
def watch(msg_id):

    video = "downloads/movie.mp4"

    return render_template("watch.html", video=video)

@app.route("/movies")
def movies():

    movies = [
        {
            "text": "🎬 Test Kino",
            "link": "/watch/1"
        }
    ]

    return render_template("movies.html", movies=movies)

@app.route('/downloads/<path:filename>')
def download_file(filename):
    return send_from_directory('downloads', filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
