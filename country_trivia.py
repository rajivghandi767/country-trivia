from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import sqlite3
from sqlite3 import Error
from numpy import random

def start_page():
    frame1.pack_propagate(False)
    
        # Logo
    # logo = ImageTk.PhotoImage(file="")
    # logo_widget = Label(frame_1, image=logo, bg="#000000")
    # logo_widget.image = logo
    # logo_widget.pack()

    Label(frame1, text="Welcome to Country Trivia \n \n Press PLAY to begin!",
        fg="white",
        font=("TkMenuFont", 14)).pack(pady=20)

    Button(frame1, text="PLAY",
        font=("TkMenuFont", 14),
        bg="#FFFFFF",
        fg="black",
        cursor="hand2",
        activebackground="#FFFFFF",
        activeforeground="black",
        command=lambda:greet_prompt).pack(pady=20)

def fetch_sql_db (path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection Successful")
    except Error as e:
        print(f"Error: {e} has occured")
        
    cursor=connection.cursor()
    cursor.execute()
    cursor.fetchall()
    connection.close()

root = Tk()
root.title("Country Trivia Game")
root.eval("tk::PlaceWindow . center")

def greet_prompt():
    user = input('Name: ')
    greet_prompt = input("Hello " + user + ". Are you ready to play? ")
    greet_prompt.capitalize()

# user_country = input('Country: ')

#     if greet_prompt == 'Yes' or greet_prompt == 'Y':
#         print("Ok, let's begin!")
#     elif greet_prompt == 'No' or greet_prompt == 'N':
#         print("Ok, Maybe next time!")
#     else:
#         print("Please answer 'Yes (Y)' or 'No (N)'")

# def guess_country():
#     input('What is the capital of ?')
    
# def guess_city():
#     input(' is the capital of what country?')

frame1 = ttk.Frame(root, width=400, height=200)
frame1.grid(row=0, column=0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

start_page()
root.mainloop()