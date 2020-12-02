import pygame
import os
from enemies.scorpion import Scorpion
from enemies.troll import Troll
from enemies.wiz import Wiz
from towers.ArcherTower import ArcherTowerLong, ArcherTowerShort
import random
import time

class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win= pygame.display.set_mode((self.width, self.height))
        self.enemys= [Wiz()]
        self.towers = [ArcherTowerLong(300, 300), ArcherTowerShort(900,300)]
        self.lives= 10
        self.money= 100
        self.bg= pygame.image.load(os.path.join("game_assets","background.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        # self.clicks=[]  #needed just to get PATH
        self.timer= time.time()
        

    def run(self):
        run= True
        clock= pygame.time.Clock()

        while run:
            if time.time() - self.timer >= 1.5:   #co ile sekund ma wychodzić nowy wróg
                self.timer = time.time()
                self.enemys.append(random.choice([Troll(), Scorpion(), Wiz()]))

            # pygame.time.delay(0)
            clock.tick(200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    run = False
                #
                # pos= pygame.mouse.get_pos()
                #
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #      self.clicks.append(pos)
                #      print(self.clicks)

            to_delete=[]
            for en in self.enemys:
                if en.x < -50:
                    to_delete.append(en)

            #usuwa wrogów, którzy wyszli poza ekran
            for d in to_delete:
                self.enemys.remove(d)

            #przechodzi przez wieże i sprawdza czy wróg jest w strefie ataku
            for tower in self.towers:
                tower.attack(self.enemys)

            

            


            self.draw()

        pygame.quit()
        



    def draw(self):
        self.win.blit(self.bg, (0,0))
        # for click in self.clicks:
        #     pygame.draw.circle(self.win, (255,0,0), (click[0], click[1]), 3, 1)

        #narysuj wroga
        for enemy in self.enemys:
            enemy.draw(self.win)

        #narysuj wieże i łuczników
        for tow in self.towers:
            tow.draw(self.win)
    
        pygame.display.update()
        

g= Game()
g.run()