import tkinter as tk

def create_page2(container, switch_page):
    page = tk.Frame(container)

    tk.Label(page, text="I am page 2", font=("Arial", 20)).pack(pady=20)

    tk.Button(
        page, text="Go to page 3",
        font=("Arial", 20),
        command=lambda: switch_page("page3")
    ).pack(pady=60)

    return page
