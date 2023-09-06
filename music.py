import pygame


class Music:
    def __init__(self):
        self.level_theme = pygame.mixer.Sound('audio/level_1_theme.wav')
        self.level_clear_theme = pygame.mixer.Sound('audio/level_clear.wav')
        self.level_theme.set_volume(0.5)
        self.level_num = 1

    def update_music(self):
        self.level_theme = pygame.mixer.Sound(f'audio/level_{self.level_num}_theme.wav')


