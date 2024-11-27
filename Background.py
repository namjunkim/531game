import pygame
class Background :
    def __init__(self, background_music, screen_width, screen_height):
        self.background_music = background_music
        self.screen_width = screen_width
        self.screen_height = screen_height

    def run_background_music(self):
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1)

    def set_background_screen(self):
        return pygame.display.set_mode((self.screen_width, self.screen_height))

