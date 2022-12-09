import pygame


class Sprite(object):
    def __init__(self, x, y, img_path):
        self.x = x
        self.y = y
        self.img = pygame.image.load(img_path)
        self.show_hitbox = False
        self.rect = pygame.Rect(self.x, self.y, 32, 32)  # The rect for collision detection.

    def toggle_hitbox(self, bool):
        self.show_hitbox = bool

    def display_hitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

    def scale_image(self, x, y):
        self.img = pygame.transform.scale(self.img, (x, y))
        self.rect.update(self.x, self.y, x, y)

class staticObject:
    def __init__(self, x, y, rect):
        self.x = x
        self.y = y
        self.rect = 1