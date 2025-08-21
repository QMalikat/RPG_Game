import os
import sys
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

# Parth to resource files
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Conversation step variable
current_step = 0

def create_winner(container, switch_page):
    winner = tk.Frame(container)

    # SCENE CONVERSATION DATA & FUNCTIONS
    conversation = [
        {"type": "text", "text": "At last, after a flurry of blows, the thief staggers back, breathing heavily. His defiance melts into exhaustion."},
        {"type": "text", "text": 'He falls down to the wet cobblestone, defeated but alive.'},     
        {"type": "text", "text": '"Fine… you win," he growls. "I’ll return what’s left… and I’ll pay the tavern back for the rest.'}, 
        {"type": "choice", "text": "", "choices": [
            {"label": "Go to tavern", "command": lambda: Tavern_win()},
        ]}
    ]

    #New scene function
    def Tavern_win():
        switch_page("tavern_win")

    # Grid framework for layout
    winner.grid_rowconfigure(0, weight=0)  # Background image
    winner.grid_rowconfigure(1, weight=1)  # Characters pictures & conversation
    winner.grid_rowconfigure(2, weight=0)  # Buttons
    winner.grid_columnconfigure(0, weight=0)  # Hero
    winner.grid_columnconfigure(1, weight=1)  # Text
    winner.grid_columnconfigure(2, weight=0)  # NPC

    #Background image - Needs to be png files
    #Nice to have: Background pictures that gets bigger with the window
    Bg_image_path = resource_path("Image/Background/Winner.png")
    Bg_image = Image.open(Bg_image_path)
    Bg_image = Bg_image.resize((1280, 500), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(Bg_image)

    background_label = Label(winner, image=tk_image)

    background_label.image = tk_image

    background_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

    # Button frame for choices
    button_frame = Frame(winner, bg="#000000")
    button_frame.grid(row=2, column=0, columnspan=3, sticky="nsew") 

    #Character pictures - Hero
    hero_image_path = resource_path("Image/Character/Hero.png")
    hero_image = Image.open(hero_image_path)
    hero_image = hero_image.resize((200, 200))
    hero_tk = ImageTk.PhotoImage(hero_image)

    hero_label = Label(winner, image=hero_tk, bg='#000000')

    hero_label.image = hero_tk

    hero_label.grid(row=1, column=0, sticky="nsew")

    #Conversation text
    Conversation = Label(winner, text="", bg='#000000', fg='#FFFFFF', font=('Arial', 20), wraplength=800)
    Conversation.grid(row=1, column=1, sticky="nsew")

    # GAME FUNKTIONALITY

    def show_step():
        global current_step
        step = conversation[current_step]

        # Update the label with the current text
        Conversation.config(text=step["text"])

        #Clear buttons
        for widget in button_frame.winfo_children():
            widget.destroy()

        if step["type"] == "text":
            btn = Button(button_frame, text="Continue", font=('Arial', 20),
                        command=next_step, bg="#FFFFFF", fg="#000000")
            btn.pack(pady=10)
        
        elif step["type"] == "choice":
            for col, choice in enumerate(step["choices"]):
                btn = Button(button_frame, text=choice["label"], font=('Arial', 20),
                            command=choice["command"], bg="#FFFFFF", fg="#000000")
                btn.grid(row=0, column=col, padx=20, pady=10, sticky="nsew")
                button_frame.grid_columnconfigure(col, weight=1)
    
    def next_step():
        global current_step
        if current_step < len(conversation) - 1:
            current_step += 1
            show_step()

    show_step()
    return winner