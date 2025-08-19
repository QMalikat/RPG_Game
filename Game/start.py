import tkinter as tk
from tkinter import *

# window properties
root = tk.Tk()
root.title("DnD Game")
root.configure(background="black")
#root.size(1280, 720)
root.geometry("1280x720")

# Create Frame widget
startframe = tk.Frame(root, width=1270, height=710, bg="white",)
startframe.pack(fill="both", expand=True)

def start():
    ###### = Frame(root, bg="#000000")
    ######.pack(fill="both", expand=True)
    for widget in startframe.winfo_children():
        widget.destroy()
     #   Tavern_test(root)

start_game =tk.Button(startframe, text="Start", font=('Arial', 30), command=start)
start_game.pack(expand=True)

root.mainloop()