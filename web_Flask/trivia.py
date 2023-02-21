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

#Trivia Database & Prompts

csv_data = pd.read_csv("static/data/country_capitals.csv")
csv_data.columns = csv_data.columns.str.strip()

def fetch_sql_db ():
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
    
    random.shuffle(game_data)
    final_game_data = dict(game_data)
    
    return final_game_data

def trivia_prompt(countries):
    for country in countries:
        flash (f"What is the Capital City of: {country}")
        return 

#Game Page w/ Trivia Question

@app.route("/trivia.html")
def trivia():
    data = fetch_sql_db()
    trivia_prompt(data)
    return render_template("trivia.html")

#Answer Check

# @app.route("/user_response", methods=["POST","GET"])
# def result_check():
#     data = fetch_sql_db()
#     result = data.keys()
#     for x in result:
#         while trivia_prompt(data).keys() == x:
#             if request.form["player_answer"] == y:
#                 return ("Correct!")
#             else:
#                 return ("Incorrect, Try Again!")
#     return render_template("trivia.html")
   
@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_database', None)
    if connection is not None:
        connection.close()  
    
if __name__ == '__main__': trivia.run()