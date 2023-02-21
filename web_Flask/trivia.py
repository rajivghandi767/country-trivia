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
    # game_data = [str(val) for val in game_data]
    
    random.shuffle(game_data)
    final_game_data = dict(game_data)
    
    return final_game_data

def trivia_prompt(capitals):
    for i in capitals:
        flash (f"What is the Capital City of: {i}")
        return 

#Game Page w/ Trivia Question

@app.route("/trivia.html")
def trivia():
    data = fetch_sql_db()
    # return str(data)
    trivia_prompt(data)
    return render_template("trivia.html", final_game_data=data)

#Answer Check
  
#   def result_check(answer):
#       for x,y in country_capital_pair:
#           while prompt == x:
#               if answer == y:
#                   return ("Correct!")
#               else:
#                   return ("Incorrect, Try Again!")
      
    
@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_database', None)
    if connection is not None:
        connection.close()  
    
if __name__ == '__main__': trivia.run()