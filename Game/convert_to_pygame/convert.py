import pygame
import os
import sys
import Text_button as button

pygame.init()

clock = pygame.time.Clock()
fps = 60

# game window
bottom_panel = 150
screen_width = 1280
screen_height = 550 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

# Parth to resource files
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# define fonts
font = pygame.font.SysFont('Times New Roman', 28)
font2 = pygame.font.SysFont('Times New Roman', 70)

# SCENE CONVERSATION DATA & FUNCTIONS
conversation = [
    {"type": "text", "text": "You are standing in a dark alley. A black cat hisses at you, its eyes glinting in the dim light."},
    {"type": "text", "text": "Your throat is dry and you desperately need something to drink."},
    {"type": "choice", "text": "What will you do?", "choices": [
        {"label": "Go to Tavern", "command": lambda: Choose_tavern()},
        {"label": "Stay in the alley", "command": lambda: Choose_stay()},
    ]}
]

#New scene function
def Choose_tavern():
    root.destroy() 
    import Tavern

#New scene function
def Choose_stay():
    root.destroy() 
    import Stay