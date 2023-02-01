from tkinter import *
from tkinter import ttk
import sqlite3
from sqlite3 import Error

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# user = input('Name: ')
# user_country = input('Country: ')

# def greet_prompt():
#     greet_prompt = input("Hello " + user + ". Are you ready to play? ")
#     greet_prompt.capitalize()

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

root = Tk()
root.title("Country Trivia Game")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)
    
root.mainloop()