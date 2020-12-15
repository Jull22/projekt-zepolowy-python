import pygame
from .tower import Tower
import os
import math
import time

range_img= [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/supportTower", "range_tower" + ".png")),(100, 120)),
        pygame.transform.scale(pygame.image.load(os.path.join("game_assets/supportTower", "range_tower2" + ".png")),(100, 120))]


class RangeTower(Tower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.zone = 175
        self.tower_imgs= range_img[:]
        self.effect=[0.2, 0.4]
        self.width= 100
        self.height= 130
        self.name = "range"


    def draw(self, win):

        super().draw_zone(win)
        super().draw(win)


    def support(self, towers):

        effected = []
        for tower in towers:
            x= tower.x
            y= tower.y

            dis= math.sqrt((self.x - x)**2 + (self.y - y)** 2)

            if dis <= self.zone:
                effected.append(tower)

        for tower in effected:
            tower.zone = tower.original_zone + round(tower.zone * self.effect[self.level - 1])





damage_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/supportTower", "damage_tower" + ".png")),(150, 150)),
                                      pygame.transform.scale(pygame.image.load(os.path.join("game_assets/supportTower", "damage_tower2" + ".png")),(150, 150))]

class DamageTower(RangeTower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.zone = 150
        self.tower_imgs= damage_imgs[:]
        self.effect= [0.2, 0.4]
        self.name = "damage"


    def draw(self, win):

        super().draw_zone(win)
        super().draw(win)


    def support(self, towers):
        """zwiększa atak wieży w zasięgu wieży damage """
        effected = []
        for tower in towers:
            x= tower.x
            y= tower.y

            dis= math.sqrt((self.x - x)**2 + (self.y - y)** 2)

            if dis  <= self.zone + tower.width/2:
                effected.append(tower)

        for tower in effected:
            tower.damage = tower.original_damage + self.effect[self.level - 1]


