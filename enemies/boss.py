import pygame
import os
from .enemy import Enemy

imgs= []

for x in range(20):
    string= str(x)

    if x < 10:
        string= "0" + string
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/monsters/PNG/7", "7_enemies_1_run_0" + string + ".png")), (120,94)))
    else:

        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/monsters/PNG/7", "7_enemies_1_run_0" + string + ".png")), (120,94)))


class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.name= "boss"
        self.money = 600
        self.max_health = 25
        self.health = self.max_health
        self.imgs = imgs[:]




