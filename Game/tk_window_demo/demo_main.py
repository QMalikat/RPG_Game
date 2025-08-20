import tkinter as tk
from tkinter import *
from page1 import create_page1
from page2 import create_page2
from page3 import create_page3
from scene import create_scene

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
    elif page_name == "page2":
        current_frame = create_page2(container, switch_page)
    elif page_name == "page3":
        current_frame = create_page3(container, switch_page)
    elif page_name == "scene":
        current_frame = create_scene(container, switch_page)

    # Display the new page
    current_frame.pack(fill="both", expand=True)

# Show first page by default
switch_page("page1")

root.mainloop()
