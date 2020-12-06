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
        pygame.transform.scale(pygame.image.load(os.path.join("game_assets/archerTower/2", str(x) + ".png")), (120, 120)))
# łucznik
for x in range(2, 19):
    archer_imgs1.append(
        pygame.transform.scale(pygame.image.load(os.path.join("game_assets/archer/2", str(x) + ".png")), (100, 100)))

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
        self.original_zone= self.zone



    def draw(self, win):

        super().draw_zone(win)
        super().draw(win)

        if self.inZone:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 7:
                self.archer_count = 0
        else:
            self.archer_count=0


        archer = self.archer_imgs[self.archer_count // 9]

        win.blit(archer, ((self.x + self.width / 2) - (archer.get_width() / 4.6),
                          (self.y - archer.get_height() * 1.9)))                    # rysuje łuczników



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

                if first_enemy.hit(self.damage) == True:
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
        pygame.transform.scale(pygame.image.load(os.path.join("game_assets/archerTower/1", str(x) + ".png")),
                               (120, 120)))
# łucznik
archer_imgs= []
for x in range(2, 19):
    archer_imgs.append(
        pygame.transform.scale(pygame.image.load(os.path.join("game_assets/archer/1", str(x) + ".png")),
                               (100, 100)))


class ArcherTowerShort(ArcherTowerLong):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs
        self.archer_imgs = archer_imgs
        self.archer_count = 0
        self.zone = 150
        self.inZone = False
        self.right = True
        self.timer = time.time()
        self.damage = 1


