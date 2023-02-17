from flask import Flask,render_template, request, flash


app = Flask(__name__)
app.secret_key = "WPJxVU!w8CW$0Vzty&CM"


@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/enter", methods=["POST", "GET"])
def trivia_prompt():
    flash ("Question Placeholder")

@app.route("/trivia.html")
def trivia():
    trivia_prompt()
    return render_template("trivia.html")