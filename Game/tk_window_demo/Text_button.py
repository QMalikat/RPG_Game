import pygame

# Button class - text-based
class Button():
    def __init__(self, surface, x, y, width, height, text, font, 
                 text_color=(0,0,0),
                 color=(255,255,255), 
                 hover_color=(150, 150, 150)):
        self.surface = surface
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.text_color = text_color
        self.color = color
        self.hover_color = hover_color
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        # check hover
        if self.rect.collidepoint(pos):
            pygame.draw.rect(self.surface, self.hover_color, self.rect)
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
        else:
            pygame.draw.rect(self.surface, self.color, self.rect)

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # render text
        text_img = self.font.render(self.text, True, self.text_color)
        text_rect = text_img.get_rect(center=self.rect.center)
        self.surface.blit(text_img, text_rect)

        return action