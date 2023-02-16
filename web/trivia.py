from flask import Flask,render_template, request, flash


app = Flask(__name__)
app.secret_key = "WPJxVU!w8CW$0Vzty&CM"


@app.route("/")
def index():
    return render_template("index.html")

