import pygame
class Player:

    def __init__(self,
                 player_img_path, player_score, player_height, player_length,
                 player_power, player_bullet_per_amount, player_bullet_img_path,
                 player_bullet
                 ):
        self.player_img_path = player_img_path
        self.player_score = player_score
        self.player_height = player_height
        self.player_length = player_length
        self.player_bullet_img_path = player_bullet_img_path
        self.player_img = ''

    def make_player_rect(self, player_img):
        return player_img.get_rect()
    def make_player_img(self):
        self.player_img = pygame.image.load(self.player_img_path)
        self.player_img = pygame.transform.scale(self.player_img, (self.player_height, self.player_length))
        return self.player_img
