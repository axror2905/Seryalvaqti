from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
