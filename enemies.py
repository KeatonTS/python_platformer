import pygame.sprite
from settings import *


class GroundEnemies(pygame.sprite.Sprite):
    def __init__(self, pos, group, level):
        super().__init__(group)
        # loading collision walls to prevent enemies from falling off-screen
        self.constraints = level
        self.constraint_list = []
        self.is_reversed = False
        # Loading all enemy positions on specified map to start from, and separating each enemy in a list
        self.enemy_pos = []
        self.enemy_pos.append(pos)
        self.enemy_group = group
        # Gathering enemy images for animation and enemy attributes
        self.SPEED = 1
        self.enemy_walk_1 = pygame.image.load('graphics/enemy/animated_enemy/enemy_animated1.png')
        self.enemy_walk_2 = pygame.image.load('graphics/enemy/animated_enemy/enemy_animated2.png')
        self.enemy_walk_3 = pygame.image.load('graphics/enemy/animated_enemy/enemy_animated3.png')
        self.enemy_walk_4 = pygame.image.load('graphics/enemy/animated_enemy/enemy_animated4.png')
        self.enemy_walk_frames = [self.enemy_walk_1, self.enemy_walk_2, self.enemy_walk_3, self.enemy_walk_4]
        self.enemy_walk_index = 0
        self.image = self.enemy_walk_frames[self.enemy_walk_index]
        self.rect = self.image.get_rect(topleft=self.enemy_pos[0])
        self.get_constraints()

    def get_constraints(self):
        for x, y, surf in self.constraints.tiles():
            pos = (x * tile_size, y * tile_size)
            self.constraint_list.append(surf.get_rect(topleft=pos))

    def animate_enemies(self):
        self.enemy_walk_index += 0.1
        if self.enemy_walk_index >= len(self.enemy_walk_frames):
            self.enemy_walk_index = 0
        self.image = self.enemy_walk_frames[int(self.enemy_walk_index)]

    def reverse_enemy(self):
        if not self.is_reversed:
            self.is_reversed = True
            for num in range(1, len(self.enemy_walk_frames) + 1):
                self.enemy_walk_frames[num - 1] = pygame.transform.flip(pygame.image.load(f'graphics/enemy/animated_enemy/enemy_animated{num}.png').convert_alpha(), True, False)
        else:
            self.is_reversed = False
            for num in range(1, len(self.enemy_walk_frames) + 1):
                self.enemy_walk_frames[num - 1] = pygame.transform.flip(pygame.image.load(f'graphics/enemy/animated_enemy/enemy_animated{num}.png').convert_alpha(), False, False)

    def update(self):
        self.animate_enemies()
        for wall in self.constraint_list:
            if self.rect.colliderect(wall):
                self.reverse_enemy()
        if self.is_reversed:
            self.rect.x += self.SPEED
        else:
            self.rect.x -= self.SPEED


class FlyingEnemies(pygame.sprite.Sprite):
    def __init__(self, pos, group, level, player):
        super().__init__(group)
        self.player_location = player

        # Grabbing Enemy Positions
        self.enemy_pos = []
        self.enemy_pos.append(pos)
        self.constraints = level
        self.constraint_list = []

        # Collecting Enemy Images
        self.fly_frog_1 = pygame.image.load('graphics/enemy_2/enemy1.png')
        self.fly_frog_2 = pygame.image.load('graphics/enemy_2/enemy2.png')
        self.fly_frog_3 = pygame.image.load('graphics/enemy_2/enemy3.png')
        self.fly_frog_4 = pygame.image.load('graphics/enemy_2/enemy4.png')
        self.fly_frog_frames = [self.fly_frog_1, self.fly_frog_2, self.fly_frog_3, self.fly_frog_4]
        self.fly_frog_index = 0
        self.direction = 'down'
        self.speed = 2
        self.is_reversed = False

        self.image = self.fly_frog_frames[self.fly_frog_index]
        self.rect = self.image.get_rect(topleft=self.enemy_pos[0])
        self.get_constraints()

    def get_constraints(self):
        for x, y, surf in self.constraints.tiles():
            pos = (x * tile_size, y * tile_size)
            self.constraint_list.append(surf.get_rect(topleft=pos))

    def animate_fly_frog(self):
        self.fly_frog_index += 0.175
        if self.fly_frog_index >= len(self.fly_frog_frames):
            self.fly_frog_index = 0
        self.image = self.fly_frog_frames[int(self.fly_frog_index)]

    def reverse_enemy(self):
        if not self.is_reversed:
            self.is_reversed = True
            for num in range(1, len(self.fly_frog_frames) + 1):
                self.fly_frog_frames[num - 1] = pygame.transform.flip(
                    pygame.image.load(f'graphics/enemy_2/enemy{num}.png').convert_alpha(), True,
                    False)
        else:
            self.is_reversed = False
            for num in range(1, len(self.fly_frog_frames) + 1):
                self.fly_frog_frames[num - 1] = pygame.transform.flip(
                    pygame.image.load(f'graphics/enemy_2/enemy{num}.png').convert_alpha(), False,
                    False)

    def enemy_movement(self):
        for wall in self.constraint_list:
            if self.rect.colliderect(wall):
                if self.direction == 'down':
                    self.direction = 'up'
                elif self.direction == 'up':
                    self.direction = 'down'
        if self.direction == 'up':
            self.rect.centery -= self.speed
        if self.direction == 'down':
            self.rect.centery += self.speed

    def enemy_behavior(self):
        for player in self.player_location:
            if player.rect.x > self.rect.x:
                self.is_reversed = False
                self.reverse_enemy()
            elif player.rect.x < self.rect.x:
                self.is_reversed = True
                self.reverse_enemy()

    def update(self):
        self.animate_fly_frog()
        self.enemy_behavior()
        self.enemy_movement()


class EnemyWalls(pygame.sprite.Sprite):
    def __init__(self, pos, groups, zones):
        super().__init__()
        self.image = zones
        self.rect = self.image.get_rect(topright=pos)






