import pygame
import os

class Button:
    def __init__(self, x, y, img, name):
        self.x = x
        self.y = y
        self.img = img
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.name = name



    def click(self, X, Y):
        """
        Sprawdza czy pozycja obiektow koliduje z menu
        :param X:
        :param Y:
        :return:
        """
        if X <= self.x + self.width and X>= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False


    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

class Menu:

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_names = []
        self.items = 0
        self.buttons= []
        self.bg= img

    def add_btn(self, img, name):
        """
        dodawanie przycisków do menu
        :param img: surface
        :param name: string
        :return: None
        """
        self.items += 1
        inc_x = self.width/self.x
        btn_x = self.x - self.bg.get_width()/2 + 35
        btn_y = self.y -167
        self.buttons.append(Button(btn_x, btn_y, img, name))

    def draw(self, win):
        """
        narysuj przyciski i menu
        :param win: surface
        :return: None
        """
        win.blit(self.bg, (self.x - self.bg.get_width()/2 + 25, self.y-170))
        for item in self.buttons:
            item.draw(win)


    def get_clicked(self, X, Y):
        for button in self.buttons:
            if button.click(X,Y):
                return button.name

