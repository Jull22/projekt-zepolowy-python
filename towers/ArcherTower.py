import pygame 
from .tower import Tower
import os
import math
import time

tower_imgs1 = []
archer_imgs1 = []

# wieża długodystansowa
for x in range(1,4):
    tower_imgs1.append(
        pygame.transform.scale(pygame.image.load(os.path.join("game_assets/archerTower/1", str(x) + ".png")), (150, 130)))
# łucznik
for x in range(1, 24):
    archer_imgs1.append(
        pygame.transform.scale(pygame.image.load(os.path.join("game_assets/archer/1", str(x) + ".png")), (90, 90)))

class ArcherTowerLong(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs= tower_imgs1
        self.archer_imgs= archer_imgs1
        self.archer_count = 0
        self.zone = 200
        self.inZone = False
        self.right= True
        self.timer = time.time()
        self.damage = 1






    def draw(self, win):


        if self.inZone:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 6:
                self.archer_count = 0
        else:
            self.archer_count=0

        super().draw(win)  # rysuje wieżę
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


        self.inZone = False
        close_enemy= []
        for enemy in enemies:

            x, y = enemy.x, enemy.y
            distance = math.sqrt((self.x-x)**2 + (self.y - y)**2)
            if distance < self.zone:
                self.inZone = True
                close_enemy.append(enemy)


        close_enemy.sort(key=lambda x: x.x)
        if len(close_enemy) > 0 :

            first_enemy= close_enemy[0]
            if time.time() - self.timer>= 0.5:
                self.timer = time.time()
                if first_enemy.hit() == True:
                    enemies.remove(first_enemy)

            if first_enemy.x < self.x and self.right:

                self.right=False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif not(self.right) and first_enemy.x > self.x :
                self.right=True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x]= pygame.transform.flip(img, True, False)

tower_imgs= []
# wieża krótkodystansowa
for x in range(1, 4):
    tower_imgs.append(
        pygame.transform.scale(pygame.image.load(os.path.join("game_assets/archerTower/2", str(x) + ".png")),
                               (150, 150)))
# łucznik
archer_imgs= []
for x in range(1, 24):
    archer_imgs.append(
        pygame.transform.scale(pygame.image.load(os.path.join("game_assets/archer/2", str(x) + ".png")),
                               (100, 100)))


class ArcherTowerShort(ArcherTowerLong):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs
        self.archer_imgs = archer_imgs
        self.archer_count = 0
        self.zone = 200
        self.inZone = False
        self.right = True
        self.timer = time.time()
        self.damage = 1


