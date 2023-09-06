import pygame.draw
from random import randint


class DefeatParticles(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        self.particle_1 = pygame.image.load('graphics/particles/particle1.png')
        self.particle_2 = pygame.image.load('graphics/particles/particle2.png')
        self.particle_3 = pygame.image.load('graphics/particles/particle3.png')
        self.particle_4 = pygame.image.load('graphics/particles/particle4.png')
        self.particle_5 = pygame.image.load('graphics/particles/particle5.png')
        self.particle_frames = [self.particle_1, self.particle_2, self.particle_3, self.particle_4, self.particle_5]
        self.particle_index = 0
        self.image = self.particle_frames[self.particle_index]
        self.rect = self.image.get_rect(topleft=pos)

    def animate_particle(self):
        self.particle_index += 0.2
        if self.particle_index >= len(self.particle_frames):
            self.particle_index = 0
            self.kill()
        self.image = self.particle_frames[int(self.particle_index)]

    def update(self):
        self.animate_particle()


class CoinParticle(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        self.coin_particle_1 = pygame.image.load('graphics/particles/coin_particle/particle1.png')
        self.coin_particle_2 = pygame.image.load('graphics/particles/coin_particle/particle2.png')
        self.coin_particle_3 = pygame.image.load('graphics/particles/coin_particle/particle3.png')
        self.coin_particle_4 = pygame.image.load('graphics/particles/coin_particle/particle4.png')
        self.coin_particle_5 = pygame.image.load('graphics/particles/coin_particle/particle5.png')
        self.coin_particle_6 = pygame.image.load('graphics/particles/coin_particle/particle6.png')
        self.coin_particle_7 = pygame.image.load('graphics/particles/coin_particle/particle7.png')
        self.coin_particle_8 = pygame.image.load('graphics/particles/coin_particle/particle8.png')
        self.coin_particle_frames = [self.coin_particle_1, self.coin_particle_2, self.coin_particle_3,
                                     self.coin_particle_4, self.coin_particle_5, self.coin_particle_6,
                                     self.coin_particle_7, self.coin_particle_8]
        self.coin_particle_index = 0
        self.image = self.coin_particle_frames[self.coin_particle_index]
        self.rect = self.image.get_rect(topleft=pos)

    def animate_coin_particle(self):
        self.coin_particle_index += 0.2
        if self.coin_particle_index >= len(self.coin_particle_frames):
            self.coin_particle_index = 0
            self.kill()
        self.image = self.coin_particle_frames[int(self.coin_particle_index)]

    def update(self):
        self.animate_coin_particle()


class BabCoinParticle(pygame.sprite.Sprite):
    def __init__(self, group, pos):
        super().__init__(group)
        self.coin_particle_1 = pygame.image.load('graphics/particles/bab_coin_particle/particle1.png')
        self.coin_particle_2 = pygame.image.load('graphics/particles/bab_coin_particle/particle2.png')
        self.coin_particle_3 = pygame.image.load('graphics/particles/bab_coin_particle/particle3.png')
        self.coin_particle_4 = pygame.image.load('graphics/particles/bab_coin_particle/particle4.png')
        self.coin_particle_5 = pygame.image.load('graphics/particles/bab_coin_particle/particle5.png')
        self.coin_particle_6 = pygame.image.load('graphics/particles/bab_coin_particle/particle6.png')
        self.coin_particle_7 = pygame.image.load('graphics/particles/bab_coin_particle/particle7.png')
        self.coin_particle_8 = pygame.image.load('graphics/particles/bab_coin_particle/particle8.png')
        self.coin_particle_9 = pygame.image.load('graphics/particles/bab_coin_particle/particle9.png')
        self.coin_particle_frames = [self.coin_particle_1, self.coin_particle_2, self.coin_particle_3,
                                     self.coin_particle_4, self.coin_particle_5, self.coin_particle_6,
                                     self.coin_particle_7, self.coin_particle_8, self.coin_particle_9]
        self.coin_particle_index = 0
        self.image = self.coin_particle_frames[self.coin_particle_index]
        self.rect = self.image.get_rect(topleft=pos)

    def animate_bab_coin_particle(self):
        self.coin_particle_index += 0.2
        if self.coin_particle_index >= len(self.coin_particle_frames):
            self.coin_particle_index = 0
            self.kill()
        self.image = self.coin_particle_frames[int(self.coin_particle_index)]

    def update(self):
        self.animate_bab_coin_particle()




