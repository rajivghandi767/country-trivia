import sqlite3
from sqlite3 import Error
import pandas as pd
import random
from flask import Flask,render_template, request, flash, g
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "WPJxVU!w8CW$0Vzty&CM"

#DB Connection Open

csv_data = pd.read_csv("static/data/country_capitals.csv")
csv_data.columns = csv_data.columns.str.strip()

def fetch_sql_db ():
    with app.app_context():
        connection = getattr(g, '_database', None)
        try:
            connection = g.database = sqlite3.connect("static/data/country_capitals.db")
            print("Connection to DB Successful")
        except Error as e:
            print(f"Error: {e} has occured")
        
        csv_data.to_sql("game_data", connection, if_exists="replace")
        cursor=connection.cursor()
        cursor.execute("select country,capital from game_data")
        game_data = cursor.fetchall()
        
        return game_data

#Landing Page w/ Play Button

@app.route("/")
def home():
    return render_template("index.html")

#Answer Form

class AnswerForm(FlaskForm):
    answer = StringField(validators=[DataRequired()])
    check_answer = SubmitField("Check Answer")

#Game Page w/ Trivia Question

@app.route("/trivia.html", methods=["GET","POST"])
def trivia():
    data = fetch_sql_db()
    shuffled_data = random.sample(data, len(data))
    form = AnswerForm()
    prompt = (f"What is the Capital City of: {shuffled_data[0][0]}")
    
    #Answer Check
    
    if form.is_submitted():
        result = request.form.values()
        for country in shuffled_data:
            if result == shuffled_data[0][1]:
                flash ("Correct!")
                break
            else:
                flash ("Incorrect, Try Again!")
                break
        
    return render_template("trivia.html", prompt = prompt, form=form)

#Close DB
   
@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_database', None)
    if connection is not None:
        connection.close()
    
if __name__ == '__main__': 
    trivia.run()