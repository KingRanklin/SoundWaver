import pygame


class Sprite(object):
    def __init__(self, x, y, img_path):
        self.x = x
        self.y = y
        self.img = pygame.image.load(img_path)
        self.show_hitbox = False

    def toggle_hitbox(self, bool):
        self.show_hitbox = bool

    def display_hitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.img.get_rect(), 2)

    def scale_image(self, x, y):
        self.img = pygame.transform.scale(self.img, (x, y))
