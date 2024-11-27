import pygame
class Enemy:

    def __init__(self,
                 enemy_img_path, enemy_score, enemy_height, enemy_length,
                 enemy_power, enemy_bullet_per_amount, enemy_bullet_img_path,
                 enemy_bullet
                 ):
        self.enemy_img_path = enemy_img_path
        self.enemy_score = enemy_score
        self.enemy_height = enemy_height
        self.enemy_length = enemy_length
        self.enemy_bullet_img_path = enemy_bullet_img_path
        self.enemy_img = ''


    def make_enemy_rect(self, enemy_img):
        return enemy_img.get_rect()
    def make_enemy_img(self):
        self.enemy_img = pygame.image.load(self.enemy_img_path)
        self.enemy_img = pygame.transform.scale(self.enemy_img, (self.enemy_height, self.enemy_length))
        return self.enemy_img