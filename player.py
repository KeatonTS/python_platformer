import pygame
from random import randint
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, self_group, tiles, enemy_1, enemy_2, coins, item, bg):
        super().__init__(group)
        self.item = item
        self.background = bg
        # Collectables items
        self.bab_coin_group = coins
        self.collected_bab_coin = False

        self.ground = tiles
        self.player = self_group

        # Separating Start and Goal Positions
        self.positions = pos
        self.get_pos = self.get_player_start_pos()
        self.start_pos = self.get_pos[1]
        self.goal_pos = self.get_pos[0]

        # Establishing Enemy presence for the player
        self.ground_enemies = enemy_1
        self.air_enemies = enemy_2

        # Idle Animation
        self.player_idle_1 = pygame.image.load('graphics/player/idle_animation1.png').convert_alpha()
        self.player_idle_2 = pygame.image.load('graphics/player/idle_animation2.png').convert_alpha()
        self.player_idle_3 = pygame.image.load('graphics/player/idle_animation3.png').convert_alpha()
        self.player_idle_4 = pygame.image.load('graphics/player/idle_animation4.png').convert_alpha()
        self.player_idle_5 = pygame.image.load('graphics/player/idle_animation5.png').convert_alpha()
        self.idle_frames = [self.player_idle_1, self.player_idle_2,
                            self.player_idle_3, self.player_idle_4, self.player_idle_5]
        self.idle_index = 0

        # Run animation
        self.player_run_1 = pygame.image.load('graphics/player/run_animation1.png').convert_alpha()
        self.player_run_2 = pygame.image.load('graphics/player/run_animation2.png').convert_alpha()
        self.player_run_3 = pygame.image.load('graphics/player/run_animation3.png').convert_alpha()
        self.player_run_4 = pygame.image.load('graphics/player/run_animation4.png').convert_alpha()
        self.player_run_5 = pygame.image.load('graphics/player/run_animation5.png').convert_alpha()
        self.player_run_6 = pygame.image.load('graphics/player/run_animation6.png').convert_alpha()
        self.run_frames = [self.player_run_1, self.player_run_2, self.player_run_3, self.player_run_4,
                           self.player_run_5, self.player_run_6]
        self.run_index = 0

        # Jump Animation
        self.player_jump_0 = pygame.image.load('graphics/player/jump_animation1.png').convert_alpha()
        self.player_jump_1 = pygame.image.load('graphics/player/jump_animation1.png').convert_alpha()
        self.player_jump_2 = pygame.image.load('graphics/player/jump_animation2.png').convert_alpha()
        self.player_jump_3 = pygame.image.load('graphics/player/jump_animation3.png').convert_alpha()
        self.player_jump_4 = pygame.image.load('graphics/player/jump_animation3.png').convert_alpha()
        self.jump_frames = [self.player_jump_0, self.player_jump_1, self.player_jump_2,
                            self.player_jump_3, self.player_jump_4]
        self.jump_index = 0

        # Flip animation
        self.flip_1 = pygame.image.load('graphics/player/flip_animation1.png')
        self.flip_2 = pygame.image.load('graphics/player/flip_animation2.png')
        self.flip_3 = pygame.image.load('graphics/player/flip_animation3.png')
        self.flip_4 = pygame.image.load('graphics/player/flip_animation4.png')
        self.flip_frames = [self.flip_1, self.flip_2, self.flip_3, self.flip_4]
        self.flip_index = 0

        # Damage_Frames
        # self.idle_damage_1 = pygame.image.load('graphics/player/idle_damage_frame1.png')
        # self.idle_damage_2 = pygame.image.load('graphics/player/idle_damage_frame2.png')
        #
        # self.run_damage_frame_1 = pygame.image.load('graphics/player/run_damage_1.png')
        # self.run_damage_frame_2 = pygame.image.load('graphics/player/run_damage_2.png')

        # Player Attributes and Stats

        # Health
        self.MAX_LIVES = 10
        self.TOTAL_LIVES = 2
        self.current_lives = self.TOTAL_LIVES
        self.TOTAL_HEARTS = 3
        self.hearts = 3
        self.INVINCIBILITY_FRAMES = float(0)
        self.respawn_timer = 0

        # Abilities
        self.SPEED = 5
        self.TOTAL_JUMPS = 2
        self.JUMP_HEIGHT = -18
        self.DOUBLE_JUMP_HEIGHT = -14
        self.GRAVITY = 0
        self.VELOCITY = 0
        self.KNOCK_BACK = 0
        self.KNOCK_BACK_DISTANCE = 15
        self.KNOCK_BACK_HEIGHT = -10
        self.enemy_stomp_height = -14

        # Coins
        self.TOTAL_BAB_COINS = 3
        self.total_coins = 0

        # Character behaviors
        self.wall_cling = pygame.image.load('graphics/player/wall_cling.png').convert_alpha()
        self.player_hit = pygame.image.load('graphics/player/player_hit.png').convert_alpha()
        self.player_victory = pygame.image.load('graphics/player/player_victory1.png').convert_alpha()
        self.on_left_wall = False
        self.on_right_wall = False
        self.on_wall = False
        self.double_jumped = False
        self.on_ground = False
        self.is_reversed = False
        self.has_jump = False
        self.is_moving = False
        self.in_air = False
        self.near_wall = False
        self.is_hit = False
        self.fell = False
        self.item_dropped = False
        self.enemy_location = ''
        self.item_location = ''
        self.collected_heart = False
        self.defeated_enemy = False

        # Player appearance
        self.image = self.idle_frames[self.idle_index]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect(topleft=self.start_pos)
        self.space_was_pressed = False
        # self.alt_player = pygame.rect.Rect(self.rect.x + 27, self.rect.y + 10, self.width - 50, self.height - 25, )

        # ---- UI elements Below ----

        # Collecting Assets
        self.player_panel = pygame.image.load('graphics/UI/player_panel.png').convert_alpha()
        self.full_heart = pygame.image.load('graphics/UI/full_heart.png').convert_alpha()
        self.empty_heart = pygame.image.load('graphics/UI/empty_heart.png').convert_alpha()
        self.item_box = pygame.image.load('graphics/UI/empty_item_box.png').convert_alpha()
        self.full_coin_slot = pygame.image.load('graphics/UI/full_bab_coin_slot.png').convert_alpha()
        self.empty_bab_coin_slot = pygame.image.load('graphics/UI/empty_bab_coin_slot.png').convert_alpha()
        self.icon = pygame.image.load('graphics/UI/player_icon.png').convert_alpha()
        self.coin_icon = pygame.image.load('graphics/UI/coin_icon.png').convert_alpha()

        # UI Base
        self.panel_rect = self.player_panel.get_rect(topleft=(0, 15))
        self.ui_distance = 279
        self.off_screen_panel = 0
        self.ui_in_way = False

        # Creating heart Slots
        self.heart_rect_list = []
        self.heart_list = []
        heart_spacing = 0
        for heart in range(self.TOTAL_HEARTS):
            self.heart_rect_list.append(self.full_heart.get_rect(topleft=(85, 23)))
            self.heart_rect_list[heart].x += heart_spacing
            heart_spacing += 35
            self.heart_list.append(self.full_heart)

        # Creating Bab_Coin Slots
        self.b_coin_list = []
        self.b_coin_rect_list = []
        b_coin_spacing = 0
        for b_coin in range(self.TOTAL_BAB_COINS):
            self.b_coin_rect_list.append(self.empty_bab_coin_slot.get_rect(topleft=(95, 53)))
            self.b_coin_rect_list[b_coin].x += b_coin_spacing
            b_coin_spacing += 25

        # Creating item box
        self.item_box_rect = self.item_box.get_rect(topleft=(190, 20))

        # Creating Icons and fonts
        self.player_icon_rect = self.icon.get_rect(topleft=(10, 20))
        self.coin_rect = self.coin_icon.get_rect(topleft=(19, 60))

        # sounds
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.stomp_sound = pygame.mixer.Sound('audio/enemy_stomp.wav')
        self.double_jump_sound = pygame.mixer.Sound('audio/double_jump.wav')
        self.land_sound = pygame.mixer.Sound('audio/land.wav')
        self.hit_sound = pygame.mixer.Sound('audio/hit.wav')
        self.walk_sound = pygame.mixer.Sound('audio/walk.mp3')
        self.fall_sound = pygame.mixer.Sound('audio/fall.wav')
        self.extra_life_sound = pygame.mixer.Sound('audio/1-up.wav')
        self.jump_sound.set_volume(0.3)
        self.extra_life_sound.set_volume(0.4)
        self.stomp_sound.set_volume(1)
        self.fall_sound.set_volume(0.4)

    def build_interface(self, display):
        # Display UI panel
        display.blit(self.player_panel, self.panel_rect)

        # Move UI if player is close to it
        if self.rect.colliderect(self.panel_rect) or self.rect.y <= self.panel_rect.bottom + 5:
            self.ui_in_way = True
        else:
            self.ui_in_way = False

        # Display UI Elements
        for num in range(self.TOTAL_HEARTS):
            display.blit(self.heart_list[num], self.heart_rect_list[num])

        for b_coin in self.b_coin_rect_list:
            display.blit(self.empty_bab_coin_slot, b_coin)

        display.blit(self.item_box, self.item_box_rect)
        display.blit(self.icon, self.player_icon_rect)
        display.blit(self.coin_icon, self.coin_rect)

    def took_damage(self):
        if self.INVINCIBILITY_FRAMES <= 0:
            self.heart_list[self.hearts - 1] = self.empty_heart
            self.hearts -= 1
            self.INVINCIBILITY_FRAMES = float(10)

    def invincibility_frames(self):
        self.INVINCIBILITY_FRAMES -= float(0.2)
        if self.INVINCIBILITY_FRAMES <= 0:
            self.INVINCIBILITY_FRAMES = 0

    def collect_bab_coins(self, screen):
        for coin in self.bab_coin_group:
            if self.rect.collidepoint(coin.rect.center):
                self.collected_bab_coin = True
            if self.collected_bab_coin:
                self.b_coin_list.append(self.full_coin_slot)
            self.collected_bab_coin = False
        if len(self.b_coin_list) >= 1:
            for coin in range(len(self.b_coin_list)):
                screen.blit(self.full_coin_slot, self.b_coin_rect_list[coin])

    def retract_ui(self):
        if self.panel_rect.right >= self.off_screen_panel and self.ui_in_way:
            self.panel_rect.right -= 30

    def return_ui(self):
        # print(self.panel_rect.right)
        if self.panel_rect.right <= self.ui_distance and not self.ui_in_way:
            self.panel_rect.right += 30
            if self.panel_rect.right >= self.ui_distance:
                self.panel_rect.right = self.ui_distance

    def get_jump_input(self):
        if self.TOTAL_JUMPS < 0:
            self.TOTAL_JUMPS = 0
        keys = pygame.key.get_pressed()
        space_is_pressed = keys[pygame.K_SPACE]
        if space_is_pressed and not self.space_was_pressed and self.TOTAL_JUMPS == 2:
            self.jump()
        elif space_is_pressed and not self.space_was_pressed and self.TOTAL_JUMPS == 1 and self.in_air:
            self.TOTAL_JUMPS -= 1
            self.double_jump()
            self.double_jumped = True
        self.space_was_pressed = space_is_pressed

    def jump(self):
        if not self.in_air:
            self.jump_sound.play()
            self.GRAVITY = self.JUMP_HEIGHT
            self.TOTAL_JUMPS -= 1

        else:
            self.TOTAL_JUMPS = 0
            self.double_jumped = True
            self.double_jump()

    def double_jump(self):
        self.jump_sound.play()
        self.GRAVITY = self.DOUBLE_JUMP_HEIGHT

    def get_player_start_pos(self):
        positions = []
        for x, y, _ in self.positions.tiles():
            pos = (x * tile_size, y * tile_size)
            positions.append(pos)
        return list(positions)

    def player_jump_animation(self):
        self.jump_index += 0.085
        if self.jump_index >= 4:
            self.jump_index = 4
            if not self.is_reversed:
                self.jump_frames[int(self.jump_index)] = pygame.transform.flip(self.player_jump_3, False, False)
            else:
                self.jump_frames[int(self.jump_index)] = pygame.transform.flip(self.player_jump_3, False, False)

        self.image = self.jump_frames[int(self.jump_index)]

    def player_flip_animation(self):
        self.flip_index += 0.300
        if self.flip_index >= len(self.flip_frames):
            self.flip_index = 0
        self.image = self.flip_frames[int(self.flip_index)]

    def player_idle_animation(self):
        self.idle_index += 0.143
        if self.idle_index >= len(self.idle_frames):
            self.idle_index = 0
        self.image = self.idle_frames[int(self.idle_index)]

    def player_run_animation(self):
        self.run_index += 0.175
        if self.run_index >= len(self.run_frames):
            self.run_index = 0
        self.image = self.run_frames[int(self.run_index)]

    def cling_to_wall(self, direction):
        if direction == 'left':
            self.image = pygame.transform.flip(pygame.image.load(
                'graphics/player/wall_cling.png').convert_alpha(), True, False)
        elif direction == 'right':
            self.image = self.image = pygame.transform.flip(pygame.image.load(
                'graphics/player/wall_cling.png').convert_alpha(), False, False)

        self.GRAVITY -= 0.8
        self.GRAVITY -= self.GRAVITY - 4
        self.TOTAL_JUMPS = 1

    def reverse(self):
        self.is_reversed = True
        for num in range(1, len(self.idle_frames) + 1):
            self.idle_frames[num - 1] = pygame.transform.flip(
                pygame.image.load(f'graphics/player/idle_animation{num}.png').convert_alpha(), True, False)

        for num in range(1, len(self.run_frames) + 1):
            self.run_frames[num - 1] = pygame.transform.flip(
                pygame.image.load(f'graphics/player/run_animation{num}.png').convert_alpha(), True, False)

        for num in range(1,  4):
            self.jump_frames[num - 1] = pygame.transform.flip(
                pygame.image.load(f'graphics/player/jump_animation{num}.png').convert_alpha(), True, False)
        self.jump_frames[0] = pygame.transform.flip(
            pygame.image.load('graphics/player/jump_animation1.png').convert_alpha(), True, False)
        self.jump_frames[4] = pygame.transform.flip(
            pygame.image.load('graphics/player/jump_animation3.png').convert_alpha(), True, False)

        for num in range(1, 5):
            self.flip_frames[num - 1] = pygame.transform.flip(
                pygame.image.load(f'graphics/player/flip_animation{num}.png').convert_alpha(), True, False)

    def undo_reverse(self):
        for num in range(1, len(self.idle_frames) + 1):
            self.idle_frames[num - 1] = pygame.transform.flip(pygame.image.load(
                f'graphics/player/idle_animation{num}.png').convert_alpha(), False, False)

        for num in range(1, len(self.run_frames) + 1):
            self.run_frames[num - 1] = pygame.transform.flip(
                pygame.image.load(f'graphics/player/run_animation{num}.png').convert_alpha(), False, False)

        for num in range(1, 4):
            self.jump_frames[num - 1] = pygame.transform.flip(
                pygame.image.load(f'graphics/player/jump_animation{num}.png').convert_alpha(), False, False)
        self.jump_frames[0] = pygame.transform.flip(
            pygame.image.load('graphics/player/jump_animation1.png').convert_alpha(), False, False)
        self.jump_frames[4] = pygame.transform.flip(
            pygame.image.load('graphics/player/jump_animation3.png').convert_alpha(), False, False)

        for num in range(1, 5):
            self.flip_frames[num - 1] = pygame.transform.flip(
                pygame.image.load(f'graphics/player/flip_animation{num}.png').convert_alpha(), False, False)

    def apply_knock_back(self):
        self.KNOCK_BACK += 1
        if self.KNOCK_BACK >= 20 or self.KNOCK_BACK <= -20:
            self.KNOCK_BACK = 0
        self.rect.x += self.KNOCK_BACK

    def apply_gravity(self):
        keys = pygame.key.get_pressed()
        self.GRAVITY += 1
        if self.GRAVITY >= 100:
            self.GRAVITY = 0
        self.rect.y += self.GRAVITY

        # Checking if player is free-falling in the air, not colliding with anything
        if not pygame.sprite.spritecollideany(self.player.sprite, self.ground):
            self.in_air = True
            self.on_wall = False
            self.on_ground = False
            self.has_jump = False
            self.DOUBLE_JUMP_HEIGHT = -15
            if not self.is_reversed:
                self.image = pygame.transform.flip(self.player_jump_3, False, False)
            else:
                self.image = pygame.transform.flip(self.player_jump_3, True, False)

        for ground in self.ground:
            if ground.rect.colliderect(pygame.rect.Rect(self.rect.x, self.rect.y, self.width, self.height)):
                # Checks if the player is on the ground
                if pygame.rect.Rect(self.rect.x, self.rect.y, self.width, self.height).colliderect(ground.rect) and self.rect.collidepoint(ground.rect.midtop):
                    self.rect.bottom = ground.rect.top
                    self.on_right_wall = False
                    self.on_left_wall = False
                    self.on_wall = False
                    self.on_ground = True
                    self.in_air = False
                    self.near_wall = False
                    self.jump_index = 0
                    self.has_jump = True
                    self.double_jumped = False
                    self.TOTAL_JUMPS = 2
                    self.GRAVITY = 0

                elif self.rect.top >= ground.rect.top and self.rect.collidepoint(ground.rect.midbottom):
                    self.rect.top = ground.rect.bottom
                    self.GRAVITY += 10

            if ground.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                if self.rect.left < ground.rect.right and self.rect.collidepoint(ground.rect.midright):
                    # Wall clinging and Jumping
                    if ground.rect.collidepoint(self.rect.midleft):
                        # self.rect.left = ground.rect.right
                        self.near_wall = True
                        if keys[pygame.K_LEFT] and ground.rect.collidepoint(self.rect.midleft):
                            self.rect.left = ground.rect.right
                            self.on_wall = True
                            self.on_left_wall = True

                    else:
                        self.near_wall = False
                        self.on_right_wall = False
                        self.DOUBLE_JUMP_HEIGHT = -15

                if self.rect.right > ground.rect.left and self.rect.collidepoint(ground.rect.midleft):
                    # Wall clinging and Jumping
                    if ground.rect.collidepoint(self.rect.midright):
                        self.rect.right = ground.rect.left
                        self.near_wall = True
                        if keys[pygame.K_RIGHT] and ground.rect.collidepoint(self.rect.midright):
                            self.rect.right = ground.rect.left
                            self.on_wall = True
                            self.on_right_wall = True

                    else:
                        self.near_wall = False
                        self.on_left_wall = False
                        self.DOUBLE_JUMP_HEIGHT = -15

    def player_input(self):
        keys = pygame.key.get_pressed()
        self.get_jump_input()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.SPEED
            self.is_moving = True
            if self.is_reversed:
                self.undo_reverse()
                self.is_reversed = False

        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.SPEED
            self.is_moving = True
            if not self.is_reversed:
                self.reverse()
                self.is_reversed = True

        else:
            self.is_moving = False

    def fell_off(self):
        if self.rect.bottom > 1000:
            self.fell = True
            self.respawn()

    def respawn(self):
        self.background.rect.left = 0
        self.rect.x, self.rect.y = self.start_pos[:2]
        self.rect.x = 200

    def camera_focus(self):
        #focusing camera on player so that it doesn't reveal blank surface
        if self.rect.x <= self.start_pos[0]:
            self.background.rect.left = 0
        if self.rect.x >= self.background.rect.right:
            self.background.rect.right = self.background.rect.right

    def animation_state(self):
        keys = pygame.key.get_pressed()
        # Run animation
        if self.is_moving and self.has_jump and not self.in_air:
            self.player_run_animation()

        elif self.on_wall:
            if self.on_right_wall and keys[pygame.K_RIGHT]:
                self.cling_to_wall('left')
            elif self.on_left_wall and keys[pygame.K_LEFT]:
                self.cling_to_wall('right')

        # Double Jump animation
        elif self.TOTAL_JUMPS == 0 and self.in_air and self.double_jumped and not self.is_hit:
            self.player_flip_animation()

        # Regular Jump animation
        elif self.TOTAL_JUMPS == 1 and not self.has_jump:
            self.player_jump_animation()

        # Player damage animation
        elif self.in_air and self.is_hit or self.ground and self.is_hit:
            if not self.is_reversed:
                self.image = pygame.transform.flip(self.player_hit, False, False)
            else:
                self.image = pygame.transform.flip(self.player_hit, True, False)

        # Free fall animation
        elif self.in_air and not self.double_jumped and not self.on_ground:
            if not self.is_reversed:
                self.image = pygame.transform.flip(self.player_jump_3, False, False)
            else:
                self.image = pygame.transform.flip(self.player_jump_3, True, False)

        else:
            self.player_idle_animation()

    def enemy_collision(self):
        enemy_drop = randint(5, 9)
        self.item_dropped = False
        keys = pygame.key.get_pressed()
        alt_player_rect = pygame.rect.Rect(self.rect.x + 27, self.rect.y + 10, self.width - 50, self.height - 25)

        for enemy in self.ground_enemies:
            if enemy.rect.colliderect(alt_player_rect):
                if alt_player_rect.bottom >= enemy.rect.top and self.in_air and not self.is_hit and keys[pygame.K_SPACE]:
                    self.defeated_enemy = True
                    self.enemy_location = (enemy.rect.centerx - 20, enemy.rect.centery - 20)
                    self.GRAVITY = self.enemy_stomp_height
                    self.stomp_sound.play()
                    enemy.kill()
                    if enemy_drop == 7:
                        self.item_location = enemy.rect.center
                        self.item_dropped = True

                if alt_player_rect.bottom >= enemy.rect.centery and self.in_air \
                        and self.INVINCIBILITY_FRAMES == 0:
                    self.is_hit = True
                    self.GRAVITY = self.KNOCK_BACK_HEIGHT
                    self.KNOCK_BACK = -self.KNOCK_BACK_DISTANCE
                    self.hit_sound.play()
                    self.took_damage()

                if self.on_ground and alt_player_rect.collidepoint(enemy.rect.midleft) \
                        and self.INVINCIBILITY_FRAMES == 0:
                    self.is_hit = True
                    self.GRAVITY = self.KNOCK_BACK_HEIGHT
                    self.KNOCK_BACK = -self.KNOCK_BACK_DISTANCE
                    self.hit_sound.play()
                    self.took_damage()

                if self.on_ground and alt_player_rect.collidepoint(enemy.rect.midright) \
                        and self.INVINCIBILITY_FRAMES == 0:
                    self.is_hit = True
                    self.GRAVITY = self.KNOCK_BACK_HEIGHT
                    self.KNOCK_BACK = self.KNOCK_BACK_DISTANCE
                    self.hit_sound.play()
                    self.took_damage()

        if self.hearts <= 0:
            self.hearts = 0

        for enemy in self.air_enemies:
            if enemy.rect.colliderect(alt_player_rect):
                if alt_player_rect.bottom >= enemy.rect.top and self.in_air and not self.is_hit and keys[pygame.K_SPACE]:
                    self.GRAVITY = self.enemy_stomp_height
                    self.stomp_sound.play()
                    self.defeated_enemy = True
                    self.enemy_location = (enemy.rect.centerx - 20, enemy.rect.centery - 20)
                    enemy.kill()
                    self.has_jump = True
                    self.TOTAL_JUMPS = 1
                    self.GRAVITY = -25

                if alt_player_rect.bottom >= enemy.rect.centery + 10 and self.in_air and self.INVINCIBILITY_FRAMES == 0:
                    self.is_hit = True
                    self.GRAVITY = self.KNOCK_BACK_HEIGHT
                    self.KNOCK_BACK = -self.KNOCK_BACK_DISTANCE
                    self.hit_sound.play()
                    self.took_damage()

                if self.in_air and alt_player_rect.collidepoint(enemy.rect.midleft):
                    self.is_hit = True
                    self.GRAVITY = self.KNOCK_BACK_HEIGHT
                    self.KNOCK_BACK = -self.KNOCK_BACK_DISTANCE
                    self.hit_sound.play()
                    self.took_damage()

                if self.in_air and alt_player_rect.collidepoint(enemy.rect.midright) and self.INVINCIBILITY_FRAMES == 0:
                    self.is_hit = True
                    self.GRAVITY = self.KNOCK_BACK_HEIGHT
                    self.KNOCK_BACK = self.KNOCK_BACK_DISTANCE
                    self.hit_sound.play()
                    self.took_damage()

        if self.is_hit:
            self.apply_knock_back()
            if self.KNOCK_BACK == 0:
                self.is_hit = False

    def player_constraints(self):
        if self.rect.x <= -20:
            self.rect.x = -20
        if self.rect.x >= 3770:
            self.rect.x = 3770

    def update(self, screen):
        self.camera_focus()
        self.apply_gravity()
        self.animation_state()
        self.fell_off()
        self.player_input()
        self.enemy_collision()
        self.player_constraints()
        self.build_interface(screen)
        self.collect_bab_coins(screen)
        self.retract_ui()
        self.return_ui()
        self.invincibility_frames()







# Code that may be discarded but unsure

    # def apply_velocity(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_SPACE] and self.on_wall:
    #         if self.is_reversed:
    #             self.VELOCITY -= 1
    #             print('applied')
    #             if self.VELOCITY <= -100:
    #                 self.VELOCITY = 0
    #         else:
    #             self.VELOCITY += 1
    #             print('applied')
    #             if self.VELOCITY >= 100:
    #                 self.VELOCITY = 0
    #         self.rect.x += self.VELOCITY



