import os
import pygame
import tkinter as tk
from tkinter import *
import Text_button as button
import random

def create_main(container, switch_page):
    # game window
    bottom_panel = 150
    screen_width = 1280
    screen_height = 550 + bottom_panel

    # embed frame
    main = tk.Frame(container, width=screen_width, height=screen_height)
    main.pack(side=LEFT)
    # main.config(cursor="none")

    # must happen before pygame.init()
    os.environ['SDL_WINDOWID'] = str(main.winfo_id())
    os.environ['SDL_VIDEODRIVER'] = 'windib'

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Battle')

    clock = pygame.time.Clock()
    fps = 60

    # define game variables
    current_fighter = 1
    total_fighters = 2
    action_cooldown = 0
    action_wait_time = 90
    game_over = 0

    # define fonts
    font = pygame.font.SysFont('Times New Roman', 28)
    font2 = pygame.font.SysFont('Times New Roman', 70)

    # define colours
    red = (255, 0, 0)
    green = (0, 255, 0)
    White = (255, 255, 255)

    # load images
    background_img = pygame.image.load('Image/Background/Fight.2.png').convert_alpha()
    panel_img = pygame.transform.scale(pygame.image.load('Image/Background/panel.png'), (1280, 150)).convert_alpha()
    victory_img = pygame.image.load('Image/Icons/victory.png').convert_alpha()
    defeat_img = pygame.image.load('Image/Icons/defeat.png').convert_alpha()
    # cursor_img = pygame.transform.scale(pygame.image.load('Image/Icons/cursor.png'), (20, 20)).convert_alpha()

    # create function for drawing text
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    def draw_bg():
        screen.blit(background_img, (0, 0))

    def draw_panel():
        screen.blit(panel_img, (0, screen_height - bottom_panel))
        draw_text(f'{hero.name} HP: {hero.hp}', font, White, 100, screen_height - bottom_panel + 10)
        draw_text(f'{thief.name} HP: {thief.hp}', font, White, 1000, screen_height - bottom_panel + 10)

    # fighter class
    class Fighter():
        def __init__(self, x, y, name, max_hp, strength):
            self.name = name
            self.max_hp = max_hp
            self.hp = max_hp
            self.strength = strength
            self.alive = True
            self.image = pygame.image.load(f'Image/Character/{self.name}/0.1.png')
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

        def draw(self):
            screen.blit(self.image, self.rect)

        def attack(self, target):
            rand = random.randint(-5, 5)
            damage = self.strength + rand
            target.hp -= damage
            if target.hp < 1:
                target.hp = 0
                target.alive = False
            damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
            damage_text_group.add(damage_text)

        def reset(self):
            self.alive = True
            self.hp = self.max_hp

    class HealthBar():
        def __init__(self, x, y, hp, max_hp):
            self.x = x
            self.y = y
            self.hp = hp
            self.max_hp = max_hp

        def draw(self, hp):
            self.hp = hp
            ratio = self.hp / self.max_hp
            pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
            pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))

    class DamageText(pygame.sprite.Sprite):
        def __init__(self, x, y, damage, colour):
            pygame.sprite.Sprite.__init__(self)
            self.image = font2.render(damage, True, colour)
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.counter = 0

        def update(self):
            self.rect.y -= 1
            self.counter += 1
            if self.counter > 30:
                self.kill()

    damage_text_group = pygame.sprite.Group()

    # create characters
    hero = Fighter(400, 400, 'Hero', 30, 8)
    thief = Fighter(1000, 400, 'Thief', 30, 8)

    hero_health_bar = HealthBar(100, screen_height - bottom_panel + 40, hero.hp, hero.max_hp)
    thief_health_bar = HealthBar(1000, screen_height - bottom_panel + 40, thief.hp, thief.max_hp)

    # buttons
    attack_button = button.Button(screen, 300, screen_height - bottom_panel + 70, 200, 63, "Attack", font)
    win_button = button.Button(screen, 550, screen_height - bottom_panel + 70, 200, 63, "You win", font)
    lose_button = button.Button(screen, 800, screen_height - bottom_panel + 70, 200, 63, "You lose", font)

    # --- MAIN GAME LOOP FUNCTION (replaces while run:) ---
    running = True

    def game_loop():
        nonlocal current_fighter, action_cooldown, game_over
        if not running:
            return
        
        clock.tick(fps)

        # draw everything
        draw_bg()
        hero.draw()
        thief.draw()

        damage_text_group.update()
        damage_text_group.draw(screen)

        draw_panel()
        hero_health_bar.draw(hero.hp)
        thief_health_bar.draw(thief.hp)

        # control player actions
        attack = False
        target = None

        if attack_button.draw() and thief.alive:
            attack = True
            target = thief

        if game_over == 0:
            # player turn
            if hero.alive and current_fighter == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    if attack and target is not None:
                        hero.attack(target)
                        current_fighter += 1
                        action_cooldown = 0

            # enemy turn
            if current_fighter == 2 and thief.alive:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    thief.attack(hero)
                    current_fighter += 1
                    action_cooldown = 0

            if current_fighter > total_fighters:
                current_fighter = 1

        # check deaths
        if not thief.alive and game_over == 0:
            game_over = 1
        if not hero.alive and game_over == 0:
            game_over = -1

        if game_over != 0:
            if game_over == 1:
                screen.blit(victory_img, (500, 50))
                if win_button.draw():
                    running = False
                    pygame.quit()
                    switch_page("winner")
            if game_over == -1:
                screen.blit(defeat_img, (500, 50))
                if lose_button.draw():
                    running = False
                    pygame.quit()
                    switch_page("loser")

        # custom cursor
        # pygame.mouse.set_visible(False)
        # pos = pygame.mouse.get_pos()
        # screen.blit(cursor_img, pos)

        # process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pygame.display.update()

        # schedule next frame
        container.after(int(1000 / fps), game_loop)

    # start game loop
    game_loop()
    return main
