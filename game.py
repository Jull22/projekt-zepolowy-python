import pygame
import os
from enemies.scorpion import Scorpion
from enemies.ghost import Ghost
from enemies.wiz import Wiz
from towers.ArcherTower import ArcherTowerLong, ArcherTowerShort
from towers.assistant_tower import RangeTower, DamageTower

import random
import time
pygame.font.init()

health_img = pygame.image.load(os.path.join("game_assets", "heart.png"))
# star_img = pygame.image.load(os.path.join("game_assets", "star.png"))


class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win= pygame.display.set_mode((self.width, self.height))
        self.enemys= [Wiz()]
        self.support_towers= [RangeTower(400, 500), DamageTower(300, 300)]
        self.attack_towers = [ArcherTowerLong(300, 300), ArcherTowerShort(900, 300)]
        self.lives= 10
        self.money= 100
        self.bg= pygame.image.load(os.path.join("game_assets","background.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        # self.clicks=[]  #needed just to get PATH
        self.timer= time.time()
        self.health_font= pygame.font.SysFont("sourcesanspro", 70, bold=200)

    def run(self):
        run= True
        clock= pygame.time.Clock()

        while run:
            if time.time() - self.timer >= 0.5:   #co ile sekund ma wychodzić nowy wróg
                self.timer = time.time()
                self.enemys.append(random.choice([Ghost(), Scorpion(), Wiz()]))

            # pygame.time.delay(0)
            clock.tick(80)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    run = False

            # pos= pygame.mouse.get_pos()

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
            for tow in self.attack_towers:
                tow.attack(self.enemys)

            #sprawdza czy wieże atakujące się w strefie
            for t in self.support_towers:
                t.support(self.attack_towers)

            #przegrana
            if self.lives<= 0 :
                print("Porażka")
                run = False


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
        for tow in self.attack_towers:
            tow.draw(self.win)

        # narysuj wieże wspierające
        for tower in self.support_towers:
            tower.draw(self.win)


        #narysuj serca- życia
        text= self.health_font.render(str(self.lives), 1, (0, 0, 0))

        life= pygame.transform.scale(health_img, (50, 50))
        start_x = self.width - life.get_width()-10

        self.win.blit(text, (start_x - text.get_width()- 1, 5))
        self.win.blit(life, (start_x, 25))

        pygame.display.update()

        def menu(self):
            pass

        

g= Game()
g.run()