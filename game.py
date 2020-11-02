import pygame
import os
from enemies.scorpion import Scorpion
from enemies.troll import Troll
from enemies.wiz import Wiz

class Game:
    def __init__(self):
        self.width = 1200
        self.height = 700
        self.win= pygame.display.set_mode((self.width, self.height))
        self.enemys= [Scorpion(), Troll(), Wiz()]
        self.towers = []
        self.lives= 10
        self.money= 100
        self.bg= pygame.image.load(os.path.join("game_assets","background.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.clicks=[]  #needed just to get PATH 
        

    def run(self):
        run= True

    
        clock= pygame.time.Clock()

        while run:
            pygame.time.delay(3)
            clock.tick(2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    run = False
                
                pos= pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                     self.clicks.append(pos)
                     print(self.clicks)

            to_delete=[]
            for en in self.enemys:
                if en.x < -5:
                    to_delete.append(en)

            for d in to_delete:
                self.enemys.remove(d)

            


            self.draw()

        pygame.quit()
        



    def draw(self):
        self.win.blit(self.bg, (0,0))
        for click in self.clicks:
             pygame.draw.circle(self.win, (255,0,0), (click[0], click[1]), 3, 1)

        #narysuj wroga
        for enemy in self.enemys:
            enemy.draw(self.win)
        pygame.display.update()

g= Game()
g.run()