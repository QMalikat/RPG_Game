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
conversation = [{
    "type": "text",
    "text": "The tavern smells of smoked meat, spilled ale, and candle wax."
    "The murmur of conversation fades as the door creaks shut behind you."
    },
    {
    "type": "text", 
    "text": "Behind the counter stands an older man with a neatly trimmed white beard, his eyes sharp and wary."
    },
    {
    "type": "choice", 
    "text": "What will you do?", 
    "choices": [
        {"label": "Ask for ale", "command": lambda: Choose_ale()},
        {"label": "Ask for wine", "command": lambda: Choose_wine()},
    ]}
]

def Choose_ale():           
    global current_step
    # Remove the last index from "conversation"
    conversation.pop()
    # Add new items to conversation list
    conversation.append({
        "type": "text",
        "text": "Ah, you'd like a drink, eh? Well… someone broke in last night and stole everything. I've got nothing left to sell."
    
    })
    conversation.append({
        "type": "text",
        "text": "He leans closer, lowering his voice."
    })
    conversation.append({
        "type": "text",
        "text": "But… there's a trail of broken glass and spilled liquor leading into the alley behind the tavern."
    })
    conversation.append({
        "type": "text",
        "text": "If you can track down the thief and recover what's mine, the first drink of my finest mead is on the house"
    })
    conversation.append({
            "type": "choice", 
    "text": "What will you do?", 
    "choices": [
        {"label": "Help the barkeep", "command": lambda: Help_barkeep()},
    ]})

    # Reset the conversation list step to index 0
    current_step = len(conversation) - 5
    show_step()

def Help_barkeep():
    root.destroy()
    import Follow

def Choose_wine():
    global current_step
    # Remove the last index from "conversation"
    conversation.pop()
    # Add new items to conversation list
    conversation.append({
        "type": "text",
        "text": "Ah, you'd like a drink, eh? Well… someone broke in last night and stole everything. I've got nothing left to sell."
    })
    conversation.append({
        "type": "text",
        "text": "He leans closer, lowering his voice."
    })
    conversation.append({
        "type": "text",
        "text": "But… there's a trail of broken glass and spilled liquor leading into the alley behind the tavern."
    })
    conversation.append({
        "type": "text",
        "text": "If you can track down the thief and recover what's mine, the first drink of my finest mead is on the house"
    })
    conversation.append({
            "type": "choice", 
    "text": "What will you do?", 
    "choices": [
        {"label": "Help the barkeep", "command": lambda: Help_barkeep()},
    ]})
    # Reset the conversation list step to index 0
    current_step = len(conversation) - 5
    show_step()



# Grid framework for layout
root.grid_rowconfigure(0, weight=0)  # Background image
root.grid_rowconfigure(1, weight=1)  # Characters pictures & conversation
root.grid_rowconfigure(2, weight=0)  # Buttons
root.grid_columnconfigure(0, weight=0)  # Hero
root.grid_columnconfigure(1, weight=1)  # Text
root.grid_columnconfigure(2, weight=0)  # NPC

#Background image - Needs to be png files
#Nice to have: Background pictures that gets bigger with the window
Bg_image_path = resource_path("Game/Image/Background/TavernIn.png")
Bg_image = Image.open(Bg_image_path)
Bg_image = Bg_image.resize((1280, 500))  
tk_image = ImageTk.PhotoImage(Bg_image)

background_label = Label(root, image=tk_image)
background_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

#Character pictures - Hero
hero_image_path = resource_path("Game/Image/Character/Hero.png")
hero_image = Image.open(hero_image_path)
hero_image = hero_image.resize((120, 120))
hero_tk = ImageTk.PhotoImage(hero_image)

hero_label = Label(root, image=hero_tk, bg='#000000')
hero_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

#Character pictures - Swift NPC with name of picture
npc_image_path = resource_path("Game/Image/Character/Barkeep.png")
npc_image = Image.open(npc_image_path)
npc_image = npc_image.resize((120, 120))
npc_tk = ImageTk.PhotoImage(npc_image)

npc_label = Label(root, image=npc_tk, bg='#000000')
npc_label.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

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