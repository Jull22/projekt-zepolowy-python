import pygame 
from .tower import Tower
import os

class ArcherTower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs= []
        self.stone_imgs= []
        self.stone_count = 0

        #wieża 1
        self.tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/stone-towers/PNG", "3" + ".png")), (64,64)))
        self.stone_imgs.append(pygame.image.load(os.path.join("game_assets/stone-towers/PNG", "40" + ".png")))
            


    def draw(self, win):
        super().draw(win)
        if self.stone_count >= len(self.stone_imgs):
            self.stone_count= 0

        stone=self.stone_imgs[self.stone_count]
        win.blit(self.tower_imgs[0], (self.x + self.width/2)- (stone.get_width()/2), (self.y - stone.get_height()/2))
        win.blit(stone, ((self.x + self.width/2)- (stone.get_width()/2), (self.y - stone.get_height()/2)))
        self.stone_count+= 1
                
                


    def attack(self, enemies):
        pass