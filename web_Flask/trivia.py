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
        
        # random.shuffle(game_data)
        final_game_data = dict(game_data)
        
        return final_game_data

#Landing Page w/ Play Button

@app.route("/")
def home():
    return render_template("index.html")

#Answer Form

class AnswerForm(FlaskForm):
    answer = StringField(validators=[DataRequired()])
    check_answer = SubmitField("Check Answer")
    next_question = SubmitField("Next")
    

#Game Page w/ Trivia Question

@app.route("/trivia.html", methods=["GET","POST"])
def trivia():
    data = fetch_sql_db()
    country = list(data.keys())
    # random.shuffle(country)
    form = AnswerForm()
    prompt = (f"What is the Capital City of: {country[0]}")
    
    if form.is_submitted():
        result = list(request.form.values())[0]
        for k,v in data.items():
            if country[0]== k and result == v:
                flash ("Correct!")
                break
            else:
                flash ("Incorrect, Try Again")
                break
    
    return render_template("trivia.html", prompt = prompt, form=form)

#Answer Check



#Close DB
   
@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_database', None)
    if connection is not None:
        connection.close()
    
if __name__ == '__main__': trivia.run()