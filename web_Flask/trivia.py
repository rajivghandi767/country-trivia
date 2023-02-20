import sqlite3
from sqlite3 import Error
import pandas as pd
import random
from flask import Flask,render_template, request, flash, g


app = Flask(__name__)
app.secret_key = "WPJxVU!w8CW$0Vzty&CM"


#Landing Page w/ Play Button

@app.route("/")
def home():
    return render_template("index.html")

#Game Page w/ Trivia Prompts

def trivia_prompt():
    flash ("What is the Capital City of: ")

@app.route("/trivia.html")
def trivia():
    data = fetch_sql_db()
    return str(data)
    # trivia_prompt()
    # return render_template("trivia.html")


game_data = pd.read_csv("static/data/country_capitals.csv")
game_data.columns = game_data.columns.str.strip()

def fetch_sql_db ():
    connection = getattr(g, '_database', None)
    try:
        connection = g.database = sqlite3.connect("static/data/country_capitals.db")
        print("Connection to DB Successful")
    except Error as e:
        print(f"Error: {e} has occured")
    
    game_data.to_sql("game_data", connection, if_exists="replace")
    cursor=connection.cursor()
    cursor.execute("select * from game_data")
    return cursor.fetchall()
    
@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_database', None)
    if connection is not None:
        connection.close()  
    
if __name__ == '__main__': trivia.run()