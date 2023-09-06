import pygame, sys
from settings import *
from tile import Tile, Grass, Background
from pytmx.util_pygame import load_pygame
from collectable import BabCoins, Coins, EndStar, HeartItem
from enemies import GroundEnemies, FlyingEnemies, EnemyWalls
from player import Player
from camera import Camera
from menu import Menu
from music import Music
from particles import DefeatParticles, CoinParticle, BabCoinParticle
from random import randint


# Game Info
pygame.init()
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_height), vsync=1)
victory_screen = pygame.display.set_mode((screen_width, screen_height), vsync=1)
level_num = 1
game_running = False
game_paused = False
game_over = False
level_clear = False
event_timer = float(0)


tmx_data = load_pygame(f'tilesets/level_{level_num}.tmx')


mouse_rect = pygame.rect.Rect(15, 15, 15, 15)

# music
music = Music()

# Backgrounds
background = Background()
# bg_surface = pygame.image.load('graphics/bg/background.png').convert_alpha()
# dark_bg_surface = pygame.image.load('graphics/bg/dark_background.png').convert_alpha()
# bg_rect = bg_surface.get_rect(topleft=(0, 0))
victory_bg_surface = pygame.image.load('graphics/bg/victory_screen.png').convert_alpha()
tile_surface = pygame.image.load('graphics/tiles/level_1.png').convert_alpha()

# Camera
camera_group = Camera(background)
camera_group.add(Camera(background))

# Game Font, Menu, and UI elements
menu = Menu()
button_1_text_height = 310
button_2_text_height = 455
button_3_text_height = 600

# Map Tiles
ground_group = pygame.sprite.Group()
ground = tmx_data.get_layer_by_name('terrain')
grass = tmx_data.get_layer_by_name('grass')
decor_group = pygame.sprite.Group()
ground_list = []

# Load Coins
bab_coins = tmx_data.get_layer_by_name('bab_coin')
coins = tmx_data.get_layer_by_name('coin')
bab_coin_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()

# Load Enemies and constraints
ground_enemies = tmx_data.get_layer_by_name('enemy')
constraints = tmx_data.get_layer_by_name('constraints')
ground_enemy_group = pygame.sprite.Group()
constraint_group = pygame.sprite.Group()

flying_enemies = tmx_data.get_layer_by_name('enemy_2')
flying_constraints = tmx_data.get_layer_by_name('constraints_2')
flying_group = pygame.sprite.Group()
flying_constraint_group = pygame.sprite.Group()

# Item Groups
item = HeartItem(pos=(0, 0), group=camera_group)
item_group = pygame.sprite.Group()
item_group.add(item)

# Load player
positions = tmx_data.get_layer_by_name('player')
player_group = pygame.sprite.GroupSingle()
player = Player(pos=positions, group=camera_group, tiles=ground_group, self_group=player_group,
                enemy_1=ground_enemy_group, enemy_2=flying_group, coins=bab_coin_group, item=item, bg=background)

player_group.add(player)


# Load Goal
goal_group = pygame.sprite.Group()
end_star = EndStar(pos=positions, group=camera_group)
goal_group.add(end_star)


# loading dummy assets then removing them from group to have access to calling the class. (this is because multiple
# instance are being made due to there being many existing at once. I don't think I learned a way around this yet)
bab_coin = BabCoins(pos=(0, 0), group=camera_group)
reg_coin = Coins(pos=(0, 0), group=camera_group)
ground_enemy = GroundEnemies((0, 0), camera_group, constraints)
flying_enemy = FlyingEnemies((0, 0),  camera_group, flying_constraints, player_group)

ground_enemy.kill()
flying_enemy.kill()
reg_coin.kill()
bab_coin.kill()
item.kill()


def start_game():
    global game_running, game_over, game_paused

    if not game_running and not game_paused or game_running and game_over:
        if not game_running:
            load_level()
            load_decor()
        load_coins()
        load_enemies()

    game_running = True
    game_over = False
    game_paused = False
    music.level_theme.play(loops=-1)


# Refreshes every element group then reloads them in start_game(). Try refactoring this code to be better in the future
def reload_level():
    global level_num

    for enemy in ground_enemy_group:
        GroundEnemies.kill(enemy)
    for enemy in flying_group:
        FlyingEnemies.kill(enemy)
    for coin in bab_coin_group:
        BabCoins.kill(coin)
    for coin in coin_group:
        Coins.kill(coin)
    for heart in item_group:
        HeartItem.kill(heart)

    player.total_coins = 0
    player.b_coin_list = []
    if game_over:
        level_num = 1
        print('true')
    start_game()


def get_tmx_elements():
    global tmx_data, ground, grass, bab_coins, coins,\
        ground_enemies, constraints, flying_enemies, flying_constraints, positions
    tmx_data = load_pygame(f'tilesets/level_{level_num}.tmx')

    bab_coins = tmx_data.get_layer_by_name('bab_coin')
    coins = tmx_data.get_layer_by_name('coin')
    ground_enemies = tmx_data.get_layer_by_name('enemy')
    constraints = tmx_data.get_layer_by_name('constraints')
    flying_enemies = tmx_data.get_layer_by_name('enemy_2')
    flying_constraints = tmx_data.get_layer_by_name('constraints_2')
    ground = tmx_data.get_layer_by_name('terrain')
    positions = tmx_data.get_layer_by_name('player')
    grass = tmx_data.get_layer_by_name('grass')


def load_next_level():
    global level_num, end_star

    get_tmx_elements()
    for enemy in ground_enemy_group:
        GroundEnemies.kill(enemy)
    for enemy in flying_group:
        FlyingEnemies.kill(enemy)
    for coin in bab_coin_group:
        BabCoins.kill(coin)
    for coin in coin_group:
        Coins.kill(coin)
    for ground in ground_group:
        Tile.kill(ground)
    for decor in decor_group:
        Grass.kill(decor)
    for goal in goal_group:
        EndStar.kill(goal)
    load_level()
    load_decor()
    load_coins()
    load_enemies()

    end_star = EndStar(pos=positions, group=camera_group)
    goal_group.add(end_star)
    end_star.load_next_pos()
    music.level_theme.play(loops=-1)


def display_menu(game_state):
    global game_paused, button_1_text_height, button_2_text_height, game_over, level_num
    mouse_rect.x, mouse_rect.y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

    if game_over:
        screen.blit(menu.game_over_bg, (0, 0))

    else:
        screen.blit(menu.bg_surface, (0, 0))

    screen.blit(menu.button_surface_1, menu.button_rect_1)
    screen.blit(menu.button_surface_2, menu.button_rect_2)
    screen.blit(menu.quit_surface, (535, button_2_text_height))

    if game_state == 'paused':
        screen.blit(menu.pause_surface, (440, 100))
        screen.blit(menu.resume_surface, (510, button_1_text_height))

    elif game_state == 'inactive':
        screen.blit(menu.play_surface, (535, button_1_text_height))
        screen.blit(menu.main_menu_surface, (355, 100))

    elif game_state == 'game over':
        screen.blit(menu.restart_surface, (490, button_1_text_height))
        screen.blit(menu.game_over_surface, (355, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if mouse_rect.colliderect(menu.button_rect_1) and menu.button_surface_2 == menu.unpressed_button:
            menu.button_surface_1 = menu.pressed_button
            button_1_text_height = 320
            if event.type == pygame.MOUSEBUTTONDOWN and game_state == 'inactive':
                start_game()

            elif event.type == pygame.MOUSEBUTTONDOWN and game_state == 'paused':
                menu.unpause_sound.play()
                game_paused = False
                music.level_theme.play(loops=-1)

            elif event.type == pygame.MOUSEBUTTONDOWN and game_state == 'game over':
                level_num = 1
                replenish_all_hearts()
                player.b_coin_list = []
                player.total_coins = 0
                player.current_lives = player.TOTAL_LIVES
                player.respawn()
                load_next_level()
                start_game()

        elif mouse_rect.colliderect(menu.button_rect_2) and menu.button_surface_1 == menu.unpressed_button:
            menu.button_surface_2 = menu.pressed_button
            button_2_text_height = 465
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

        else:
            menu.button_surface_1, menu.button_surface_2 = menu.unpressed_button, menu.unpressed_button
            button_1_text_height = 310
            button_2_text_height = 455

    pygame.display.update()


def load_coins():
    for x, y, _ in bab_coins.tiles():
        pos = (x * tile_size, y * tile_size)
        bab_coin_group.add(BabCoins(pos=pos, group=camera_group))
    for x, y, _ in coins.tiles():
        pos = (x * tile_size, y * tile_size)
        coin_group.add(Coins(pos=pos, group=camera_group))


def load_level():

    for layer in tmx_data.visible_layers:
        if hasattr(layer, 'data'):
            for x, y, surface in ground.tiles():
                pos = (x * tile_size, y * tile_size)
                ground_group.add(Tile(pos=pos, surf=surface, group=camera_group))
                ground_list.append(surface.get_rect(topleft=pos))


def collect_coins():
    coins_collected = pygame.sprite.spritecollide(player_group.sprite, coin_group, False)
    for coin in coins_collected:
        if player_group.sprite.rect.collidepoint(coin.rect.center):
            reg_coin.sound.play()
            player.total_coins += 1

            particle_group.add(CoinParticle(group=camera_group, pos=(coin.rect.centerx -20, coin.rect.centery - 20)))
            coin.kill()
    bab_coins_collected = pygame.sprite.spritecollide(player_group.sprite, bab_coin_group, False)
    for coin in bab_coins_collected:
        if player_group.sprite.rect.collidepoint(coin.rect.center):
            particle_group.add()
            bab_coin.sound.play()
            particle_group.add(BabCoinParticle(group=camera_group, pos=(coin.rect.centerx -20, coin.rect.centery - 20)))
            coin.kill()


def load_decor():
    for x, y, surf in grass.tiles():
        pos = (x * tile_size, y * tile_size)
        decor_group.add(Grass(pos=pos, group=camera_group, surf=surf))


def load_enemies():
    """Loads all enemies from Tiled, grabs each position and puts them into their specific group"""
    for x, y, surf in ground_enemies.tiles():
        pos = (x * tile_size, y * tile_size)
        ground_enemy_group.add(GroundEnemies(pos=pos, group=camera_group, level=constraints))

    # Loading walls for enemies to turn around if run into
    for x, y, surf in constraints.tiles():
        pos = (x * tile_size, y * tile_size)
        img = surf
        constraint_group.add(EnemyWalls(pos=pos, groups=constraint_group, zones=surf))

    for x, y, surf in flying_enemies.tiles():
        pos = (x * tile_size, y * tile_size)
        flying_group.add(FlyingEnemies(pos=pos, group=camera_group, level=flying_constraints, player=player_group))


def event_pause():
    global event_timer
    event_timer -= float(0.1)
    if event_timer <= 0:
        event_timer = float(0)


def player_status():
    """Checks conditions of the player based on numerous variables, affects game_over status"""
    global game_over, level_num, player, event_timer, level_clear

    if player.hearts == 0 and player.current_lives > 0:
        player.current_lives -= 1
        player.hearts = player.TOTAL_HEARTS
        # Replenishing Hearts
        replenish_all_hearts()
        player.respawn()
    if player.current_lives <= 0:
        player.current_lives = 0

    if player.fell:
        player.fell = False
        player.fall_sound.play()
        player.took_damage()

    if player.current_lives == 0 and player.hearts == 0:
        game_over = True
        menu.game_over_sound.play()

    if player.total_coins >= 50:
        player.total_coins = 0
        player.current_lives += 1
        player.extra_life_sound.play()

    if player.rect.collidepoint(end_star.rect.center):
        level_clear = True
        replenish_all_hearts()
        player.b_coin_list = []
        player.image = player.player_victory
        end_star.rect.midbottom = player.rect.midtop
        end_star.rect.centery = end_star.rect.centery - 50
        event_timer = 20
        victory_scene()

    for heart in item_group:
        if player.rect.collidepoint(heart.rect.center):
            if not player.hearts == 3:
                player.collected_heart = True
                heart.kill()
                replenish_heart()
            else:
                heart.kill()
                item.heart_sound.play()
    return False


def victory_scene():
    music.level_clear_theme.play()


def replenish_all_hearts():
    """Clears list of empty heart images in player class and replaces them with full hearts"""
    player.hearts = player.TOTAL_HEARTS
    for num in range(player.TOTAL_HEARTS):
        player.heart_list[num] = player.full_heart


def replenish_heart():
    if player.collected_heart:
        player.collected_heart = False
        player.hearts += 1
        player.heart_list[player.hearts - 1] = player.full_heart
        item.heart_sound.play()


def dropped_item():
    if player.item_dropped:
        item_group.add(HeartItem(pos=player.item_location, group=camera_group))
    player.item_location = ''


def defeated_enemy():
    if player.defeated_enemy:
        particle_group.add(DefeatParticles(group=camera_group, pos=player.enemy_location))

    player.defeated_enemy = False


def check_game_state():
    """Checks the current state of the game depending on the status of the player"""
    if not game_running:
        return 'inactive'
    if game_paused:
        return 'paused'
    if game_over:
        return 'game over'
    if level_clear:
        return 'level clear'

    return ''


particle_group = pygame.sprite.Group()


while True:

    if game_running and not game_paused and not game_over and not level_clear:
        # Screen Setup and background
        screen.fill('black')
        screen.blit(background.image, background.rect)
        # particles.get_player_pos(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_paused = True
                    menu.pause_sound.play()
                if event.key == pygame.K_UP:
                    player.rect.center = (3400, 100)

        # Status Checks
        player_status()
        replenish_heart()
        defeated_enemy()

        # Blits and Updates
        particle_group.update()
        camera_group.custom_draw(player_group)
        collect_coins()
        bab_coin_group.update()
        coin_group.update()
        ground_enemy_group.update()
        flying_group.update()
        player_group.update(screen)
        ground_group.update()
        item_group.update()
        decor_group.update()
        goal_group.update()
        dropped_item()

        # Coin and life display
        life_counter = menu.game_font_medium.render(f'{player.current_lives}', True, menu.font_color)
        coin_counter = menu.game_font_medium.render(f'{player.total_coins}', True, menu.font_color)
        screen.blit(menu.counter_1, (43, 38))
        screen.blit(menu.counter_2, (43, 64))
        screen.blit(life_counter, (55, 35))
        screen.blit(coin_counter, (55, 61))

    # Pre game/Game Over loop and game states
    if game_running and game_paused and not game_over:
        music.level_theme.stop()
        display_menu(check_game_state())

    if game_running and not game_paused and game_over:
        music.level_theme.stop()
        display_menu(check_game_state())

    if not game_running and not game_paused and not game_over:
        music.level_theme.stop()
        display_menu(check_game_state())

    if level_clear and game_running:
        victory_screen.fill('black')
        victory_screen.blit(victory_bg_surface, (0, 0))
        victory_screen.blit(player.player_victory, (570, 350))
        end_star.rect.center = (610, 300)
        goal_group.draw(victory_screen)
        goal_group.update()
        music.level_theme.stop()
        end_star.update()
        event_pause()
        if event_timer == 0:
            level_num += 1
            music.level_num += 1
            background.bg_img += 1
            music.update_music()
            background.change_background()
            level_clear = False
            player.camera_focus()
            end_star.end_star_sound.play()
            load_next_level()
            player.respawn()

    pygame.display.update()
    clock.tick(FPS)


