import pygame.sprite
from settings import *

class BabCoins(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.bab_coin_pos = []
        self.bab_coin_pos.append(pos)
        self.bab_coin_1 = pygame.image.load('graphics/coins/bab_coin_frames/bab_coin1.png').convert_alpha()
        self.bab_coin_2 = pygame.image.load('graphics/coins/bab_coin_frames/bab_coin2.png').convert_alpha()
        self.bab_coin_3 = pygame.image.load('graphics/coins/bab_coin_frames/bab_coin3.png').convert_alpha()
        self.bab_coin_4 = pygame.image.load('graphics/coins/bab_coin_frames/bab_coin4.png').convert_alpha()
        self.bab_coin_frames = [self.bab_coin_1, self.bab_coin_2, self.bab_coin_3, self.bab_coin_4]
        self.bab_coin_index = 0
        self.image = self.bab_coin_frames[self.bab_coin_index]
        self.rect = self.image.get_rect(topleft=self.bab_coin_pos[0])
        self.sound = pygame.mixer.Sound('audio/bab_coin_sound.wav')
        self.sound.set_volume(1)

    def animate_bab_coins(self):
        self.bab_coin_index += 0.1
        if self.bab_coin_index >= len(self.bab_coin_frames):
            self.bab_coin_index = 0
        self.image = self.bab_coin_frames[int(self.bab_coin_index)]

    def update(self):
        self.animate_bab_coins()


class Coins(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.coin_pos = []
        self.coin_pos.append(pos)
        self.coin_1 = pygame.image.load('graphics/coins/coin_frames/animated_coin1.png').convert_alpha()
        self.coin_2 = pygame.image.load('graphics/coins/coin_frames/animated_coin2.png').convert_alpha()
        self.coin_3 = pygame.image.load('graphics/coins/coin_frames/animated_coin3.png').convert_alpha()
        self.coin_4 = pygame.image.load('graphics/coins/coin_frames/animated_coin4.png').convert_alpha()
        self.coin_5 = pygame.image.load('graphics/coins/coin_frames/animated_coin5.png').convert_alpha()
        self.coin_6 = pygame.image.load('graphics/coins/coin_frames/animated_coin6.png').convert_alpha()
        self.coin_7 = pygame.image.load('graphics/coins/coin_frames/animated_coin7.png').convert_alpha()
        self.coin_8 = pygame.image.load('graphics/coins/coin_frames/animated_coin8.png').convert_alpha()
        self.coin_frames = [self.coin_1, self.coin_2, self.coin_3, self.coin_4,
                            self.coin_5, self.coin_6, self.coin_7, self.coin_8]
        self.coin_index = 0
        self.image = self.coin_frames[self.coin_index]
        self.rect = self.image.get_rect(topleft=self.coin_pos[0])
        self.sound = pygame.mixer.Sound('audio/coin_sound.wav')
        self.sound.set_volume(0.1)

    def animate_coins(self):
        self.coin_index += 0.13
        if self.coin_index >= len(self.coin_frames):
            self.coin_index = 0
        self.image = self.coin_frames[int(self.coin_index)]

    def update(self):
        self.animate_coins()


class HeartItem(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self_heart_frame_1 = pygame.image.load('graphics/items/heart_item_shine1.png')
        self_heart_frame_2 = pygame.image.load('graphics/items/heart_item_shine2.png')
        self_heart_frame_3 = pygame.image.load('graphics/items/heart_item_shine3.png')
        self_heart_frame_4 = pygame.image.load('graphics/items/heart_item_shine4.png')
        self_heart_frame_5 = pygame.image.load('graphics/items/heart_item_shine5.png')
        self_heart_frame_6 = pygame.image.load('graphics/items/heart_item_shine6.png')
        self_heart_frame_7 = pygame.image.load('graphics/items/heart_item_shine7.png')
        self_heart_frame_8 = pygame.image.load('graphics/items/heart_item_shine8.png')
        self.heart_frames = [self_heart_frame_1, self_heart_frame_2, self_heart_frame_3, self_heart_frame_4,
                             self_heart_frame_5, self_heart_frame_6, self_heart_frame_7, self_heart_frame_8]
        self.heart_frames_index = 0

        self.heart_sound = pygame.mixer.Sound('audio/heart_get.wav')
        self.heart_sound.set_volume(0.3)

        self.image = self.heart_frames[self.heart_frames_index]
        self.rect = self.image.get_rect(topleft=pos)

    def animate_heart(self):
        self.heart_frames_index += 0.2
        if self.heart_frames_index >= len(self.heart_frames):
            self.heart_frames_index = 0
        self.image = self.heart_frames[int(self.heart_frames_index)]

    def update(self):
        self.animate_heart()


class EndStar(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.positions = pos
        self.get_pos = self.get_player_start_pos()
        self.start_pos = self.get_pos[1]
        self.goal_pos = self.get_pos[0]
        self.direction = 'up'
        self.float_frame = 1
        self.float_timer = float(0)

        self.star_1 = pygame.image.load('graphics/goal/end_star_animation1.png').convert_alpha()
        self.star_2 = pygame.image.load('graphics/goal/end_star_animation2.png').convert_alpha()
        self.star_3 = pygame.image.load('graphics/goal/end_star_animation3.png').convert_alpha()
        self.star_4 = pygame.image.load('graphics/goal/end_star_animation4.png').convert_alpha()
        self.star_5 = pygame.image.load('graphics/goal/end_star_animation5.png').convert_alpha()
        self.star_6 = pygame.image.load('graphics/goal/end_star_animation6.png').convert_alpha()
        self.star_7 = pygame.image.load('graphics/goal/end_star_animation7.png').convert_alpha()
        self.star_8 = pygame.image.load('graphics/goal/end_star_animation8.png').convert_alpha()
        self.star_9 = pygame.image.load('graphics/goal/end_star_animation9.png').convert_alpha()
        self.star_10 = pygame.image.load('graphics/goal/end_star_animation10.png').convert_alpha()
        self.star_11 = pygame.image.load('graphics/goal/end_star_animation11.png').convert_alpha()
        self.star_12 = pygame.image.load('graphics/goal/end_star_animation12.png').convert_alpha()
        self.star_frames = [self.star_1, self.star_2, self.star_3, self.star_4, self.star_5, self.star_6,
                            self.star_7, self.star_8, self.star_9, self.star_10, self.star_11, self.star_12]
        self.star_index = 0

        self.image = self.star_frames[self.star_index]
        self.rect = self.image.get_rect(topleft=self.goal_pos)

        self.end_star_sound = pygame.mixer.Sound("audio/end_star_get.wav")

    def get_player_start_pos(self):
        positions = []
        for x, y, _ in self.positions.tiles():
            pos = (x * tile_size, y * tile_size)
            positions.append(pos)
        return list(positions)

    def animate_star(self):
        self.star_index += 0.145
        if self.star_index >= len(self.star_frames):
            self.star_index = 0
        self.image = self.star_frames[int(self.star_index)]

    def float(self):
        if self.direction == 'up':
            self.float_timer += float(0.2)
            self.rect.y -= self.float_frame
            if self.float_timer >= 10:
                self.direction = 'down'

        if self.direction == 'down':
            self.float_timer -= float(0.2)
            self.rect.y += self.float_frame
            if self.float_timer <= 0:
                self.direction = 'up'

    def load_next_pos(self):
        self.rect.x, self.rect.y = self.goal_pos[:2]

    def update(self):
        self.float()
        self.animate_star()









