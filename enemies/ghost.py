import pygame
import os
from .enemy import Enemy 

imgs= []

for x in range(20):
    string= str(x)

    if x < 10:
        string= "0" + string
        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/monsters/PNG/10", "10_enemies_1_run_0" + string + ".png")), (90,64)))
    else:

        imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/monsters/PNG/10", "10_enemies_1_run_0" + string + ".png")), (90,64)))


class Ghost(Enemy):
    def __init__(self):
        super().__init__()
        self.name= "ghost"
        self.money = 15
        self.max_health = 3
        self.health = self.max_health
        self.imgs = imgs[:]




