import os
import sys
from tkinter import *
from PIL import Image, ImageTk

# Parth to resource files
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#Main window setup
root = Tk()
root.title("DnD Roleplay game")
root.geometry("1280x720")
root.config(bg='#000000')

# SCENE CONVERSATION DATA & FUNCTIONS
conversation = [
    {"type": "text", "text": "Your strike barely fazes him. He’s far stronger than you imagined. His fist connects with crushing force, and the world spins as you collapse to the cold cobblestones."},
    {"type": "text", "text": "Darkness swallows you whole."},
    {"type": "choice", "text": "What will you do?", "choices": [
        {"label": "Try again?", "command": lambda: Choose_Template()},
        {"label": "End game", "command": lambda: Choose_End_game()},
    ]}
]

#New scene function
def Choose_Template():
    root.destroy() 
    import Tenplate

#New scene function
def Choose_End_game():
    root.destroy() 

# Grid framework for layout
root.grid_rowconfigure(0, weight=0)  # Background image
root.grid_rowconfigure(1, weight=1)  # Characters pictures & conversation
root.grid_rowconfigure(2, weight=0)  # Buttons
root.grid_columnconfigure(0, weight=0)  # Hero
root.grid_columnconfigure(1, weight=1)  # Text
root.grid_columnconfigure(2, weight=0)  # NPC

#Background image - Needs to be png files
#Nice to have: Background pictures that gets bigger with the window
Bg_image_path = resource_path("Image/Background/Loser.png")
Bg_image = Image.open(Bg_image_path)
Bg_image = Bg_image.resize((1280, 500), Image.Resampling.LANCZOS)
tk_image = ImageTk.PhotoImage(Bg_image)

background_label = Label(root, image=tk_image)
background_label.grid(row=0, column=0, columnspan=3, sticky="nsew")


#Character pictures - Hero
hero_image_path = resource_path("Image/Character/Hero.png")
hero_image = Image.open(hero_image_path)
hero_image = hero_image.resize((120, 120))
hero_tk = ImageTk.PhotoImage(hero_image)

hero_label = Label(root, image=hero_tk, bg='#000000')
hero_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

#Conversation text
Conversation = Label(root, text="", bg='#000000', fg='#FFFFFF', font=('Arial', 20), wraplength=800)
Conversation.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

# Button frame for choices
button_frame = Frame(root, bg="#000000")
button_frame.grid(row=2, column=0, columnspan=3, sticky="nsew") 

# GAME FUNKTIONALITY
current_step = 0

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

root.mainloop()