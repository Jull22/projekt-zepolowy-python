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
        self.tower_imgs=[]

    def draw(self, win):

        img = self.tower_imgs[self.level-1]
        win.blit(img, (self.x - (img.get_width())/3, (self.y - img.get_height())))



    def draw_zone(self, win):
        #draw zone
        if self.selected:
            strefa= pygame.Surface((self.zone*4, self.zone*4), pygame.SRCALPHA, 32)
            pygame.draw.circle(strefa, (128, 128, 189, 100), (self.zone, self.zone), self.zone, 0)

            win.blit(strefa, (self.x- self.zone +20, self.y- self.zone-70))



    def zone_of_attack(self, r):
        """
        :param r:
        :return: None

        zasięg ataku wieży
        """
        self.zone = r

    def click(self, X, Y):
        """wybranie wieży
            param:X: int
            param:Y:int
            return: Boolean"""
        
        img = self.tower_imgs[self.level-1]    #120x120x32
        if X <= self.x- img.get_width() +95 + self.width and X>= self.x- img.get_width()+95 :
            if Y  <= self.y - img.get_height() + 10 + self.height and Y>= self.y - img.get_height()-30:
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


