import pygame 
from .tower import Tower
import os
import math

class ArcherTowerLong(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs= []
        self.archer_imgs= []
        self.archer_count = 0
        self.zone = 200
        self.inZone = False
        self.right= True

        #wieża 1,2,3
        for x in range(1, 4):
            self.tower_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/archerTower", str(x) + ".png")), (120, 120)))
        #łucznik
        for x in range(1, 24):
            self.archer_imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("game_assets/archer", str(x) + ".png")), (80, 80)))



    def draw(self, win):
        super().draw(win)   #rysuje wieżę

        if self.inZone:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 6:
                self.archer_count = 0
        else:
            self.archer_count=0
        archer = self.archer_imgs[self.archer_count // 6]
        win.blit(archer, ((self.x + self.width / 2) - (archer.get_width() / 3.5),(self.y - archer.get_height() * 2.2)))  # rysuje łuczników


        #draw zone
        strefa= pygame.Surface((self.zone*4, self.zone*4), pygame.SRCALPHA, 32)
        pygame.draw.circle(strefa, (128, 128, 189, 100), (self.zone, self.zone), self.zone, 0)

        win.blit(strefa, (self.x- self.zone +9, self.y- self.zone-70))
        super().draw(win)


    def zone_of_attack(self, r):
        """
        :param r:
        :return: None

        zasięg ataku wieży
        """
        self.zone = r


    def attack(self, enemies):
        # atak wroga
        for enemy in enemies:
            x, y = enemy.x, enemy.y

            self.inZone = False
            close_enemy= []
            distance = math.sqrt((self.x-x)**2 + (self.y - y)**2)
            if distance < self.zone:
                self.inZone = True
                close_enemy.append(enemy)


        close_enemy.sort(key=lambda x: x.x)
        if len(close_enemy) > 0 :

            first_enemy= close_enemy[0]

            if first_enemy.x < self.x and self.right:

                self.right=False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif not(self.right) and first_enemy.x > self.x :
                self.right=True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x]= pygame.transform.flip(img, True, False)


