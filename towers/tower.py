import pygame

class Tower:

    def __init__(self, x,y):
        self.x= x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_cost = [0,0,0]
        self.price = [0,0,0]
        self.level = 1
        self.selected= False
        self.menu= None
        self.damage= 1

    def draw(self, win):

        img = self.tower_imgs[self.level-1]
        win.blit(img, ((self.x + self.width) - (img.get_width())/3, (self.y - img.get_height())))
        
    def click(self, X, Y):
        """wybranie wieży
            param:X: int
            param:Y:int
            return: Boolean"""
        

        if X < self.x + self.width and X>= self.x:
            if Y <= self.y + self.height and Y>= self.y:
                return True

        return False

    def sell(self):
        return self.sell_cost[self.level-1]

    def upgrade(self):
        """ulepszenie wieży   """
        self.level += 1
        self.damage+= 1
        
    def get_upgrade_cost(self):
        """ cena za ulepszenie"""
        return self.price[self.level-1]

    def move(self, x, y):
        self.x = x
        self.y = y


