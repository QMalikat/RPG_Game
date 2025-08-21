import tkinter as tk

def create_page1(container, switch_page):
    page = tk.Frame(container)
    
    tk.Label(page, text="NAME OF THE GAME", font=("Arial", 20)).pack(pady=20)

    tk.Button(
        page, text="Start",
        font=("Arial", 20),
        command=lambda: switch_page("template")).pack(pady=60)

    return page
