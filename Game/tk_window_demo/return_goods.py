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

def create_return_goods(container, switch_page):
    return_goods = tk.Frame(container)

    # SCENE CONVERSATION DATA & FUNCTIONS
    conversation = [
        {"type": "text", "text": 'You yell "Return what you stole from the tavern"'},
        {"type": "text", "text": "He only grins and before you can react, he lunges forward, aiming a punch straight for your stomach."},
        {"type": "choice", "text": "What will you do?", "choices": [
            {"label": "Fight back", "command": lambda: Choose_Fight()},
        ]}
    ]

    def Choose_Fight():
        return_goods.destroy() 
        import main

    # Grid framework for layout
    return_goods.grid_rowconfigure(0, weight=0)  # Background image
    return_goods.grid_rowconfigure(1, weight=1)  # Characters pictures & conversation
    return_goods.grid_rowconfigure(2, weight=0)  # Buttons
    return_goods.grid_columnconfigure(0, weight=0)  # Hero
    return_goods.grid_columnconfigure(1, weight=1)  # Text
    return_goods.grid_columnconfigure(2, weight=0)  # NPC

    #Background image - Needs to be png files
    #Nice to have: Background pictures that gets bigger with the window
    Bg_image_path = resource_path("Image/Background/Thief.png")
    Bg_image = Image.open(Bg_image_path)
    Bg_image = Bg_image.resize((1280, 500), Image.Resampling.LANCZOS)
    tk_image = ImageTk.PhotoImage(Bg_image)

    background_label = Label(return_goods, image=tk_image)

    background_label.image = tk_image

    background_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

    # Button frame for choices
    button_frame = Frame(return_goods, bg="#000000")
    button_frame.grid(row=2, column=0, columnspan=3, sticky="nsew") 

    #Character pictures - Hero
    hero_image_path = resource_path("Image/Character/Hero.png")
    hero_image = Image.open(hero_image_path)
    hero_image = hero_image.resize((200, 200))
    hero_tk = ImageTk.PhotoImage(hero_image)

    hero_label = Label(return_goods, image=hero_tk, bg='#000000')

    hero_label.image = hero_tk

    hero_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    #Character pictures - Swift NPC with name of picture
    npc_image_path = resource_path("Image/Character/Villan.png")
    npc_image = Image.open(npc_image_path)
    npc_image = npc_image.resize((200, 200))
    npc_tk = ImageTk.PhotoImage(npc_image)

    npc_label = Label(return_goods, image=npc_tk, bg='#000000')

    npc_label.image = npc_tk

    npc_label.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

    #Conversation text
    Conversation = Label(return_goods, text="", bg='#000000', fg='#FFFFFF', font=('Arial', 20), wraplength=800)
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
    return return_goods