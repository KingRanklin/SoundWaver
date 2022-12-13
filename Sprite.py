import pygame


class Sprite(pygame.sprite.Sprite):

    def __init__(self, x, y, img_path, w_scaling=None, h_scaling=None):
        """
        Constructor for custom Sprite class.

        :param int x: number indicating the value of the X axis this sprite will display on
        :param int y: number indicating the value of the Y axis this sprite will display on
        :param str img_path: relative path of image
        """

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        if img_path is not None:
            self.image = pygame.image.load(img_path)
            if w_scaling is not None and h_scaling is not None:
                self.scale_image(w_scaling, h_scaling)
            else:
                self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x, y

        # TODO this should be removed at some point :\
        self.show_hitbox = False

    def toggle_hitbox(self, bool):
        self.show_hitbox = bool

    def display_hitbox(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

    def is_collided_with(self, sprite):
        """
        Check if the passed sprite collides with this sprite.
        :param sprite: Sprite object, must have a defined rect
        :return:  True if the two sprites collide, false otherwise
        """
        return self.rect.colliderect(sprite.rect)

    def scale_image(self, w, h):
        """
        Utility function to re-scale the sprite's image.

        :param int w: number value of the desired width
        :param int h: number value of the desired height
        """
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
