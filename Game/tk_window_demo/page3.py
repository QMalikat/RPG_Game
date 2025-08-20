import tkinter as tk

def create_page3(container, switch_page):
    page = tk.Frame(container)
    
    tk.Label(page, text="I am page 3", font=("Arial", 20)).pack(pady=20)

    tk.Button(
        page, text="Starter scene",
        font=("Arial", 20),
        command=lambda: switch_page("scene")).pack(pady=60)

    return page
