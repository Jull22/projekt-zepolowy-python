import pygame
import os
from .enemy import Enemy 

class Scorpion(Enemy):
    imgs = []

    for x in range(20):
        string= str(x)
        
        if x < 10:
            string= "0" + string
            imgs.append(pygame.image.load(os.path.join("game_assets/monsters/PNG/1", "1_enemies_1_run_0" + string + ".png")))
        else: 

            imgs.append(pygame.image.load(os.path.join("game_assets/monsters/PNG/1", "1_enemies_1_run_0" + string + ".png")))
    
    def __init__(self):
        super().__init__()