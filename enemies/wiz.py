import pygame
import os
from .enemy import Enemy 

class Wiz(Enemy):
    
    

    def __init__(self):
        super().__init__()
        self.imgs = []
    
        for x in range(20):
            string= str(x)
            
            if x < 10:
                string= "0" + string
                self.imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/monsters/PNG/2", "2_enemies_1_run_0" + string + ".png")), (64,64)))
            else: 

                self.imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/monsters/PNG/2", "2_enemies_1_run_0" + string + ".png")), (64,64)))