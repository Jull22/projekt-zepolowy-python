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
        self.path = [(10, 130), (129, 130), (274, 140), (423, 150), (573, 150), (716, 151), (787, 205), (803, 285), (770, 341), (696, 371), (623, 399), (584, 464), (570, 530), (555, 530), (485, 615), (409, 615), (288, 615), (169, 615), (54, 615), (1, 615), (-20,900)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.imgs=[]
        self.path_pos = 0
        self.move_dis = 0
        self.dis = 0
        self.flipped= False

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
        if self.path_pos + 1 >= len(self.path):  #jeśli jesteśmy na końcu iteracji przez ścieżkę
            x2, y2= (-10, 610)   #wróg ma wyjść poza widziany obszar jeśli jest już na końcu ścieżki
        else: 
            x2, y2 = self.path[self.path_pos + 1]   #w innym wypadku idziemy do kolejnego punktu

        #move_dis = math.sqrt((x2-x1)**2 + (y2- y1)**2)   #dystans jaki dzieli punkty 

         
        direction= (x2-x1, y2-y1)   #kierunek przesunięcia
        


        if direction[0]<0 and not(self.flipped):   #jeśli wróg idzie w drugą stronę to musimy go odwrócić
            self.flipped= True
            for x, img in enumerate(self.imgs):
                self.imgs[x] = pygame.transform.flip(img, True, False)


        move_x, move_y= (self.x + direction[0] , self.y + direction[1] -4 )
        # self.dis += math.sqrt((move_x - x1)**2 + (move_y - y1)**2)   #dystans o jaki chcemy przesunąć wroga
      
        self.x = move_x
        self.y= move_y 


        # self.dis = 0
        self.path_pos += 1
        if self.path_pos >= len(self.path):
            return False

        

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True