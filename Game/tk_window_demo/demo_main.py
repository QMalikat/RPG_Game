import tkinter as tk
from tkinter import *
from start_screen import create_page1
from template import create_template
from tavern import create_tavern
from stay import create_stay
from follow import create_follow
from thief import create_thief
from main import create_main
from loser import create_loser
from winner import create_winner
from return_goods import create_return_goods
from tavern_win import create_tavern_win


root = tk.Tk()
root.title("Demo")
root.geometry("1280x720")
root.resizable(False, False)

container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Only one frame exists at a time
current_frame = None

# Page switch function
def switch_page(page_name):
    global current_frame

    # Destroy the current page before new one loads
    if current_frame is not None:
        current_frame.destroy()

    # Create new page on demand
    if page_name == "page1":
        current_frame = create_page1(container, switch_page)
    elif page_name == "template":
        current_frame = create_template(container, switch_page)
    elif page_name == "tavern":
        current_frame = create_tavern(container, switch_page)
    elif page_name == "stay":
        current_frame = create_stay(container, switch_page)
    elif page_name == "follow":
        current_frame = create_follow(container, switch_page)
    elif page_name == "thief":
        current_frame = create_thief(container, switch_page)
    elif page_name == "main":
        current_frame = create_main(container, switch_page)
    elif page_name == "loser":
        current_frame = create_loser(container, switch_page)
    elif page_name == "winner":
        current_frame = create_winner(container, switch_page)
    elif page_name == "return_goods":
        current_frame = create_return_goods(container, switch_page)
    elif page_name == "tavern_win":
        current_frame = create_tavern_win(container, switch_page)


    # Display the new page
    current_frame.pack(fill="both", expand=True)

# Show first page by default
switch_page("page1")

root.mainloop()
