import pygame
from menu import Menu
import os, math

menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "menu.png")), (125, 50))
upgrade = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "upgrade.png")), (45,45))
star = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "star.png")), (25,25))



class Tower:

    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_cost = [0,0,0]
        self.price = [0,0,0]
        self.level = 1
        self.selected= False
        self.menu= Menu(self, self.x, self.y, menu_bg, [2000,"MAX"])
        self.menu.add_btn(upgrade, "Upgrade")

        self.damage= 1
        self.place_color= (179, 179, 230, 100)
        self.tower_imgs=[]



    def draw(self, win):

        img = self.tower_imgs[self.level-1]
        win.blit(img, (self.x - (img.get_width())/3, (self.y - img.get_height())))
        if self.selected:
            self.menu.draw(win)




    def draw_zone(self, win):
        #draw zone
        if self.selected:
            strefa= pygame.Surface((self.zone*4, self.zone*4), pygame.SRCALPHA, 32)
            pygame.draw.circle(strefa, self.place_color, (self.zone, self.zone), self.zone, 0)

            win.blit(strefa, (self.x- self.zone +20, self.y- self.zone-70))

    def draw_placement(self, win):
        #draw zone

        strefa= pygame.Surface((self.zone*4, self.zone*4), pygame.SRCALPHA, 32)
        pygame.draw.circle(strefa, self.place_color, (62,62), 62, 0)

        win.blit(strefa, (self.x-45 , self.y-125))



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

        if self.level <  len(self.tower_imgs):

            self.level += 1
            self.damage+= 1
        
    def get_upgrade_cost(self):
        """ cena za ulepszenie"""
        return self.price[self.level-1]

    def move(self, x, y):
        #przenosi wieżę na daną pozycję x i y
        self.x = x
        self.y = y
        self.menu.x= x
        self.menu.y= y
        self.menu.update()

    def collide(self, otherTower):
        x2= otherTower.x
        y2= otherTower.y


        dist= math.sqrt((x2-self.x)**2 + (y2-self.y)**2)
        if dist >= 80:
            return False
        else:
            return True



