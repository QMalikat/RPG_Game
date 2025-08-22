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


def create_page1(container, switch_page):
    page = tk.Frame(container)
        # Grid framework for layout
    page.grid_rowconfigure(0, weight=0)  # Background image
    page.grid_rowconfigure(1, weight=1)  # Characters pictures & conversation
    page.grid_rowconfigure(2, weight=0)  # Buttons
    page.grid_columnconfigure(0, weight=0)  # Hero
    page.grid_columnconfigure(1, weight=1)  # Text
    page.grid_columnconfigure(2, weight=0)  # NPC

    #Background image - Needs to be png files
    #Nice to have: Background pictures that gets bigger with the window
    Bg_image_path = resource_path("Image/Background/Fight.png")
    Bg_image = Image.open(Bg_image_path)
    Bg_image = Bg_image.resize((1280, 720))  
    tk_image = ImageTk.PhotoImage(Bg_image)

    background_label = Label(page, image=tk_image)
    background_label.image = tk_image
    background_label.grid(row=0, column=0, rowspan=3,columnspan=3, sticky="nsew")
    
    tk.Label(page, text="Mead & Misery", font=("Times new roman", 50)).grid(row=0, column=1,pady=20)

    tk.Button(
        page, text="Start",
        font=("Arial", 20),
        command=lambda: switch_page("template")).grid(row=2, column=1, pady=30)

    return page
