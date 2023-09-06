import pygame.sprite


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, group):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


class Grass(pygame.sprite.Sprite):
    def __init__(self, pos, surf, group):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


class Background:
    def __init__(self):
        super().__init__()
        self.bg_img = 1
        self.image = pygame.image.load(f'graphics/bg/background_{self.bg_img}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 0))

    def change_background(self):
        self.image = pygame.image.load(f'graphics/bg/background_{self.bg_img}.png').convert_alpha()


