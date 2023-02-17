from flask import Flask,render_template, request, flash


app = Flask(__name__)
app.secret_key = "WPJxVU!w8CW$0Vzty&CM"


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/trivia.html")
def trivia():
    return render_template("trivia.html")