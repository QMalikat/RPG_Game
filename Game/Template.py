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
root.config(bg='#FFFFFF')

#Background image - Needs to be png files
#Nice to have: Background pictures that gets bigger with the window
image_path = resource_path("Image/Background/Test.png")
image = Image.open(image_path)  
image = image.resize((1280, 720))  
tk_image = ImageTk.PhotoImage(image)

background_label = Label(root, image=tk_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#New scene function
def Choose_tavern():
    root.destroy() 
    import scene_tavern

#Need to add grid frame, so we have somewhere to put button, picture and text

#Button
button = Button(root, text="Go To Tavern", command=Choose_tavern,
                bg='#FFFFFF', fg='#000000', font=('Arial', 20))
button.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

#Conversation text

root.mainloop()