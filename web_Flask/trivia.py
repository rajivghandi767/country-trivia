import sqlite3
from sqlite3 import Error
import pandas as pd
import random
from flask import Flask, render_template, request, flash, g
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from os import environ
from Bard import Chatbot

app = Flask(__name__)
app.secret_key = "WPJxVU!w8CW$0Vzty&CM"

# token = environ.get("BARD_TOKEN")
# chatbot = Chatbot(token)

# DB Connection Open

csv_data = pd.read_csv("static/data/country_capitals.csv")
csv_data.columns = csv_data.columns.str.strip()


def fetch_sql_db():
    with app.app_context():
        connection = getattr(g, '_database', None)
        try:
            connection = g.database = sqlite3.connect("static/data/country_capitals.db")
            print("Connection to DB Successful")
        except Error as e:
            print(f"Error: {e} has occured")

        csv_data.to_sql("game_data", connection, if_exists="replace")
        cursor = connection.cursor()
        cursor.execute("select country,capital from game_data")
        country_city_pair = cursor.fetchall()

        return country_city_pair


game_data = fetch_sql_db()
shuffled_game_data = random.sample(game_data, len(game_data))

# Landing Page w/ Play Button


@app.route("/")
def home():
    return render_template("index.html")

# Answer Form


class AnswerForm(FlaskForm):
    answer = StringField(validators=[DataRequired()])
    check_answer = SubmitField("Check Answer")

# Game Page w/ Trivia Question


@app.route("/trivia.html", methods=["GET", "POST"])
def trivia():

    print(game_data[0][0])
    print(shuffled_game_data[0][1])
    form = AnswerForm()
    prompt = (f"What is the Capital City of: {shuffled_game_data[0][0]}")

    # Answer Check

    if form.is_submitted():
        result = request.form
        ans = list(result.items())
        print(ans)
        print(game_data[0][1])

        if shuffled_game_data[0][1] == ans[0][1]:
            flash(f"Correct! The capital city of {shuffled_game_data[0][0]} is {shuffled_game_data[0][1]}.")
        else:
            flash("Incorrect, Try Again!")

    return render_template("trivia.html", prompt=prompt, form=form)


# Page Not Found
@app.errorhandler(404)
def page_no_found(e):
    return render_template("404.html"), 404

# Server Error


@app.errorhandler(500)
def page_no_found(e):
    return render_template("500.html"), 500

# Close DB


@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_database', None)
    if connection is not None:
        connection.close()


if __name__ == '__main__':
    trivia.run()
