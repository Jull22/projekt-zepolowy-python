import pygame
from game import Game
import os

play_btn = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/buttons", "play.png")), (1000,400))

class StartMenu:
    def __init__(self):
        self.width = 1350
        self.height = 700
        self.bg = pygame.image.load(os.path.join("game_assets", "background.jpg"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win =pygame.display.set_mode((1200, 700))

        self.btn = (self.width/2-580 , 150, play_btn.get_width(), play_btn.get_height())

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    # check if hit start btn
                    x, y = pygame.mouse.get_pos()

                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            game = Game(self.win)
                            game.run()
                            del game
            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        self.win.blit(play_btn, (self.btn[0], self.btn[1]))
        pygame.display.update()