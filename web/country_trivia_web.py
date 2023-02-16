from flask import Flask
import sqlite3
from sqlite3 import Error
import pandas as pd
from numpy import random

game_data = pd.read_csv("data/country_capitals.csv")
game_data.columns = game_data.columns.str.strip()

def fetch_sql_db (path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to DB Successful")
    except Error as e:
        print(f"Error: {e} has occured")
    
    game_data.to_sql("Country Data", connection, if_exists="replace")
    # cursor=connection.cursor()
    # cursor.execute()
    # cursor.fetchall()
    connection.close()