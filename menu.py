import pygame


class Menu:
    def __init__(self):
        # Gathering Fonts
        self.game_font_small = pygame.font.Font('font/PressStart2P-Regular.ttf', size=10)
        self.game_font_medium = pygame.font.Font('font/PressStart2P-Regular.ttf', size=14)
        self.game_font_options = pygame.font.Font('font/PressStart2P-Regular.ttf', size=32)
        self.game_font_large = pygame.font.Font('font/PressStart2P-Regular.ttf', size=56)
        self.font_color = '#363355'

        # Displaying in-game counters and basic fonts
        self.counter_1 = self.game_font_small.render('x', True, self.font_color)
        self.counter_2 = self.game_font_small.render('x', True, self.font_color)

        # Setting up pause and main menus
        self.bg_surface = pygame.image.load('graphics/UI/menu_ui/menu_bg.png')
        self.game_over_bg = pygame.image.load('graphics/UI/menu_ui/game_over_bg.png')
        self.pause_surface = self.game_font_large.render('PAUSED', True, 'White')
        self.main_menu_surface = self.game_font_large.render('MAIN MENU', True, 'White')
        self.game_over_surface = self.game_font_large.render('GAME OVER', True, 'White')
        self.resume_surface = self.game_font_options.render('Resume', True, 'White')
        self.play_surface = self.game_font_options.render('Play', True, 'White')
        self.quit_surface = self.game_font_options.render('Quit', True, 'White')
        self.restart_surface = self.game_font_options.render('Restart', True, 'White')
        self.button_surface_1 = pygame.image.load('graphics/UI/menu_ui/button_not_pressed.png').convert_alpha()
        self.button_surface_2 = pygame.image.load('graphics/UI/menu_ui/button_not_pressed.png').convert_alpha()
        self.pressed_button = pygame.image.load('graphics/UI/menu_ui/button_pressed.png').convert_alpha()
        self.unpressed_button = pygame.image.load('graphics/UI/menu_ui/button_not_pressed.png').convert_alpha()
        self.button_rect_1 = self.button_surface_1.get_rect(topleft=(415, 280))
        self.button_rect_2 = self.button_surface_2.get_rect(topleft=(415, 420))


        #Menu Sounds
        self.pause_sound = pygame.mixer.Sound('audio/pause.mp3')
        self.unpause_sound = pygame.mixer.Sound('audio/unpause.mp3')
        self.game_over_sound = pygame.mixer.Sound('audio/game_over.wav')

