import pygame
import random
import button


pygame.init()

clock = pygame.time.Clock()
fps = 60

# game window
bottom_panel = 150
screen_width = 1280
screen_height = 550 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

# define game variables
current_fighter = 1
total_fighters = 2
action_cooldown = 0
action_wait_time = 90
attack = False
clicked = False
game_over = 0

# define fonts
font = pygame.font.SysFont('Times New Roman', 26)

# define colours
red = (255, 0, 0)
green = (0, 255, 0)


# load images
# background image
background_img = pygame.image.load('Image/Background/Beginning.png').convert_alpha()
# conversation panel image
panel_img = pygame.transform.scale(pygame.image.load('Image/Background/panel.png'),(1280, 150)).convert_alpha()

# button images
attack_img = pygame.image.load('Image/Icons/attack.png').convert_alpha()
restart_img = pygame.image.load('Image/Icons/try_again.png').convert_alpha()
tavern_img = pygame.image.load('Image/Icons/Tavern.png').convert_alpha()
# load victory and defeat images
victory_img = pygame.image.load('Image/Icons/victory.png').convert_alpha()
defeat_img = pygame.image.load('Image/Icons/defeat.png').convert_alpha()
# cursor image

#load images
#background image
background_img = pygame.image.load('Image/Background/Beginning.png').convert_alpha()
#panel image
panel_img = pygame.transform.scale(pygame.image.load('Image/Background/panel.png'),(1280, 150)).convert_alpha()

# #button images
attack_img = pygame.image.load('Image/Icons/attack.png').convert_alpha()
restart_img = pygame.image.load('Image/Icons/try_again.png').convert_alpha()
tavern_img = pygame.image.load('Image/Icons/Tavern.png').convert_alpha()
# #load victory and defeat images
victory_img = pygame.image.load('Image/Icons/victory.png').convert_alpha()
defeat_img = pygame.image.load('Image/Icons/defeat.png').convert_alpha()
#cursor image

cursor_img = pygame.transform.scale(pygame.image.load('Image/Icons/cursor.png'), (20,20)).convert_alpha()


# create function for drawing text
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

# function for drawing background
def draw_bg():
    screen.blit(background_img, (0, 0))


# function for drawing conversation panel
def draw_panel():
    # draw panel rectangle
    screen.blit(panel_img, (0, screen_height - bottom_panel))
	# show hero stats
    draw_text(f'{hero.name} HP: {hero.hp}', font, red, 100, screen_height - bottom_panel + 10)
    draw_text(f'{thief.name} HP: {thief.hp}', font, red, 1000, screen_height - bottom_panel + 10) 

# fighter class
class Fighter():
    def __init__(self, x, y, name, max_hp, strength):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self.image = pygame.image.load(f'Image/Character/{self.name}/0.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)

    def attack(self, target):
		# deal damage to enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        # check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            # target.death()
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)

    def reset (self):
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
		# calculate health ratio
		ratio = self.hp / self.max_hp
		pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
		pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))

# show damage amount on the screen
class DamageText(pygame.sprite.Sprite):
	def __init__(self, x, y, damage, colour):
		pygame.sprite.Sprite.__init__(self)
		self.image = font.render(damage, True, colour)
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.counter = 0

	def update(self):
		# move damage text up
		self.rect.y -= 1
		# delete the text after a few seconds
		self.counter += 1
		if self.counter > 30:
			self.kill()

# create damage text
damage_text_group = pygame.sprite.Group()

# create characters
hero = Fighter(500, 400, 'Hero', 30, 10)
thief = Fighter(900, 400, 'Thief', 20, 6)

# create hp bars
hero_health_bar = HealthBar(100, screen_height - bottom_panel + 40, hero.hp, hero.max_hp)
thief_health_bar = HealthBar(1000, screen_height - bottom_panel + 40, thief.hp, thief.max_hp)

# create buttons
attack_button = button.Button(screen, 100, screen_height - bottom_panel + 70, attack_img, 151, 63)
restart_button = button.Button(screen, 1000, screen_height - bottom_panel + 70, restart_img, 192, 63)
tavern_button = button.Button(screen, 1000, screen_height - bottom_panel + 70, tavern_img, 250, 63)

#Running the game
run = True
while run:

    clock.tick(fps)

    # draw background
    draw_bg()

    # draw fighters
    hero.draw()
    thief.draw()

	# draw the damage text
    damage_text_group.update()
    damage_text_group.draw(screen)

    # draw conversation panel
    draw_panel()

    # draw hp bars
    hero_health_bar.draw(hero.hp)
    thief_health_bar.draw(thief.hp)

	# control player actions
    attack = False
    target = None

    # attack button action
    if attack_button.draw() and thief.alive == True:  
        attack = True
        target = thief

    if game_over == 0:
    # player action
        if hero.alive == True:
            if current_fighter == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    # look for player action
                    # attack
                    if attack == True and target != None:
                        hero.attack(target)
                        current_fighter += 1
                        action_cooldown = 0

        # Enemy action
        if current_fighter == 2:
            if thief.alive == True:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    thief.attack(hero)
                    current_fighter += 1
                    action_cooldown = 0

            # if all fighters have had a turn then reset
            if current_fighter > total_fighters:
                current_fighter = 1

    # check if thief is dead
    alive_thieves = 0
    if thief.alive == True:
        alive_thieves += 1
    if alive_thieves == 0:
        game_over = 1

    # check if game is over
    if game_over != 0:
        if game_over == 1:
            screen.blit(victory_img, (250, 50))
            if tavern_button.draw():
                # close pygame ifvictory and open tavern scene
                pygame.quit()
                import Tavern_win

                # if defeat, restart the fight 
                if game_over == -1:
                    screen.blit(defeat_img, (290, 50))
                    if restart_button.draw():
                        hero.reset()
                        thief.reset()
                        current_fighter = 1
                        action_cooldown
                        game_over = 0

    # hide the original mouse pointer
    pygame.mouse.set_visible(False)
    # show custom cursor in place of mouse cursor
    pos = pygame.mouse.get_pos()
    screen.blit(cursor_img, pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
            else:
                clicked = False

    pygame.display.update()

pygame.quit()