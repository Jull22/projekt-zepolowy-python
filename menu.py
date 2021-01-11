import pygame
import os

star = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "star.png")), (25,25))

class Button:
    def __init__(self, menu, img, name):
        self.x = menu.x - 30
        self.y = menu.y - 168
        self.img = img
        self.menu= menu
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.name = name



    def click(self, X, Y):
        """
        Sprawdza czy pozycja obiektow koliduje z menu
        :param X: int
        :param Y: int
        :return: bool
        """
        if X <= self.x + self.width and X>= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False


    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def update(self):
        self.x = self.menu.x - 30
        self.y = self.menu.y - 168

class Menu:

    def __init__(self, tower, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_names = []
        self.items = 0
        self.item_cost = item_cost
        self.buttons= []
        self.bg= img
        self.font = pygame.font.SysFont("sourcesanspro", 17, bold=200)
        self.tower = tower

    def add_btn(self, img, name):
        """
        dodawanie przycisków do menu
        :param img: surface
        :param name: string
        :return: None
        """
        self.items += 1
        btn_x = self.x - self.bg.get_width()/2 + 35
        btn_y = self.y -167
        self.buttons.append(Button(self, img, name))

    def get_item_cost(self):
        """
        cena za ulepszenie wieży
        :return:
        """

        return self.item_cost[self.tower.level -1]

    def draw(self, win):
        """
        narysuj przyciski i menu
        :param win: surface
        :return: None
        """
        win.blit(self.bg, (self.x - self.bg.get_width()/2 + 25, self.y-170))
        for item in self.buttons:
            item.draw(win)
            win.blit(star, (item.x + item.width * 1.5 + 5, item.y + 3))                     #rysuje gwiazdke
            text = self.font.render(str(self.item_cost[self.tower.level-1]), 1, (255,255,255))
            win.blit(text, (item.x + item.width + 25 , item.y + 24))                        #rysuje kwotę

    def get_upgrade_cost(self, name):
        return self.menu.get_item_cost()



    def get_clicked(self, X, Y):
        for button in self.buttons:
            if button.click(X,Y):
                return button.name


        return None

    def update(self):
        for btn in self.buttons:
            btn.update()

class PausePlayButton(Button):
    def __init__(self, start_btn, pause_btn, x, y):
        self.x = x
        self.y = y
        self.img = start_btn
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.pause = pause_btn
        self.start= start_btn

    def start_pause_img(self):
        if self.img == self.start:
            self.img == self.pause
        else:
            self.img == self.start

class VerticalButton(Button):
    def __init__(self, x, y, img, name, cost):
        self.x = x
        self.y = y
        self.img = img

        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.name = name
        self.cost= cost



    def click(self, X, Y):
        """
        Sprawdza czy pozycja obiektow koliduje z menu
        :param X: int
        :param Y: int
        :return: bool
        """
        if X <= self.x + self.width and X>= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False


    def draw(self, win):
        win.blit(self.img, (self.x, self.y))


class VerticalMenu(Menu):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.items = 0
        self.buttons = []
        self.bg = img
        self.font = pygame.font.SysFont("sourcesanspro", 17, bold=200)


    def add_btn(self, img, name, cost):
        """
        dodawanie przycisków do menu
        :param img: surface
        :param name: string
        :return: None
        """
        self.items += 1
        btn_x = self.x - 9
        btn_y = self.y + (self.items-1) * 110 - 153
        self.buttons.append(VerticalButton(btn_x, btn_y, img, name, cost))

    def get_item_cost(self, name):
        #koszt wieży
        for btn in self.buttons:
            if btn.name == name:
                return btn.cost

        return -1

    def draw(self, win):
        """
        narysuj przyciski i menu
        :param win: surface
        :return: None
        """
        win.blit(self.bg, (self.x - self.bg.get_width()/2 + 25, self.y-170))
        for item in self.buttons:
            item.draw(win)
            win.blit(star, (item.x  , item.y + 60))                     #rysuje gwiazdke
            text = self.font.render(str(item.cost), 1, (255,255,255))
            win.blit(text, (item.x + 24 , item.y + 68))                        #rysuje kwotę