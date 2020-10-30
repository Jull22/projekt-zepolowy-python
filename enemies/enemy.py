import pygame
import math


class Enemy:
    imgs = []

    def __init__(self):

        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 1
        self.vel = 3
        self.path = [(10, 146), (129, 150), (274, 153), (423, 147), (573, 146), (716, 151), (787, 205), (803, 285), (770, 341), (696, 371), (623, 399), (584, 464), (585, 530), (555, 569), (485, 590), (409, 599), (288, 606), (169, 601), (54, 599), (1, 599), (-20,900)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.dis = 0

    def draw(self, win):

        #rysuje enemy - obrazek 

        
        self.img= self.imgs[self.animation_count//3]
        self.animation_count +=1
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0 
        win.blit(self.img, (self.x, self.y))
        self.move()

        pass


    def collide(self, X, Y):

        if X < self.x + self.width and X>= self.x:
            if Y <= self.y + self.height and Y>= self.y:
                return True

        return False

    def move(self):
        
        #ruch wroga

        x1,y1= self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2= (-10, 610)   #wróg ma wyjść poza widziany obszar jeśli jest to już na końcu ścieżki
        else: 
            x2, y2 = self.path[self.path_pos + 1]

        move_dis = math.sqrt((x2-x1)**2 + (y2- y1)**2)

        self.move_count+= 1
        direction= (x2-x1, y2-y1)

        move_x, move_y= (self.x + direction[0] * self.move_count, self.y + direction[1] * self.move_count)
        self.dis += math.sqrt((move_x - x1)**2 + (move_y - y1)**2)

        if self.dis >= move_dis:
            self.dis = 0
            self.move_count = 0
            self.path_pos += 1
            if self.path_pos >= len(self.path):
                self.path_pos = 0

        self.x = move_x
        self.y= move_y

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True