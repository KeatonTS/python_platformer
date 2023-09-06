import pygame.sprite
from settings import *
from tile import Background


class Camera(pygame.sprite.Group):
    def __init__(self, bg):
        super().__init__()
        self.background = bg
        self.camera_movement = 0
        self.offset = pygame.math.Vector2(self.camera_movement, 0)
        self.display_surface = pygame.display.get_surface()
        self.camera_borders = {'left': 150,
                               'right': 500,
                               'top': 100,
                               'bottom': 100
                               }
        left = self.camera_borders['left']
        top = self.camera_borders['top']
        width = self.display_surface.get_size()[0] - (self.camera_borders['left'] + self.camera_borders['right'])
        height = self.display_surface.get_size()[1] - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(left, top, width, height)

    def box_target_camera(self, target):
        keys = pygame.key.get_pressed()
        for player in target.sprites():
            if player.rect.right >= self.camera_rect.right <= 3325:
                self.camera_rect.right = player.rect.right
                if keys[pygame.K_RIGHT]:
                    self.background.rect.x -= 2

            if player.rect.left <= self.camera_rect.left >= 175:
                self.camera_rect.left = player.rect.left
                if keys[pygame.K_LEFT]:
                    self.background.rect.x += 2

            if player.rect.y >= 1700:
                self.camera_rect.left = 150
            if self.camera_rect.left <= -15:
                self.camera_rect.left = -25

        self.offset.x = self.camera_rect.left - self.camera_borders['left']

    def custom_draw(self, player):
        # Offsets the camera when moving far left or right
        self.box_target_camera(player)
        # affects all active sprites within a group
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.right - sprite.rect.left):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
