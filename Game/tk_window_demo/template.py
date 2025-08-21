import os
import sys
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Parth to resource files
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Conversation step variable
current_step = 0

def create_template(container, switch_page):
    template = tk.Frame(container)


    # SCENE CONVERSATION DATA & FUNCTIONS
    conversation = [
        {"type": "text", "text": "You are standing in a dark alley. A black cat hisses at you, its eyes glinting in the dim light."},
        {"type": "text", "text": "Your throat is dry and you desperately need something to drink."},
        {"type": "choice", "text": "What will you do?", "choices": [
            {"label": "Go to Tavern", "command": lambda: Choose_tavern()},
            {"label": "Stay in the alley", "command": lambda: Choose_stay()},
        ]}
    ]

    #New scene function
    def Choose_tavern():
        switch_page("tavern")

    #New scene function
    def Choose_stay():
        switch_page("stay")

    # Grid framework for layout
    template.grid_rowconfigure(0, weight=0)  # Background image
    template.grid_rowconfigure(1, weight=1)  # Characters pictures & conversation
    template.grid_rowconfigure(2, weight=0)  # Buttons
    template.grid_columnconfigure(0, weight=0)  # Hero
    template.grid_columnconfigure(1, weight=1)  # Text
    template.grid_columnconfigure(2, weight=0)  # NPC

    #Background image - Needs to be png files
    #Nice to have: Background pictures that gets bigger with the window
    Bg_image_path = resource_path("Image/Background/Beginning.png")
    Bg_image = Image.open(Bg_image_path)
    Bg_image = Bg_image.resize((1280, 500), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(Bg_image)

    background_label = Label(template, image=tk_image)

    background_label.image = tk_image

    background_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

    # Button frame for choices

    button_frame = Frame(template, bg="#000000")

    button_frame.grid(row=2, column=0, columnspan=3, sticky="nsew") 
    
    #Character pictures - Hero
    hero_image_path = resource_path("Image/Character/Hero.png")
    hero_image = Image.open(hero_image_path)
    hero_image = hero_image.resize((200, 200))
    hero_tk = ImageTk.PhotoImage(hero_image)

    hero_label = Label(template, image=hero_tk, bg='#000000')

    hero_label.image = hero_tk

    hero_label.grid(row=1, rowspan=2, column=0, sticky="nsew")

    #Conversation text
    Conversation = Label(template, text="", bg='#000000', fg='#FFFFFF', font=('Arial', 20), wraplength=800)
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
    return template
