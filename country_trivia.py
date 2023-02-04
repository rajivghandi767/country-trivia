from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import sqlite3
from sqlite3 import Error
import pandas as pd
from numpy import random

game_data = pd.read_csv("country_capitals.csv")
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

def start_page():
    frame1.pack_propagate(False)

    Label(frame1, text="Welcome to Country Trivia! \n \n Press PLAY to begin!",
        fg="white",
        font=("TkMenuFont", 14)).pack(pady=20)

    Button(frame1, text="PLAY",
        font=("TkMenuFont", 14),
        bg="#FFFFFF",
        fg="black",
        cursor="hand2",
        activebackground="#FFFFFF",
        activeforeground="black",
        command=lambda:print("Play!")).pack(pady=20) 

def info_page():
    pass
    # trivia_id = input('Trivia Master Moniker: ')
    # print("Hello " + trivia_id + ". Let's begin!")

def game_page():
    pass
    # guess_capital = input('What is the capital of ?')
    # guess_country = input(' is the capital of what country?')

def score_sheet():
    pass

root = Tk()
root.title("Country Trivia Game")
root.eval("tk::PlaceWindow . center")

frame1 = ttk.Frame(root, width=400, height=200)
frame1.grid(row=0, column=0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fetch_sql_db("country_capitals.db")
start_page()
root.mainloop()